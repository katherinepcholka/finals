from django.urls import path
from .views import MainPage, ProductByCategory, ShowProduct, Search
from . import views


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('about', views.about, name='about'),
    path('catalog/<str:slug>/', ProductByCategory.as_view(), name='product_list'),
    path('product/<int:prdt_id>', ShowProduct.as_view(), name='product'),
    path('search/', Search.as_view(), name='search'),
]
