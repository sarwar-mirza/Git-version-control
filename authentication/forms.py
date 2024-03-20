from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
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


# Login 
class LoginAuthenticationForm(AuthenticationForm):
    username = UsernameField(error_messages= {'required':'Enter Your Username'},widget=forms.TextInput(attrs={"autofocus": True,"class":"form-control", "placeholder":"Username"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        error_messages= {'required':'Enter Your Password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","class":"form-control", "placeholder":"Password"}),
    )


# Change password
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        error_messages= {'required':'Enter Your Old Password'},
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True,"class":"form-control", "placeholder":"Old Password"}
        ),
    )
    
    new_password1 = forms.CharField(
        label=_("New password"),
        error_messages= {'required':'Enter Your New Password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control", "placeholder":"New Password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Confirm Password(again)"),
        strip=False,
        error_messages= {'required':'Enter Your Re-Enter Password'},
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control", "placeholder":"Re-Enter Password"}),
    )

