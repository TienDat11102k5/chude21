from django import forms
from Pet_MNG.models import Pet
from Customer_MNG.models import Customer
from Employee_MNG.models import Employee
from Veterinarian_MNG.models import Veterinarian
from LichTrinhBS_MNG.models import LichTrinhBS
from Booking_MNG.models import Booking
from MedicalRecord_MNG.models import MedicalRecord
from Kennel_MNG.models import KennelAssignment, Kennel
from HospitalizationRecord_MNG.models import HospitalizationRecord
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['customer','name', 'species', 'age', 'medical_history']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'address', 'email', 'birthday', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'phone_number', 'address', 'email', 'birthday', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class VeterinarianForm(forms.ModelForm):
    class Meta:
        model = Veterinarian
        fields = ['name', 'phone_number', 'address', 'email', 'birthday', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LichTrinhBSForm(forms.ModelForm):
    class Meta:
        model = LichTrinhBS
        fields = ['date', 'start_time', 'end_time', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

class BookingForm(forms.ModelForm):
    veterinarian = forms.ModelChoiceField(queryset=Veterinarian.objects.all(), required=False, empty_label="Chọn bác sĩ")
    class Meta:
        model = Booking
        fields = ['customer', 'pet', 'veterinarian', 'appointment_date', 'fee']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class BookingManagementForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=Booking.STATUS_CHOICES)
        }

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['customer', 'pet', 'veterinarian', 'diagnosis', 'treatment', 'stay_required']


class MedicalRecordRatingForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['rating', 'feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Nhập ý kiến của bạn'}),
        }

class KennelForm(forms.ModelForm):
    class Meta:
        model = Kennel
        fields = ['name', 'is_occupied']
        labels = {
            'name': 'Tên chuồng',
            'is_occupied': 'Trạng thái'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_occupied': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class AssignKennelForm(forms.ModelForm):
    kennel = forms.ModelChoiceField(
        queryset=Kennel.objects.filter(is_occupied=False),  
        empty_label="Chọn chuồng",
        label="Chọn chuồng"
    )
    class Meta:
        model = KennelAssignment
        fields = ['pet', 'kennel']


class ScheduleAdmissionForm(forms.ModelForm):
    class Meta:
        model = KennelAssignment
        fields = ['pet', 'kennel']

class CareAdmissionForm(forms.ModelForm):
    class Meta:
        model = HospitalizationRecord
        fields = ['notes']