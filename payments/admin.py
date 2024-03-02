from django.contrib import admin
from .models import Payment
# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "reservation", "food_order","merchant_request_id", "checkout_request_id", 
        "result_code",  "result_description", "mpesa_receipt_number", "transaction_date",
        "phone_number", "ammount","created_at", "created_at", "updated_at"        
        )