from django.urls import reverse_lazy
import threading
from .models import Orders
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from trade.stock.models import Stock
from trade.dashboard.views import validate_user_session
from trade.t_api.models import AddApi
from .p_thread import PriceThread
from.placeorder import PlaceOrder


def order(request, id, token, sid):
    UserModel = get_user_model()
    user = UserModel.objects.get(id=id)
    if not validate_user_session(id, token):
        return render(request, 'p404.html')
    stocks = Stock.objects.get(id=sid)
    orders = Orders.objects.filter(user_id=id).values
    key = AddApi.objects.get(user_id=user.id)
    p1 = PriceThread(str(key.api_key), str(
        key.secret_key), str(stocks.stock))
    p1.start()
    if request.method == 'POST':
        bprice = request.POST['b_price']
        bquan = request.POST['b_qun']
        btime = request.POST['btime']
        sprice = request.POST['s_price']
        squan = request.POST['s_qun']
        stime = request.POST['stime']
        b = Orders(stock=stocks.stock, b_p=bprice,
                   s_p=sprice, bquantity=bquan, squantity=squan, btime=btime, stime=stime, user_id=id)
        b.save()
        context = {
            'user': user,
            'stocks': stocks,
            'orders': orders
        }
        return render(request, 'order.html', context)
    context = {
        'orders': orders,
        'stocks': stocks
    }
    return render(request, 'order.html', context)


def buy(request, id, sym):
    UserModel = get_user_model()
    user = UserModel.objects.get(id=id)
    key = AddApi.objects.get(user_id=user.id)
    p1 = PlaceOrder(str(key.api_key), str(
        key.secret_key), sym, id, 'buy')
    p1.start()
    context = {
        'user': user
    }
    return render(request, 'thanks.html', context)


def sell(request, id, sym):
    UserModel = get_user_model()
    user = UserModel.objects.get(id=id)
    key = AddApi.objects.get(user_id=user.id)
    p1 = PlaceOrder(str(key.api_key), str(
        key.secret_key), sym, id, 'sell')
    p1.start()
    context = {
        'user': user
    }
    return render(request, 'thanks.html', context)


def auto(request, id, sym):
    UserModel = get_user_model()
    user = UserModel.objects.get(id=id)
    key = AddApi.objects.get(user_id=user.id)
    p1 = PlaceOrder(str(key.api_key), str(
        key.secret_key), sym, id, 'auto')
    p1.start()
    context = {
        'user': user
    }
    return render(request, 'thanks.html', context)
