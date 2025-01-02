from django.test import TestCase
from .models import Service

class ServiceModelTest(TestCase):
    def setUp(self):
        Service.objects.create(name="Grooming", description="Full grooming service", price=50.0)

    def test_service_creation(self):
        service = Service.objects.get(name="Grooming")
        self.assertEqual(service.price, 50.0)
