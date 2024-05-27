from django.db import models
from users.models import User
from main.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def sum(self):
        return self.quantity * self.product.price

    class Meta():
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

