from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Stock(models.Model):
    stock = models.CharField(max_length=10)
    price = models.CharField(max_length=10, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.stock
