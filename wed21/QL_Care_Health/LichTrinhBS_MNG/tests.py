from django.test import TestCase
from Veterinarian_MNG.models import Veterinarian
from .models import LichTrinhBS
from datetime import date, time

class LichTrinhBSTest(TestCase):
    def setUp(self):
        """Thiết lập dữ liệu mẫu"""
        self.vet = Veterinarian.objects.create(
            name="Dr. Nguyễn Văn B",
            phone_number="0987654321",
            address="456 Đường XYZ, Hà Nội",
            email="drnguyenb@example.com",
            birthday="1985-06-15"
        )

        self.lich_trinh = LichTrinhBS.objects.create(
            veterinarian=self.vet,
            date=date(2024, 2, 15),
            start_time=time(9, 0),
            end_time=time(12, 0),
            note="Khám định kỳ tại phòng khám"
        )

    def test_create_lich_trinh(self):
        """Kiểm tra xem lịch trình có được tạo đúng không"""
        lich = LichTrinhBS.objects.get(veterinarian=self.vet, date=date(2024, 2, 15))
        self.assertEqual(lich.start_time, time(9, 0))
        self.assertEqual(lich.end_time, time(12, 0))
        self.assertEqual(lich.note, "Khám định kỳ tại phòng khám")

    def test_foreign_key_relationship(self):
        """Kiểm tra quan hệ giữa Veterinarian và LichTrinhBS"""
        self.assertEqual(self.vet.lich_trinh.count(), 1)  # Bác sĩ có đúng 1 lịch trình
        self.assertEqual(self.vet.lich_trinh.first().date, date(2024, 2, 15))

    def test_str_method(self):
        """Kiểm tra phương thức __str__"""
        expected_str = "Dr. Nguyễn Văn B - 2024-02-15 (09:00:00 - 12:00:00)"
        self.assertEqual(str(self.lich_trinh), expected_str)
