from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "name",
            "description",
            "transaction_type",
            "amount",
            "date",
            "frequency",
            "is_paid",
            "category",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter name",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
            }),
            "amount": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "0.00",
            }),
            "date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
            "category": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter category",
            }),
        }