from django import forms
from Pet_MNG.models import Pet
from Customer_MNG.models import Customer
from Employee_MNG.models import Employee
from Veterinarian_MNG.models import Veterinarian
from LichTrinhBS_MNG.models import LichTrinhBS

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
