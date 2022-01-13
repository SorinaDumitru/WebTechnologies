from django import forms
from .models import Patient_medical_data


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class UserAddDataForm(forms.ModelForm):
    class Meta:
        model = Patient_medical_data
        fields = ['date', 'value']

