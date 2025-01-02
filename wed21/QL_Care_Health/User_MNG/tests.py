from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(fullname="John Doe", birthdate="1990-01-01", gender=True, phone="123456789", email="john@example.com", role_id=1)

    def test_user_creation(self):
        user = User.objects.get(fullname="John Doe")
        self.assertEqual(user.email, "john@example.com")
