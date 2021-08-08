from django.db import models
from django.db.models.fields import CharField
from trade.stock.models import Stock
from django.contrib.auth import get_user_model

User = get_user_model()


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.CharField(max_length=10)
    b_p = models.CharField(max_length=10)
    s_p = models.CharField(max_length=10)
    bquantity = models.CharField(max_length=10)
    squantity = models.CharField(max_length=10)
    # o_type = models.CharField(max_length=10)
    btime = models.CharField(max_length=10)
    stime = models.CharField(max_length=10)
    ordered_at = models.DateTimeField(auto_now_add=True)
    # state = models.CharField(max_length=10)

    def __str__(self):
        return self.stock+" "+str(self.ordered_at)
