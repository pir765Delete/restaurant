from django.shortcuts import render
from .models import Dish

def index(request):
    board = Dish.objects.all
    return render(request, 'menu/base-menu.html', {'board': board})
