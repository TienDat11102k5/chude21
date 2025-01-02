from django.db import models

class Veterinarian(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return f"Veterinarian {self.employee_id}: Specialization - {self.specialization}"
