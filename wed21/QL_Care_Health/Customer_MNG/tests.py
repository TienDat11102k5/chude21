from django.test import TestCase
from .models import Customer

class CustomerModelTest(TestCase):
    def setUp(self):
        Customer.objects.create(user_id=1, address="123 Main St")

    def test_customer_creation(self):
        customer = Customer.objects.get(user_id=1)
        self.assertEqual(customer.address, "123 Main St")
