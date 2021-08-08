from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/<str:token>/<int:sid>/', views.order, name='order'),
    path('buy/<int:id>/<str:sym>/', views.buy, name='buy'),
    path('sell/<int:id>/<str:sym>/', views.sell, name='sell'),
    path('auto/<int:id>/<str:sym>/', views.auto, name='auto')
]
