from django.shortcuts import render, redirect
from .models import Pizza, Ingredient, Order
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'recipes/index.html')

def menu(request):
    pizzas = Pizza.objects.all()
    return render(request, 'recipes/menu.html', {'pizzas': pizzas})

@login_required
def cart(request):
    return render(request, 'cart.html')

@login_required
def order_status(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_status.html', {'orders': orders})

