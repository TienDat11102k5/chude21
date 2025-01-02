from django.db import models

class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    medical_history = models.TextField()
    customer_id = models.IntegerField()

    def __str__(self):
        return self.name
