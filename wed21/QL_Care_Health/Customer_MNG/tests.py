from django.test import TestCase
from .models import Customer

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name="Nguyen Van A",
            phone_number="0123456789",
            address="123 ABC Street",
            email="nguyenvana@example.com",
            birthday="1990-01-01",
        )
        self.customer.set_password("securepassword")
        self.customer.save()

    def test_create_customer(self):
        self.assertEqual(self.customer.name, "Nguyen Van A")
        self.assertEqual(self.customer.phone_number, "0123456789")
        self.assertEqual(self.customer.address, "123 ABC Street")
        self.assertEqual(self.customer.email, "nguyenvana@example.com")
        self.assertEqual(str(self.customer), "Nguyen Van A")

    def test_password_hashing(self):
        self.assertNotEqual(self.customer.password, "securepassword")  # Mật khẩu không lưu dạng plaintext
        self.assertTrue(self.customer.check_password("securepassword"))  # Kiểm tra hash
        self.assertFalse(self.customer.check_password("wrongpassword"))  # Mật khẩu sai

    def test_update_customer(self):
        self.customer.name = "Le Van B"
        self.customer.save()
        updated_customer = Customer.objects.get(customer_id=self.customer.customer_id)
        self.assertEqual(updated_customer.name, "Le Van B")

    def test_delete_customer(self):
        customer_id = self.customer.customer_id
        self.customer.delete()
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(customer_id=customer_id)
