__author__ = 'achachar'
from django import forms
from .models import Addresses

class ContactForm(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = ['name', 'email', 'phone', 'address', 'city', 'state', 'country', 'image']
