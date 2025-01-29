from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from Customer_MNG.models import Customer
from Veterinarian_MNG.models import Veterinarian
from Pet_MNG.models import Pet
class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    customer = models.ForeignKey(Customer, related_name='bookings', on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, related_name='bookings', on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, related_name='bookings', on_delete=models.SET_NULL, blank=True, null=True)
    booking_date = models.DateTimeField(default=now)
    appointment_date = models.DateTimeField()
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    paid = models.BooleanField(default=False)
def cancel_booking(self, cancelled_by_system=False, cancelled_by_employee=False):
    """
    Xử lý hủy booking:
    - Trường hợp hệ thống hoặc nhân viên hủy: hoàn tiền nếu đã thanh toán.
    - Trường hợp khách hủy: hoàn tiền theo thời gian hủy.
    """
    if cancelled_by_system or cancelled_by_employee:
        # Nếu hệ thống hoặc nhân viên hủy
        self.status = 'Cancelled'
        if self.paid:
            self.refund_fee(self.fee)
    else:
        # Nếu khách hàng hủy
        days_to_appointment = (self.appointment_date - now()).days
        if days_to_appointment >= 7:
            refund_amount = self.fee
        elif 3 <= days_to_appointment <= 6:
            refund_amount = self.fee * 0.75
        else:
            refund_amount = 0
        self.status = 'Cancelled'
        if refund_amount > 0 and self.paid:
            self.refund_fee(refund_amount)

    self.save()
def refund_fee(self, amount):
        print(f"Refunding {amount} for booking ID {self.id}")

def __str__(self):
        return f"Booking ID {self.id} - {self.customer.name} - {self.pet.name} - {self.status}"
