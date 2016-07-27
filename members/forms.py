from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    usertype = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['username','email','password','usertype']
