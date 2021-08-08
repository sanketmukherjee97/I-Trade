from django.contrib.auth import models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
import random

User = get_user_model()


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)]+[str(i) for i in range(10)]) for _ in range(length))


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_pass = request.POST['confirm_pass']
        if password == conf_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print(request, 'user created')
                return redirect('/')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
    else:
        context = {}
        return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            token = generate_session_token()
            user.session_token = token
            user.save()
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Wrong email or password')
            return redirect("login")
    else:
        context = {}
        return render(request, 'login.html', context)


def logout(request, id):
    user = User.objects.get(pk=id)
    user.session_token = "0"
    user.save()
    auth.logout(request)
    return redirect('/')
