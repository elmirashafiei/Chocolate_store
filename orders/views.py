from django.shortcuts import render

from cart.cart import Cart


def order_placed(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'orders/order_placed.html')
