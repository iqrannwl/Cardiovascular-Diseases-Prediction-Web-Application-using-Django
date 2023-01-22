from attr import attr, fields
from django.contrib.auth.forms import AuthenticationForm ,UsernameField ,UserCreationForm
from django import forms
from matplotlib import widgets 
from .models import * 
from django.utils.translation import gettext , gettext_lazy as _
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))


class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email']

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }



class DoctorsForms(forms.ModelForm):
    class Meta:
        model=Doctors
        fields = "__all__"
        

class ArticlaForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"