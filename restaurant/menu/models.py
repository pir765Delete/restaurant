from django.db import models
from django.db.models import ImageField
from users.models import User


class Dish(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)


    objects = BasketQuerySet.as_manager()
    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product}'

    def sum(self):
        return self.product.price * self.quantity


class OrderQuerySet(models.QuerySet):
    def total_sum(self):
        orders = self.filter(status='Выполнено')
        return sum(order.price for order in orders)


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True, default="Обрабатывается")
    price = models.DecimalField(max_digits=8, decimal_places=2)

    objects = OrderQuerySet.as_manager()

    def change_status(self, new_value):
        self.status = new_value
        self.save()
    def __str__(self):
        return f'Заказ № {self.id}'

