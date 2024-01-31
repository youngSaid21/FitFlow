from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    last_name = forms.CharField(max_length=100)
    first_name = forms.CharField(widget=forms.PasswordInput)
    email  = forms.EmailField(max_length = 64)
    phone = PhoneNumberField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)