from django.db import models
from phonenumber_field import modelfields
from taggit.managers import TaggableManager


# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="hotels/logos")
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phoneNumber = modelfields.PhoneNumberField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=3)
    amenities = TaggableManager(verbose_name="Amenities")
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.name


class HotelImage(models.Model):
    image = models.ImageField(upload_to="upload/hotels")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="images")


class RoomType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-updated_at"]


    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.CharField(max_length=50)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="rooms")
    capacity = models.PositiveIntegerField(default=3, help_text="number of guests it can accommodate")
    price_per_night = models.DecimalField(decimal_places=2, max_digits=12)
    feature = TaggableManager(verbose_name="Features")
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hotel} {self.number}"
    
    class Meta:
        ordering = ["-updated_at"]


class RoomImage(models.Model):
    image = models.ImageField(upload_to="upload/room")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="images")


class Reservation(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="reservations")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reservations")
    price_per_night = models.DecimalField(decimal_places=2, max_digits=12)
    checkin_date = models.DateField()
    nights = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=255, choices=(
        ("confirmed", "Confirmed"),
        ("cancelled", "Canceled"),
        ("checked-in", "Checked In"),
        ("checked-out", "Checked Out"),
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-updated_at"]
