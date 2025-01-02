from django.test import TestCase
from .models import Veterinarian

class VeterinarianModelTest(TestCase):
    def setUp(self):
        Veterinarian.objects.create(user_id=1, specialization="Exotic Animals")

    def test_veterinarian_creation(self):
        veterinarian = Veterinarian.objects.get(user_id=1)
        self.assertEqual(veterinarian.specialization, "Exotic Animals")
