from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'text'}))
    password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'text'}))