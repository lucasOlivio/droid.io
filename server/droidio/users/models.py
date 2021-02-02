from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token


class User(AbstractUser):
    def type_user(self):
        return "Administrador" if self.is_superuser else "Anunciante"

    def __str__(self):
        return self.username
