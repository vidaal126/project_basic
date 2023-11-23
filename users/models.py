from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='media', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='custom_users')
