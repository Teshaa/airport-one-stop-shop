from django.urls import path, include
from rest_framework import routers

from core.views import ServiceViewSet, TerminalViewSet, OrderView

app_name = "core"

router = routers.DefaultRouter()
router.register(prefix="terminalS", viewset=TerminalViewSet, basename="terminal")
router.register(prefix="services", viewset=ServiceViewSet, basename="service")
urlpatterns = [
    path("", include(router.urls)),
    path("orders/", OrderView.as_view()),
]
