from django import forms
from accounts.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'fname',
            'lname',
            'email',
            'phone',
            'sex',
            'birthday',
            'client_type'
        ]
        widgets = {
            'fname': forms.TextInput(
                attrs={'class': 'form-input', 'placeholder': 'First Name'}
                ),
            'lname': forms.TextInput(
                attrs={'class': 'form-input', 'placeholder': 'Last Name'}
                ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'email@example.com'
                    }
                ),
            'phone': forms.TextInput(
                attrs={'class': 'form-input', 'placeholder': '+380 ...'}
                ),
            'sex': forms.Select(
                attrs={'class': 'form-input'}
                ),
            'birthday': forms.DateInput(
                attrs={'class': 'form-input', 'type': 'date'}
                ),
            'client_type': forms.Select(
                attrs={'class': 'form-input'}
                ),
        }
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'email': 'Email',
            'phone': 'Phone',
            'sex': 'Sex',
            'birthday': 'Birthday',
            'client_type': 'Client Type',
        }


class LoginForm(forms.Form):
    phone = forms.CharField(
        max_length=150,
        label='Phone number'
        )
    password = forms.CharField(
        max_length=150,
        label='Password'
    )
    remember = forms.BooleanField(
        required=False,
        label='Remember me'
    )


class RegisterForm(forms.Form):
    phone = forms.CharField(
        max_length=30,
        label='Phone number'
    )
    fname = forms.CharField(
        max_length=50,
        label='First name',
    )
    lname = forms.CharField(
        max_length=50,
        label='Last name'
    )
    password1 = forms.CharField(
        max_length=100,
        label='Password',
    )
    password2 = forms.CharField(
        max_length=100,
        label='Repeat Password',
    )


class NewPasswordForm(forms.Form):
    phone = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Phone number'})
    )
    password1 = forms.CharField(
        max_length=100,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'New password'})
    )
    password2 = forms.CharField(
        max_length=100,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'})
    )
