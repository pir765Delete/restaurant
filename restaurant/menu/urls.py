from django.urls import path
from . import views
from .views import Dish, basket_add, basket_remove

urlpatterns = [
    path('', views.index, name='main'),
    path('basket/', views.basket, name='basket'),
    path('order/', views.order, name='order'),
    path('order/add', views.create_order, name='create_order'),
    path('order/return/<int:order_id>', views.order_return_step, name='order_return_step'),
    path('order/remove/<int:order_id>', views.order_pay, name='order_pay'),
    path('order/next/<int:order_id>', views.order_next_step, name='order_next_step'),
    path('order/return/<int:order_id>', views.order_return_step, name='order_return_step'),
    path('baskets/add/<int:product_id>', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>', views.basket_remove, name='basket_remove'),
]
