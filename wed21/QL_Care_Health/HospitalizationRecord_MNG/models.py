from django.db import models
from Pet_MNG.models import Pet
from Kennel_MNG.models import KennelAssignment
# Create your models here.
class HospitalizationRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    kennel_assignment = models.OneToOneField(KennelAssignment, on_delete=models.CASCADE)
    admitted_at = models.DateTimeField(auto_now_add=True)
    discharged_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pet.name} nhập viện vào {self.admitted_at}" 