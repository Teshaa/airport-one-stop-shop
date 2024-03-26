from django.contrib import admin

from hotels.models import Hotel, HotelImage, RoomImage, RoomType, Room, Reservation


# Register your models here.


class RoomTabularInline(admin.TabularInline):
    model = Room

class HotelImageTabularInline(admin.TabularInline):
    model = HotelImage

class RoomImageTabularInline(admin.TabularInline):
    model = RoomImage


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "address", "email",
          "phoneNumber", "rating", "description",
            "created_at", "updated_at"
            )
    # fieldsets = ((None, {'fields': ('amenities',)}),)
    inlines = [
        HotelImageTabularInline,
        # RoomTabularInline
    ]


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
        "id", "number", "description", "type", "capacity",
          "price_per_night", "available",  "created_at", "updated_at"
          ]
    # fieldsets = ((None, {'fields': ('feature',)}),)
    inlines= [
        RoomImageTabularInline
    ]
