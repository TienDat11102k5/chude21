from django.db import models

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name
