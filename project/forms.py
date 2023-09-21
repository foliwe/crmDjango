from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Record


# Create User

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form_control", "placeholder": "username", "id": "username", "required": True})
        self.fields["email"].widget.attrs.update(
            {"class": "form_control", "placeholder": "email", "id": "email", "required": True})
        self.fields["password1"].widget.attrs.update(
            {"class": "form_control", "placeholder": "*******", "id": "password1", "required": True})
        self.fields["password2"].widget.attrs.update(
            {"class": "form_control", "placeholder": "*******", "id": "password2", "required": True})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Login User


class LogInForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={"class": "form_control"}))
    password = forms.CharField(
        widget=PasswordInput(attrs={"class": "form_control"}))


class CreateRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form_control", "placeholder": "First Name", "id": "first_name", "required": True})

        self.fields["last_name"].widget.attrs.update(
            {"class": "form_control", "placeholder": "Last Name", "id": "last_name", "required": True})

        self.fields["email"].widget.attrs.update(
            {"class": "form_control", "placeholder": "email", "id": "email", "required": True})

        self.fields["address"].widget.attrs.update(
            {"class": "form_control", "placeholder": "your address", "id": "address", "required": True})

        self.fields["phone"].widget.attrs.update(
            {"class": "form_control", "placeholder": "mobile number", "id": "phone"})

        self.fields["city"].widget.attrs.update(
            {"class": "form_control", "placeholder": "city", "id": "city", })

        self.fields["country"].widget.attrs.update(
            {"class": "form_control", "placeholder": "country", "id": "country", "required": True})

        self.fields["province"].widget.attrs.update(
            {"class": "form_control", "id": "provinve", "placeholder": "province"})

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email',
                  'address', 'phone', 'city', 'country', 'province']


class UpdateRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {"class": "form_control", "placeholder": "First Name", "id": "first_name", "required": True})

        self.fields["last_name"].widget.attrs.update(
            {"class": "form_control", "placeholder": "Last Name", "id": "last_name", "required": True})

        self.fields["email"].widget.attrs.update(
            {"class": "form_control", "placeholder": "email", "id": "email", "required": True})

        self.fields["address"].widget.attrs.update(
            {"class": "form_control", "placeholder": "your address", "id": "address", "required": True})

        self.fields["phone"].widget.attrs.update(
            {"class": "form_control", "placeholder": "mobile number", "id": "phone"})

        self.fields["city"].widget.attrs.update(
            {"class": "form_control", "placeholder": "city", "id": "city", })

        self.fields["country"].widget.attrs.update(
            {"class": "form_control", "placeholder": "country", "id": "country", "required": True})

        self.fields["province"].widget.attrs.update(
            {"class": "form_control", "id": "provinve", "placeholder": "province"})

    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email',
                  'address', 'phone', 'city', 'country', 'province']
