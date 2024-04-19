from django.db import models


class RestaurantImage(models.Model):
    image = models.ImageField(upload_to="upload/restaurant")
    restaurant = models.ForeignKey("meals.Restaurant", on_delete=models.CASCADE, related_name="images")


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    address = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to="upload/logo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["-updated_at"]


class FoodType(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="meales/types")
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["-updated_at"]


class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="food_items")
    type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name="food_items")
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.IntegerField(help_text="Estimated time in minutes to prepare the food item", null=True,
                                           blank=True)
    readily_available = models.BooleanField(null=True, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=3)
    image = models.ImageField(upload_to="upload/food")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["-updated_at"]


class FoodOrder(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="orders")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255, choices=(
        ("cancelled", "Cancelled"),
        ("pending", "Pending"),
        ("delivered", "Delivered"),
    ), default="pending")
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="food_orders")
    quantity = models.IntegerField()
    # terminal = models.ForeignKey("core.Terminal", related_name="orders", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.food_item} order"
    

    class Meta:
        ordering = ["-status", "-updated_at"]




# -1.3275419276289535, 36.892774467385905