from django import forms

class IdentityForm(forms.Form):
    your_name = forms.CharField(label='Your identity', max_length=300)
