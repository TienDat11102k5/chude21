from django.test import TestCase
from .models import Pet

class PetModelTestCase(TestCase):
    def setUp(self):
        # Tạo dữ liệu mẫu để sử dụng trong các bài kiểm tra
        Pet.objects.create(
            customer_id=1,
            name="Luna",
            species="Dog",
            age=3,
            medical_history="Vaccinated for rabies"
        )
        Pet.objects.create(
            customer_id=2,
            name="Milo",
            species="Cat",
            age=2,
            medical_history="No known issues"
        )

    def test_pet_creation(self):
        # Kiểm tra xem các đối tượng đã được tạo hay chưa
        pet1 = Pet.objects.get(name="Luna")
        pet2 = Pet.objects.get(name="Milo")
        
        self.assertEqual(pet1.customer_id, 1)
        self.assertEqual(pet1.species, "Dog")
        self.assertEqual(pet1.age, 3)
        self.assertEqual(pet1.medical_history, "Vaccinated for rabies")
        
        self.assertEqual(pet2.customer_id, 2)
        self.assertEqual(pet2.species, "Cat")
        self.assertEqual(pet2.age, 2)
        self.assertEqual(pet2.medical_history, "No known issues")

    def test_pet_str_method(self):
        # Kiểm tra phương thức __str__()
        pet1 = Pet.objects.get(name="Luna")
        pet2 = Pet.objects.get(name="Milo")
        
        self.assertEqual(str(pet1), "Luna")
        self.assertEqual(str(pet2), "Milo")
