from django.db import models

# Create your models here.
class Veterinarian(models.Model):
    usesID = models.CharFiled(max_length=100)
    employeeID = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
def _str_ (self):
    return self.userID