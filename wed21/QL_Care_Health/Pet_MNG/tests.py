from django.test import TestCase
from .models import Pet

class PetModelTest(TestCase):
    def setUp(self):
        Pet.objects.create(name="Buddy", species="Dog", age=3, medical_history="Healthy", customer_id=1)

    def test_pet_creation(self):
        pet = Pet.objects.get(name="Buddy")
        self.assertEqual(pet.species, "Dog")
        self.assertEqual(pet.age, 3)
