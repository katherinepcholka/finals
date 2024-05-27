# Generated by Django 4.2.11 on 2024-05-27 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderitem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.BooleanField(choices=[(False, 'В пути'), (True, 'Доставлен')], default=0, verbose_name='Статус'),
        ),
    ]