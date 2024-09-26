# daytrack/forms.py
from django import forms
from .models import Day

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['activities']
        widgets = {
#            'description': forms.TextInput(attrs={'placeholder': 'How was your day?'}),
#           'mood': forms.TextInput(attrs={'placeholder': 'Your mood'}),
            'activities': forms.Textarea(attrs={'placeholder': 'Activities done during the day...'}),
        }
