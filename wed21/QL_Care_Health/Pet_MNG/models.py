from django.db import models
from Customer_MNG.models import Customer
class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='pets', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    medical_history = models.TextField()
    def __str__(self):
        return self.name
