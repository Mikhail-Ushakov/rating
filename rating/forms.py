from django import forms
from django.contrib.auth import get_user_model

from .models import Rate, Estimate

User = get_user_model()

class SimpleForm(forms.ModelForm):
    
    class Meta:
        model = Estimate
        fields = ['name', 'text']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['rating']