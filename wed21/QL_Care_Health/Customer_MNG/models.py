from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.address
