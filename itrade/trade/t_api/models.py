from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField

User = get_user_model()


class AddApi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=200)
    secret_key = models.CharField(max_length=200)

    def __str__(self):
        return self.user
