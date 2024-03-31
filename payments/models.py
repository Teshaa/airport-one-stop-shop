from django.db import models


# Create your models here.
class Payment(models.Model):
    reservation = models.OneToOneField("hotels.Reservation", on_delete=models.CASCADE, related_name="payments",
                                       null=True, blank=True)
    food_order = models.OneToOneField(
        'meals.FoodOrder', on_delete=models.CASCADE,
        related_name="payments", null=True,
        blank=True,
    )
    merchant_request_id = models.CharField(max_length=100)
    checkout_request_id = models.CharField(max_length=100)
    result_code = models.IntegerField()
    result_description = models.TextField()
    mpesa_receipt_number = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    transaction_date = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=13,
        null=True,
        blank=True
    )
    ammount = models.DecimalField(max_digits=13, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
