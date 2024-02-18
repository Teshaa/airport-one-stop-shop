from django.contrib import admin

from hotels.models import Hotel, RoomType, Room, Reservation


# Register your models here.


class RoomTabularInline(admin.TabularInline):
    model = Room


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "address", "email", "phoneNumber", "rating", "amenities", "description", "created_at",
        "updated_at")
    inlines = [RoomTabularInline]


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "description", "created_at", "updated_at")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        "id", "user", "room", "checkin_date", "checkout_date", "status", "created_at", "updated_at"]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [
        "id", "number", "description", "type", "capacity", "price_per_night", "available", "feature",
        "created_at", "updated_at"]