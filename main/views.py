from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TransactionForm
from .models import Transaction


def transaction_list(request):
    transactions = Transaction.objects.all()

    transaction_type = request.GET.get("type", "")
    status = request.GET.get("status", "")
    sort = request.GET.get("sort", "date")

    if transaction_type in ["income", "expense"]:
        transactions = transactions.filter(
            transaction_type=transaction_type
        )

    if status == "paid":
        transactions = transactions.filter(is_paid=True)
    elif status == "unpaid":
        transactions = transactions.filter(is_paid=False)

    allowed_sorts = {
        "date": "date",
        "-date": "-date",
        "name": "name",
        "-name": "-name",
        "amount": "amount",
        "-amount": "-amount",
    }

    transactions = transactions.order_by(
        allowed_sorts.get(sort, "date"),
        "id",
    )

    total_income = (
        Transaction.objects.filter(
            transaction_type="income"
        ).aggregate(total=Sum("amount"))["total"] or 0
    )

    total_expenses = (
        Transaction.objects.filter(
            transaction_type="expense"
        ).aggregate(total=Sum("amount"))["total"] or 0
    )

    context = {
        "transactions": transactions,
        "form": TransactionForm(),
        "transaction_type": transaction_type,
        "status": status,
        "sort": sort,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_total": total_income - total_expenses,
    }

    return render(request, "main/transactions.html", context)


def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm()

    return render(request, "main/add_transaction.html", {"form": form})


def toggle_paid(request, transaction_id):
    if request.method == "POST":
        transaction = get_object_or_404(
            Transaction,
            pk=transaction_id,
        )
        transaction.is_paid = not transaction.is_paid
        transaction.save(update_fields=["is_paid"])

    return redirect("transaction_list")


def delete_transaction(request, transaction_id):
    if request.method == "POST":
        transaction = get_object_or_404(
            Transaction,
            pk=transaction_id,
        )
        transaction.delete()

    return redirect("transaction_list")