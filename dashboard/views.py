from django.shortcuts import render, redirect

from dashboard.models import Guest, Accommodation, Booking, Payment
from .forms import GuestForm, AccommodationForm, BookingForm, PaymentForm


def index(request):
    return render(request, 'index.html')

def ewc(request):
    return render('EWC', request)

def multi_form_view(request):
    guest_form = GuestForm(request.POST or None)
    accommodation_form = AccommodationForm(request.POST or None)
    booking_form = BookingForm(request.POST or None)
    payment_form = PaymentForm(request.POST or None)
    
    if request.method == 'POST':
        if guest_form.is_valid() and accommodation_form.is_valid() and booking_form.is_valid() and payment_form.is_valid():
            guest = guest_form.save()
            accommodation = accommodation_form.save()
            booking = booking_form.save(commit=False)
            booking.guest = guest  # Link guest to booking
            booking.accommodation = accommodation  # Link accommodation to booking
            booking.save()
            payment = payment_form.save(commit=False)
            payment.booking = booking  # Link booking to payment
            payment.save()

            # Once data is saved, fetch all entries to display in the table
            all_guests = Guest.objects.all()
            all_accommodations = Accommodation.objects.all()
            all_bookings = Booking.objects.all()
            all_payments = Payment.objects.all()

            return render(request, 'multi_form.html', {
                'guest_form': guest_form,
                'accommodation_form': accommodation_form,
                'booking_form': booking_form,
                'payment_form': payment_form,
                'guests': all_guests,
                'accommodations': all_accommodations,
                'bookings': all_bookings,
                'payments': all_payments
            })

    return render(request, 'multi_form.html', {
        'guest_form': guest_form,
        'accommodation_form': accommodation_form,
        'booking_form': booking_form,
        'payment_form': payment_form
    })
