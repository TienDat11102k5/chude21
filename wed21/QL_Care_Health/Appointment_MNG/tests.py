from django.test import TestCase
from .models import Appointment

class AppointmentModelTest(TestCase):
    def setUp(self):
        Appointment.objects.create(customer_id=1, pet_id=1, veterinarian_id=1, date="2024-12-31", time="10:00:00", status="Scheduled", notes="Checkup")

    def test_appointment_creation(self):
        appointment = Appointment.objects.get(customer_id=1)
        self.assertEqual(appointment.status, "Scheduled")
