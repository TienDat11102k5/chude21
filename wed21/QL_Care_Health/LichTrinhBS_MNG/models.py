from django.db import models
from Veterinarian_MNG.models import Veterinarian
# Create your models here.
class LichTrinhBS(models.Model):
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE, related_name='lich_trinh')
    date = models.DateField()
    start_time = models.TimeField()  
    end_time = models.TimeField()  
    note = models.TextField(blank=True, null=True)  
    def __str__(self):
        return f"{self.veterinarian.name} - {self.date} ({self.start_time} - {self.end_time})"
