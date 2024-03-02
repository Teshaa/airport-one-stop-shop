from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to="upload/logo")
    location = models.CharField(max_length=255, help_text="Location of the restaurant within JKIA (e.g., Terminal 1, Gate 15)")

class FoodItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="food_items")
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.IntegerField(help_text="Estimated time in minutes to prepare the food item")
    readily_available = models.BooleanField(null=True, blank=True)
    image = models.ImageField(upload_to="upload/food")

class FoodOrder(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="orders")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="orders")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=(
        ("cancelled", "Cancelled"),
        ("pending", "Pending"),
        ("delivered", "Delivered"),
    ))

# asociation
class OrderItem(models.Model):
    order = models.ForeignKey(FoodOrder, on_delete=models.CASCADE, related_name="order_items")
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.IntegerField()
