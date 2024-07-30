# from django import forms
# from .models import Contact

# class AdmissionForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['full_name', 'date_of_birth', 'gender', 'nationality', 'home_address']

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'full_name', 'date_of_birth', 'gender', 'nationality', 'home_address',
            'phone_number', 'email_address', 'education_level', 'other_education',
            'work_experience', 'work_experience_details', 'medical_conditions',
            'medical_conditions_details', 'training_program', 'emergency_contact_name',
            'emergency_contact_phone'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'work_experience_details': forms.Textarea(attrs={'rows': 3}),
            'medical_conditions_details': forms.Textarea(attrs={'rows': 3}),
        }
