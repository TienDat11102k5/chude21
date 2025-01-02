from django.db import models

class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else f"Guest {self.guest_id}"
