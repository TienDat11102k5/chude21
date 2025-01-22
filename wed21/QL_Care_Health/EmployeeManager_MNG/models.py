from django.db import models
from Employee_MNG.models import Employee
from Veterinarian_MNG.models import Veterinarian
# Create your models here.
class EmployeeManager(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='manager')
    def assign_veterinarian(self, booking):
        if not booking.veterinarian:
            available_vet = Veterinarian.objects.first()  # Lấy bác sĩ đầu tiên (hoặc logic khác)
            booking.veterinarian = available_vet
            booking.status = 'Confirmed'
            booking.save()

    def cancel_booking_system(self, booking):
        booking.cancel_booking(cancelled_by_system=True)

    def __str__(self):
        return f"Manager {self.employee.name}"
