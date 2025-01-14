from django import forms
from Pet_MNG.models import Pet
from Customer_MNG.models import Customer
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['customer','name', 'species', 'age', 'medical_history']
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number', 'address']