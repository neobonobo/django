from django import forms

class TextInputForm(forms.Form):
    user_text = forms.CharField(
        label='Enter your text', 
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        max_length=500
    )
class QuizForm(forms.Form):
    question = forms.CharField(max_length=255)
    options = forms.ChoiceField(choices=[])
