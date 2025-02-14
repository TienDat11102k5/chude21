from django.test import TestCase
from Customer_MNG.models import Customer
from Veterinarian_MNG.models import Veterinarian
from Pet_MNG.models import Pet
from .models import MedicalRecord
from datetime import datetime

class MedicalRecordTest(TestCase):
    def setUp(self):
        """Thiết lập dữ liệu mẫu"""
        self.customer = Customer.objects.create(
            name="Trần Văn A",
            phone_number="0912345678",
            address="123 Đường ABC, TP.HCM",
            email="customerA@example.com"
        )

        self.vet = Veterinarian.objects.create(
            name="Dr. Lê Văn C",
            phone_number="0987654321",
            address="456 Đường XYZ, Hà Nội",
            email="drle@example.com",
            birthday="1980-05-20"
        )

        self.pet = Pet.objects.create(
            name="Milo",
            species="Dog",
            breed="Golden Retriever",
            age=3,
            owner=self.customer
        )

        self.record = MedicalRecord.objects.create(
            customer=self.customer,
            pet=self.pet,
            veterinarian=self.vet,
            diagnosis="Viêm da",
            treatment="Dùng thuốc kháng viêm",
            stay_required=True,
            rating=5,
            feedback="Bác sĩ tư vấn rất tận tình."
        )

    def test_create_medical_record(self):
        """Kiểm tra xem hồ sơ khám bệnh có được tạo đúng không"""
        record = MedicalRecord.objects.get(id=self.record.id)
        self.assertEqual(record.diagnosis, "Viêm da")
        self.assertEqual(record.treatment, "Dùng thuốc kháng viêm")
        self.assertEqual(record.stay_required, True)
        self.assertEqual(record.rating, 5)
        self.assertEqual(record.feedback, "Bác sĩ tư vấn rất tận tình.")

    def test_foreign_key_relationship(self):
        """Kiểm tra quan hệ giữa MedicalRecord với Customer, Pet, và Veterinarian"""
        self.assertEqual(self.customer.medical_records.count(), 1)
        self.assertEqual(self.pet.medical_records.count(), 1)
        self.assertEqual(self.vet.medical_records.count(), 1)

    def test_str_method(self):
        """Kiểm tra phương thức __str__"""
        expected_str = f"Hồ sơ khám Milo - {self.record.date.strftime('%Y-%m-%d')}"
        self.assertEqual(str(self.record), expected_str)
