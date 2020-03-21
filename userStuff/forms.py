from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter username',
                'id':"username",
            }))

    password = forms.CharField(widget = forms.PasswordInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'password'
            }))

    class Meta: 
        model = User
        fields = ['username','password']




class UserCreateForm(UserCreationForm):
    # overridding the default styles of UserCreationForm

    username = forms.CharField(widget = forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter username',
                'id':"username",
            }))

    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Password',
                'id': 'password1'
            }))

    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Re-enter Password',
                'id': 'password2'
            }))

    captha = forms.IntegerField(widget = forms.NumberInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Result',
            }))

    num1 = forms.IntegerField(widget = forms.NumberInput(attrs = {
        'id': 'num',
        'readonly': 'true',
        'class': 'star text-center'
    }))

    num2 = forms.IntegerField(widget = forms.NumberInput(attrs = {
        'id': 'num',
        'readonly': 'true',
        'class': 'star text-center'
    }))

    # custom validation for captha
    def clean(self):
        cleaned_data = super().clean()
        captha = cleaned_data.get('captha')
        num1 = cleaned_data.get('num1')
        num2 = cleaned_data.get('num2')
        print(captha, num1, num2)
        if(captha != num1 + num2):
            self.add_error('captha',"CAPTCHA FAILED")

    class Meta:
        model = User
        fields = ['username','password1','password2','captha']
