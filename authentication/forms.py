from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation


class SignUpUserCreationForm(UserCreationForm):
    
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        error_messages= {'required': 'Enter Your Password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control", "placeholder":"Password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Confirm Password(again)"),
        error_messages= {'required': 'Enter Your Confirm Password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class":"form-control", "placeholder":"Re-Enter Password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        # Ordering field name
        fields = ['username', 'first_name', 'last_name', 'email']
        
        
        # labels
        labels = {
            'email': 'Email',
        }
        
        # error messages
        error_messages = {
            'username': {'required':"Enter Your Password"},
        }
        
        # Form widget
        widgets = {
            'username': forms.TextInput(attrs={"class":"form-control", "placeholder":"Username"}),
            'first_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}),
            'last_name': forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}),
            'email': forms.EmailInput(attrs={"class":"form-control", "placeholder":"@gmail.com"}),
        }