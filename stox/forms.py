from django import forms

class PriceCheckForm(forms.Form):
    url = forms.URLField()
    size = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)