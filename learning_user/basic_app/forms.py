from django.contrib.auth.models import User
from basic_app.models import UserProfie
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfieInfo(forms.ModelForm):

    class Meta():
        model = UserProfie
        fields = {'protfolio_site','profile_picture'}
