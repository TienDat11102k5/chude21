from django.test import TestCase
from Pet_MNG.models import Pet
from .models import Kennel, KennelAssignment

class KennelTestCase(TestCase):
    def setUp(self):
        """Thiết lập dữ liệu mẫu"""
        self.kennel1 = Kennel.objects.create(name="Chuồng 101")
        self.kennel2 = Kennel.objects.create(name="Chuồng 102", is_occupied=True)

        self.pet = Pet.objects.create(
            name="Luna",
            species="Dog",
            breed="Husky",
            age=2
        )

        self.assignment = KennelAssignment.objects.create(
            pet=self.pet,
            kennel=self.kennel1
        )

    def test_create_kennel(self):
        """Kiểm tra việc tạo chuồng"""
        kennel = Kennel.objects.get(name="Chuồng 101")
        self.assertEqual(kennel.is_occupied, False)

    def test_str_method_kennel(self):
        """Kiểm tra phương thức __str__ của Kennel"""
        self.assertEqual(str(self.kennel1), "Chuồng 101 - Trống")
        self.assertEqual(str(self.kennel2), "Chuồng 102 - Đầy")

    def test_create_kennel_assignment(self):
        """Kiểm tra việc tạo bản ghi phân công chuồng"""
        assignment = KennelAssignment.objects.get(id=self.assignment.id)
        self.assertEqual(assignment.pet.name, "Luna")
        self.assertEqual(assignment.kennel.name, "Chuồng 101")

    def test_str_method_kennel_assignment(self):
        """Kiểm tra phương thức __str__ của KennelAssignment"""
        self.assertEqual(str(self.assignment), "Luna -> Chuồng 101")
