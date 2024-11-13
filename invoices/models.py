from django.db import models


# Create your models here.
class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=32, unique=True)
    customer_name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self) -> str:
        return f"Invoice {self.invoice_number} - {self.customer_name}"


class InvoiceDetail(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="details"
    )
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)
