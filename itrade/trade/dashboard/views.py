from django.shortcuts import render
from django.contrib.auth import get_user_model
from trade.t_api.models import AddApi
from trade.stock.models import Stock
from .api_thread import ApiThread, API_KEY, SECRET_KEY, symbols


def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


def dashboard(request, id, token):
    UserModel = get_user_model()
    user = UserModel.objects.get(pk=id)
    stock = Stock.objects.filter(user_id=id).values()
    key = AddApi.objects.get(user_id=user.id)
    API_KEY = key.api_key
    SECRET_KEY = key.secret_key
    # for st in stock:
    #     symbols.append(st)
    # th1 = ApiThread()
    if not validate_user_session(id, token):
        return render(request, 'p404.html')
    if not AddApi.objects.filter(user_id=user.id).exists():
        th1.start()
        context = {
            'user': user
        }
        return render(request, 'key.html', context)
    # th1.start()
    context = {
        'user': user,
        'stock': stock
    }
    return render(request, 'dash.html', context)
