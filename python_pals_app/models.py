from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email_address = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    follows = models.ManyToManyField('Profile', related_name='followers')
