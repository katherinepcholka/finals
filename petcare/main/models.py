from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children', db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name="Slug")

    class MPTTMeta:
        order_insertion_by = ['slug']

    class Meta:
        unique_together = [['parent', 'slug']]
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('product_list', kwargs={'slug': self.slug})   


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=Product.Status.AVAILABLE)


class Product(models.Model):
    class Status(models.IntegerChoices):
        UNAVAILABLE = 0, 'Недоступен'
        AVAILABLE = 1, 'Доступен'

    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name="Категория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="Slug")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Фото")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    is_available = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.UNAVAILABLE, verbose_name="Статус")

    objects = models.Manager()
    available = AvailableManager() 

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})   