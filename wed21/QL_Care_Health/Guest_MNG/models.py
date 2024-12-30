from django.db import models

# Create your models here.
class Guest(models.Model):
  name = models.CharField(max_length=100)
  usesID = models.CharField(max_length=50)
  birthday = models.CharFiedl(max_length=50)
  phone = models.CharField(max_length=50)
  gender = models.CharField(boolean)
  email = models.EmailField(max_length=100)
  roleID = models.CharField(max_length=100)
def _str_ (self):
 return self.name
