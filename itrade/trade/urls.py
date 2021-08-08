from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('trade.users.urls')),
    path('dashboard/<int:id>/<str:token>/', include('trade.dashboard.urls')),
    path('stock/<int:id>/', include('trade.stock.urls')),
    path('add-api/<int:id>/', include('trade.t_api.urls')),
    path('order/', include('trade.orders.urls'))
]
