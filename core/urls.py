from rest_framework import routers

from core.views import ServiceViewSet, TerminalViewSet

app_name = "core"

router = routers.DefaultRouter()
router.register(prefix="terminalS", viewset=TerminalViewSet, basename="terminal")
router.register(prefix="services", viewset=ServiceViewSet, basename="service")
urlpatterns = router.urls