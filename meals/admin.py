from django.contrib import admin
from .models import FoodItem, FoodOrder, FoodType, OrderItem, Restaurant, RestaurantImage
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class FoodInline(admin.TabularInline):
    model = FoodItem


class OrderInline(admin.TabularInline):
    model = FoodOrder


class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display=("restaurant", "name", "price","preparation_time", "readily_available","image")


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=("name", "logo", "location")
    inlines = [RestaurantImageInline, FoodInline, OrderInline]


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
class OrderItemAdmin(admin.ModelAdmin):
    list_display=(
        "order", "food_item", "quantity",
          )
    

@admin.register(FoodType)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=(
        "name", "description", "created_at","updated_at",
          )
    


