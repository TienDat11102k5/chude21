from django.test import TestCase
from .models import Guest

class GuestModelTest(TestCase):
    def setUp(self):
        Guest.objects.create(user_id=1, address="123 Main St", name="Jane Doe", email="jane@example.com")

    def test_guest_creation(self):
        guest = Guest.objects.get(user_id=1)
        self.assertEqual(guest.name, "Jane Doe")
        self.assertEqual(guest.email, "jane@example.com")
