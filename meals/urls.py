from rest_framework import routers

from meals.views import FoodItemViewSet, FoodOrderViewSet, FoodTypeViewSet, OrderItemViewset, RestaurantViewSet
app_name = "meals"


router = routers.DefaultRouter()
router.register(prefix="food-types", basename="food-type", viewset=FoodTypeViewSet)
router.register(prefix="orders", basename="order", viewset=FoodOrderViewSet)
router.register(prefix="restaurants", basename="restaurant", viewset=RestaurantViewSet)
router.register(prefix="", basename="food", viewset=FoodItemViewSet)

urlpatterns = router.urls