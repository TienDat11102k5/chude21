from django.db import models

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    pet_id = models.IntegerField()
    veterinarian_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return f"Appointment {self.appointment_id} on {self.date}"
