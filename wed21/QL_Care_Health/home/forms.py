from django import forms
from Pet_MNG.models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['customer_id', 'name', 'species', 'age', 'medical_history']