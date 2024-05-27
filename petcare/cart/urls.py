from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('', views.cart, name= 'cart'),
    path('add_item/<int:prdt_id>', views.add_item, name= 'add_item'),
    path('delete_items/<int:id>', views.delete_items, name= 'delete_items'),
]