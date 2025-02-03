from django.db import models
from Pet_MNG.models import Pet

class Kennel(models.Model):
    kennel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True) 
    is_occupied = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.name} - {'Đầy' if self.is_occupied else 'Trống'}"

class KennelAssignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    pet = models.ForeignKey(Pet, null=True, blank=True, on_delete=models.SET_NULL) 
    kennel = models.ForeignKey(Kennel, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return f"{self.pet.name} -> {self.kennel.name}"
