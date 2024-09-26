# pages/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    # You can add any custom fields or styles here if needed
    pass
