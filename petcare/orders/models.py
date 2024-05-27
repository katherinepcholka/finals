from django.db import models
from main.models import Product

class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя',)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия',)
    email = models.EmailField(verbose_name='Почта',)
    phone = models.CharField(max_length=20, verbose_name='Телефон',)
    address = models.CharField(max_length=200, verbose_name='Адрес')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    city = models.CharField(max_length=100, verbose_name='Город')

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатель'

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    class Status(models.IntegerChoices):
        ON_THE_WAY = 0, 'В пути'
        DELIVERED = 1, 'Доставлен'


    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Получатель')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кол-во')
    status = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.ON_THE_WAY, verbose_name="Статус")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_cost(self):
        return self.price * self.quantity