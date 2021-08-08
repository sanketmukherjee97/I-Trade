from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    session_token = models.CharField(max_length=10, default=0)
