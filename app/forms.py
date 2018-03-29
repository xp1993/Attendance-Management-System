from django import forms
from .models import UserInfo
class loginForm(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=UserInfo
        field=('studentNum')
