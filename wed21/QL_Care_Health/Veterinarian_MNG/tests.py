from django.test import TestCase
from .models import Veterinarian

class VeterinarianModelTest(TestCase):
    def setUp(self):
        """ Thiết lập dữ liệu mẫu """
        self.vet = Veterinarian.objects.create(
            name="Dr. Nguyễn Văn B",
            phone_number="0987654321",
            address="456 Đường XYZ, Hà Nội",
            email="drnguyenb@example.com",
            birthday="1985-06-15"
        )
        self.vet.set_password("securepassword")
        self.vet.save()

    def test_create_veterinarian(self):
        """ Kiểm tra xem bác sĩ thú y có được tạo đúng không """
        vet = Veterinarian.objects.get(name="Dr. Nguyễn Văn B")
        self.assertEqual(vet.phone_number, "0987654321")
        self.assertEqual(vet.email, "drnguyenb@example.com")

    def test_password_hashing(self):
        """ Kiểm tra mật khẩu có được hash không """
        vet = Veterinarian.objects.get(name="Dr. Nguyễn Văn B")
        self.assertNotEqual(vet.password, "securepassword")  # Không được lưu plaintext
        self.assertTrue(vet.check_password("securepassword"))  # Kiểm tra đúng mật khẩu

    def test_invalid_password(self):
        """ Kiểm tra mật khẩu sai """
        vet = Veterinarian.objects.get(name="Dr. Nguyễn Văn B")
        self.assertFalse(vet.check_password("wrongpassword"))  # Mật khẩu sai phải trả về False
