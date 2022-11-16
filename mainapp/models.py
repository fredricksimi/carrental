from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'User Data'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.user}"

class Brands(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name

class Fueltype(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_title = models.CharField(max_length=100)
    vehicle_brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    vehicle_overview = models.TextField()
    price_per_day = models.IntegerField()
    fuel_type = models.ForeignKey(Fueltype, on_delete=models.CASCADE)
    model_year = models.CharField(max_length=4)
    seating_capacity = models.IntegerField()
    image = models.ImageField(upload_to='media_pics/', blank=True, default='default-banner.jpg')
    air_conditioner = models.BooleanField(default=False)
    power_door_locks = models.BooleanField(default=False)
    antilock_braking_system = models.BooleanField(default=False)
    brake_assist = models.BooleanField(default=False)
    power_steering = models.BooleanField(default=False)
    driver_airbag = models.BooleanField(default=False)
    passenger_airbag = models.BooleanField(default=False)
    power_windows = models.BooleanField(default=False)
    cd_player = models.BooleanField(default=False)
    central_locking = models.BooleanField(default=False)
    crash_sensor = models.BooleanField(default=False)
    leather_seats = models.BooleanField(default=False)
    registration_date = models.DateTimeField()
    updation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle_title} {self.model_year}"

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media_pics/', blank=True, default='default-banner.jpg')

    def __str__(self):
        return self.vehicle.vehicle_title

class BookVehicle(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Booked Vehicles"

    def __str__(self):
        return f"{self.vehicle.vehicle_title} booked by {self.customer.username}"

class Testimonial(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_sent = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial - {self.customer.username} sent on {self.date_sent}"