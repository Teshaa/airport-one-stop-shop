from rest_framework import routers

from payments.views import PaymentViewSet

app_name = "payments"

router = routers.DefaultRouter()

router.register("", viewset=PaymentViewSet, basename="payments")

urlpatterns = router.urls
