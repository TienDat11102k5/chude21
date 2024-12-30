from django.db import models

# Create your models here.
class Employee(models.Model):
   employeeID = models.CharField(max_lenghth=50)
   usesID = models.CharField(max_length=50)
def _str_ (self):
    return self.employeeID