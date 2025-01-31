from django.db import models
from Customer_MNG.models import Customer
from Veterinarian_MNG.models import Veterinarian
from Pet_MNG.models import Pet
# Create your models here.
class MedicalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='medical_records', on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, related_name='medical_records', on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(Veterinarian, related_name='medical_records', on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    stay_required = models.BooleanField(default=False)
    rating = models.IntegerField(null=True, blank=True, choices=[(i, i) for i in range(1, 6)])  
    feedback = models.TextField(null=True, blank=True)  
    def __str__(self):
        return f"Hồ sơ khám {self.pet.name} - {self.date.strftime('%Y-%m-%d')}"