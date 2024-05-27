from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from main.models import Product
from .models import Cart

@login_required
def add_item(request, prdt_id):
    current_page = (request.META.get('HTTP_REFERER'))
    product = Product.objects.get(id=prdt_id)
    cart = Cart.objects.filter(user=request.user, product=product)
    if not cart.exists():
        Cart.objects.create(user=request.user, product=product)
        return HttpResponseRedirect(current_page)
    else:
        cart = cart.first()
        cart.quantity += 1
        cart.save()
        return HttpResponseRedirect(current_page)

@login_required
def cart(request):
    goods_list = Cart.objects.filter(user=request.user)

    total_quantity = sum(goods.quantity for goods in goods_list)
    total_sum = sum(goods.sum() for goods in goods_list)

    data = {
        'goods_list': goods_list,
        'total_quantity': total_quantity ,
        'total_sum': total_sum,
        }
    return render (request, 'cart/cart.html', data)

@login_required
def delete_items(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('cart:cart')
