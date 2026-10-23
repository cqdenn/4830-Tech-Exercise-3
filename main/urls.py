from django.urls import path
from . import views

urlpatterns = [
    path("", views.transaction_list, name="transaction_list"),
    path("add/", views.add_transaction, name="add_transaction"),
    path(
        "toggle-paid/<int:transaction_id>/",
        views.toggle_paid,
        name="toggle_paid",
    ),
    path(
        "delete/<int:transaction_id>/",
        views.delete_transaction,
        name="delete_transaction",
    ),
]