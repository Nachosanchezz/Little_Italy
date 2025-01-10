from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('order_status/', views.order_status, name='order_status'),
]
