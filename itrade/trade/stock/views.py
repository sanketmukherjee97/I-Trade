from trade.dashboard.views import dashboard
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Stock

UserModel = get_user_model()


def stock(request, id):
    user = UserModel.objects.get(id=id)
    if request.method == 'POST':
        symbol = request.POST['stocks']
        if Stock.objects.filter(stock=symbol).exists():
            stock = Stock.objects.filter(user_id=id).values()
            context = {
                'stock': stock
            }
            return render(request, 'dash.html', context)
        else:
            add = Stock(stock=symbol, user_id=user.id)
            add.save()
            stock = Stock.objects.filter(user_id=id).values()
            context = {
                'stock': stock
            }
            return render(request, 'dash.html', context)
    else:
        stock = Stock.objects.filter(user_id=id).values()
        context = {
            'stock': stock
        }
        return render(request, 'dash.html', context)
