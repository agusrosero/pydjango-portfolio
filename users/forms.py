from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Login form
class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)

# Register form
class SignUpForm(UserCreationForm):

    class Meta:
        
        model = User
        fields = ('username', 'password1', 'password2',)
