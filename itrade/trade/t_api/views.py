from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import AddApi

userModel = get_user_model()


def addApi(request, id):
    user = userModel.objects.get(id=id)
    if request.method == 'POST':
        a_key = request.POST['a_key']
        s_key = request.POST['s_key']
        add = AddApi(api_key=a_key, secret_key=s_key, user_id=user.id)
        add.save()
        context = {
            'user': user
        }
        return render(request, 'dash.html', context)

    else:
        context = {}
        return render(request, 'key.html', context)
