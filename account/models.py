from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField('Admin', default=False)
    profile_image = models.ImageField(
        default='dhttps://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__340.png',
        upload_to='portfolio/',
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # Create your models here.


class Profile(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    profile_image = models.ImageField(
        default='dhttps://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__340.png',
        upload_to='portfolio/',
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])]
    )
    date_created = models.DateTimeField(auto_now_add=True)
