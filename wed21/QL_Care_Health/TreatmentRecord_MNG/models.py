from django.db import models

class TreatmentRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    pet_id = models.IntegerField()
    veterinarian_id = models.IntegerField()
    diagnosis = models.TextField()
    prescriptions = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return f"Record {self.record_id} for Pet {self.pet_id}"
