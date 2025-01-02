from django.test import TestCase
from .models import Role

class RoleModelTest(TestCase):
    def setUp(self):
        Role.objects.create(name="Admin", description="Administrator role")

    def test_role_creation(self):
        role = Role.objects.get(name="Admin")
        self.assertEqual(role.description, "Administrator role")
