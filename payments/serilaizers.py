from rest_framework import serializers

from payments.models import Payment


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "id", "reservation", "food_order",
            "merchant_request_id", "checkout_request_id",
            "result_code", "result_description", "mpesa_receipt_number",
            "transaction_date", "phone_number", "ammount",
            "created_at", "updated_at"
        )
        extra_kwargs = {

        }
