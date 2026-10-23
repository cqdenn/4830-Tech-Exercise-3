from django.db import models

# Create your models here.
class Transaction(models.Model):

    TYPE_CHOICES = [
        ("income", "Income"),
        ("expense", "Expense"),
    ]

    FREQUENCY_CHOICES = [
        ("none", "Does not repeat"),
        ("weekly", "Weekly"),
        ("monthly", "Monthly"),
        ("yearly", "Yearly"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    transaction_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    frequency = models.CharField(
        max_length=10,
        choices=FREQUENCY_CHOICES,
        default="none",
    )
    is_paid = models.BooleanField(default=False)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} - ${self.amount}"
