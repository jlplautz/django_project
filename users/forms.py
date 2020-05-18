from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    This class is going to inherit from user creation form, because um want to
    add the fields additional -> email field
    """
    email = forms.EmailField()

    class Meta:
        """
        This class meta gives us a nested namespace for configurations and keeps
        the configuration in one place and within the configurations were are saying that
        the model that will be affected is the user model
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
