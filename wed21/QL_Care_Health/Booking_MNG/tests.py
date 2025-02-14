from django.test import TestCase
from django.utils.timezone import now, timedelta
from Customer_MNG.models import Customer
from Veterinarian_MNG.models import Veterinarian
from Pet_MNG.models import Pet
from Booking_MNG.models import Booking

class BookingTestCase(TestCase):
    def setUp(self):
        """Thiết lập dữ liệu mẫu"""
        self.customer = Customer.objects.create(name="Nguyễn Văn A")
        self.pet = Pet.objects.create(name="Milo", species="Dog", breed="Golden", age=3)
        self.veterinarian = Veterinarian.objects.create(name="Bác sĩ B")

        self.booking = Booking.objects.create(
            customer=self.customer,
            pet=self.pet,
            veterinarian=self.veterinarian,
            appointment_date=now() + timedelta(days=5),  # Lịch hẹn trong 5 ngày tới
            fee=200.00,
            paid=True
        )

    def test_create_booking(self):
        """Kiểm tra tạo Booking"""
        booking = Booking.objects.get(id=self.booking.id)
        self.assertEqual(booking.customer.name, "Nguyễn Văn A")
        self.assertEqual(booking.pet.name, "Milo")
        self.assertEqual(booking.veterinarian.name, "Bác sĩ B")
        self.assertEqual(booking.status, "Pending")
        self.assertTrue(booking.paid)

    def test_cancel_booking_by_customer(self):
        """Kiểm tra khách hàng hủy booking"""
        self.booking.cancel_booking()
        self.assertEqual(self.booking.status, "Cancelled")

    def test_cancel_booking_by_system(self):
        """Kiểm tra hệ thống hủy booking"""
        self.booking.cancel_booking(cancelled_by_system=True)
        self.assertEqual(self.booking.status, "Cancelled")

    def test_cancel_booking_no_refund(self):
        """Kiểm tra hủy booking mà không được hoàn tiền"""
        self.booking.appointment_date = now() + timedelta(days=1)
        self.booking.cancel_booking()
        self.assertEqual(self.booking.status, "Cancelled")

    def test_str_method(self):
        """Kiểm tra phương thức __str__"""
        self.assertIn("Booking ID", str(self.booking))
