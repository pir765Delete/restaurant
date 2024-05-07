from django.shortcuts import render, HttpResponseRedirect
from .models import Dish, Basket, Order
from django.contrib.auth.decorators import login_required
def index(request):
    board = Dish.objects.all
    return render(request, 'menu/base-menu.html', {'board': board})


def basket(request):
    user = request.user
    if user.groups.filter(name='Admins').exists():
        flag = True
    elif user.groups.filter(name='Waiters').exists():
        flag = True
    else:
        flag = False
    context = {
        'baskets': Basket.objects.filter(user=request.user),
        'flag': flag,
    }
    return render(request, 'menu/baskets.html', context)


@login_required
def basket_add(request, product_id):
    product = Dish.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def order(request):
    user = request.user
    if user.groups.filter(name='Admins').exists():
        flag = 'Admins'
    elif user.groups.filter(name='Waiters').exists():
        flag = 'Waiters'
    elif user.groups.filter(name='Cooks').exists():
        flag = 'Cooks'
    elif user.groups.filter(name='Bookers').exists():
        flag = 'Bookers'
    else:
        flag = 'Users'
    context = {
        'orders': Order.objects.all(),
        'flag': flag,
    }
    return render(request, 'menu/orders.html', context)


def order_pay(request, order_id):
    orders = Order.objects.all()
    for order in orders:
        if order.id == order_id:
            order.change_status("Выполнено")
    return HttpResponseRedirect('/order')

def order_next_step(request, order_id):
    orders = Order.objects.all()
    for order in orders:
        if order.id == order_id:
            order.change_status("Готовится")
    return HttpResponseRedirect('/order')

def order_return_step(request, order_id):
    orders = Order.objects.all()
    for order in orders:
        if order.id == order_id:
            order.change_status("Готово к выдаче")
    return HttpResponseRedirect('/order')

def create_order(request):
    user = request.user
    summ = 0
    baskets = Basket.objects.filter(user=user)
    for basket in baskets:
        summ += basket.sum()
        basket.delete()
    Order.objects.create(user=user, status="В работе", price=summ)

    return HttpResponseRedirect('/order')