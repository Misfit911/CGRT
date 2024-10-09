from django.contrib import admin
from .models import Guest, Accommodation, Booking, Payment

# Register your models here.
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'company', 'country')

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'capacity', 'price_per_night', 'discount', 'availability')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest', 'accommodation', 'check_in_date', 'check_out_date', 'total_price', 'status')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'payment_date', 'amount', 'payment_method')