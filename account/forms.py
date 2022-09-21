from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User


class ProfileForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1',
                  'password2', 'profile_image', )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(ProfileForm, self).__init__(*args, **kwargs)

        for fieldname in ('username', 'email', 'password1', 'password2', 'profile_image', ):
            self.fields[fieldname].help_text = None


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'profile_image', )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(EditProfileForm, self).__init__(*args, **kwargs)

        for fieldname in ('first_name', 'last_name', 'username', 'email', 'profile_image', ):
            self.fields[fieldname].help_text = None
