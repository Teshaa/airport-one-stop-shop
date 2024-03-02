from django.contrib import admin
from .models import FoodItem, FoodOrder, OrderItem, Restaurant
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class FoodInline(admin.TabularInline):
    model = FoodItem


class OrderInline(admin.TabularInline):
    model = FoodOrder


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display=("restaurant", "name", "price","preparation_time", "readily_available","image")


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=("name", "logo", "location")
    inlines = [FoodInline, OrderInline]


@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display=(
        "user", "restaurant", "total_price",
          "order_time", "order_time", "status"
          )
    inlines = [
        OrderItemInline
    ]
    

@admin.register(OrderItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display=(
        "order", "food_item", "quantity",
          )
    

