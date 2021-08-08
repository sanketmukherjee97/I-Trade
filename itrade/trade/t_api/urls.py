from django.urls import path
from . import views

urlpatterns = [
    path('', views.addApi, name='addapi'),
]
