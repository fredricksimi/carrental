from django.contrib import admin
from .models import Vehicle, Brands, Fueltype, VehicleImage, BookVehicle, Testimonial

class VehicleImageAdmin(admin.StackedInline):
    model = VehicleImage

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [VehicleImageAdmin]

    class Meta:
        model = Vehicle

@admin.register(VehicleImage)
class VehicleImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Brands)
admin.site.register(BookVehicle)
admin.site.register(Fueltype)
admin.site.register(Testimonial)

admin.site.site_header="Car Rental Portal"
admin.site.site_title="Car Rental Portal"