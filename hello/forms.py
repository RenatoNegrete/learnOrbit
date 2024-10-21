from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')