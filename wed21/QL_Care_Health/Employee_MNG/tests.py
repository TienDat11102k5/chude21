from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Employee

class EmployeeModelTest(TestCase):
    def setUp(self):
        Employee.objects.create(user_id=1, specialization="Specialization 1")

    def test_employee_creation(self):
        employee = Employee.objects.get(user_id=1)
        self.assertEqual(employee.specialization, "Specialization 1")
