from django import forms
from .models import UserInfo, Address
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class SignupForm(UserCreationForm):
    class Meta:
        model = UserInfo
        fields = ["username", "first_name", "last_name", "firstname2", "lastname2", "email", "sex", "age"]

class LoginForm(AuthenticationForm):
    pass


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("zip_code", "address1", "address2")