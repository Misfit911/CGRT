from django import forms
from .models import Guest, Accommodation, Booking, Payment

COMPANY_CHOICES = [
    ('Company A', 'Company A'),
    ('Company B', 'Company B'),
]

COUNTRY_CHOICES = [
    ('Kenya', 'Kenya'),
    ('USA', 'USA'),
]

AVAILABILITY_CHOICES = [
    ('Available', 'Available'),
    ('Not Available', 'Not Available'),
]

STATUS_CHOICES = [
    ('Confirmed', 'Confirmed'),
    ('Pending', 'Pending'),
]

PAYMENT_METHOD_CHOICES = [
    ('Credit Card', 'Credit Card'),
    ('Mobile Money', 'Mobile Money'),
]

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'company', 'country', 'email', 'phone_number']
        widgets = {
            'company': forms.Select(choices=COMPANY_CHOICES),
            'country': forms.Select(choices=COUNTRY_CHOICES),
        }

class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['type', 'description', 'capacity', 'price_per_night', 'discount', 'availability']
        widgets = {
            'availability': forms.Select(choices=AVAILABILITY_CHOICES),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in_date', 'check_out_date', 'total_price', 'status']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=STATUS_CHOICES),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_date', 'amount', 'payment_method']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
            'payment_method': forms.Select(choices=PAYMENT_METHOD_CHOICES),
        }