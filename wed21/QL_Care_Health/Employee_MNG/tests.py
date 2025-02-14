from django.test import TestCase
from .models import Employee

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="Nguyễn Văn A",
            phone_number="0123456789",
            address="123 Đường ABC, TP.HCM",
            email="nguyenvana@example.com",
            birthday="1990-01-01"
        )
        self.employee.set_password("password123")
        self.employee.save()

    def test_create_employee(self):
        """ Kiểm tra xem nhân viên có được tạo đúng không """
        employee = Employee.objects.get(name="Nguyễn Văn A")
        self.assertEqual(employee.phone_number, "0123456789")
        self.assertEqual(employee.email, "nguyenvana@example.com")

    def test_password_hashing(self):
        """ Kiểm tra xem mật khẩu có được hash đúng không """
        employee = Employee.objects.get(name="Nguyễn Văn A")
        self.assertNotEqual(employee.password, "password123") 
        self.assertTrue(employee.check_password("password123"))  

    def test_invalid_password(self):
        """ Kiểm tra mật khẩu sai """
        employee = Employee.objects.get(name="Nguyễn Văn A")
        self.assertFalse(employee.check_password("wrongpassword")) 
