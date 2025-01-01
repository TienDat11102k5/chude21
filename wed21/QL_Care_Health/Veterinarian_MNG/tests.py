from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Veterinarian

class VeterinarianModelTest(TestCase):
    def setUp(self):
        Veterinarian.objects.create(user_id=1, specialization="Specialization 1")

    def test_veterinarian_creation(self):
        veterinarian = Veterinarian.objects.get(user_id=1)
        self.assertEqual(veterinarian.specialization, "Specialization 1")
