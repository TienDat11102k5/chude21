from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    customer_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.address}"
=======
=======
>>>>>>> Stashed changes
    customerID = models.CharField(max_length=50)
    usesID = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    def _str_ (self):
<<<<<<< Updated upstream
        return self.customerID
>>>>>>> Stashed changes
=======
        return self.customerID
>>>>>>> Stashed changes
