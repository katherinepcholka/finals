from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cart.views import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem


@login_required
def create_order(request):
    cart = Cart.objects.filter(user=request.user)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item.product,
                                         price=item.product.price,
                                         quantity=item.quantity)
            cart.delete()
            return render(request, 'main/main_page.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})

