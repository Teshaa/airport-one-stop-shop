from django.contrib import admin
from .models import FoodItem, FoodOrder, FoodType, Restaurant, RestaurantImage
# Register your models here.


class FoodInline(admin.TabularInline):
    model = FoodItem



class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display=("restaurant", "name", "price","preparation_time", "readily_available","image")


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=("name", "logo", "location")
    inlines = [RestaurantImageInline, FoodInline]


@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display=(
        "user", "price","food_item", "quantity",
          "order_time", "order_time", "status"
          )

    

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display=(
        "name", "description", "created_at","updated_at",
          )
    


