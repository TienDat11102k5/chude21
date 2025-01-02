from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.BooleanField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    role_id = models.IntegerField()

    def __str__(self):
        return self.fullname
