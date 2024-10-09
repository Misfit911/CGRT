from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)  # Use CharField for phone number

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Accommodation(models.Model):
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for prices
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # Use DecimalField for discounts
    availability = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)  # Add on_delete behavior
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)  # Add on_delete behavior
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for price
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Booking for {self.guest} - {self.status}"


class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)  # Add on_delete behavior
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for amount
    payment_method = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment of {self.amount} for {self.booking}"
