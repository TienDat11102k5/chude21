from django.test import TestCase
from .models import TreatmentRecord

class TreatmentRecordModelTest(TestCase):
    def setUp(self):
        TreatmentRecord.objects.create(pet_id=1, veterinarian_id=1, diagnosis="Flu", prescriptions="Rest and fluids", notes="Follow up in one week")

    def test_treatment_record_creation(self):
        treatment_record = TreatmentRecord.objects.get(pet_id=1)
        self.assertEqual(treatment_record.diagnosis, "Flu")
