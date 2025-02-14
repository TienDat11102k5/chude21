from django.test import TestCase
from django.utils.timezone import now
from Pet_MNG.models import Pet
from Kennel_MNG.models import Kennel, KennelAssignment
from .models import HospitalizationRecord

class HospitalizationRecordTestCase(TestCase):
    def setUp(self):
        """Thiết lập dữ liệu mẫu"""
        self.pet = Pet.objects.create(
            name="Luna",
            species="Dog",
            breed="Husky",
            age=2
        )

        self.kennel = Kennel.objects.create(name="Chuồng 101")
        self.kennel_assignment = KennelAssignment.objects.create(
            pet=self.pet,
            kennel=self.kennel
        )

        self.hospitalization = HospitalizationRecord.objects.create(
            pet=self.pet,
            kennel_assignment=self.kennel_assignment,
            notes="Theo dõi sức khỏe"
        )

    def test_create_hospitalization_record(self):
        """Kiểm tra tạo hồ sơ nhập viện"""
        record = HospitalizationRecord.objects.get(id=self.hospitalization.id)
        self.assertEqual(record.pet.name, "Luna")
        self.assertEqual(record.kennel_assignment.kennel.name, "Chuồng 101")
        self.assertEqual(record.notes, "Theo dõi sức khỏe")
        self.assertIsNone(record.discharged_at)

    def test_str_method(self):
        """Kiểm tra phương thức __str__"""
        self.assertIn("Luna nhập viện vào", str(self.hospitalization))

    def test_discharge_pet(self):
        """Kiểm tra cập nhật ngày xuất viện"""
        self.hospitalization.discharged_at = now()
        self.hospitalization.save()
        updated_record = HospitalizationRecord.objects.get(id=self.hospitalization.id)
        self.assertIsNotNone(updated_record.discharged_at)
