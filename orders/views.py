from django.contrib.auth.decorators import login_required
from django.shortcuts import render

<<<<<<< HEAD
from cart.cart import Cart


def order_placed(request):
    cart = Cart(request)
    cart.clear()
=======
from accounts.models import UserAccount
from cart.cart import Cart
from .models import Order


@login_required
def order_placed(request):
    cart = Cart(request)
    user = request.user
    profile = UserAccount.objects.get(user=user)
    active_order = Order.objects.get(client=profile)

    active_order.active_cart = False
    active_order.order_status = 'PD'
    active_order.invoice_total = cart.get_total_price()

    active_order.save()
    cart.clear()

>>>>>>> feature/Order-Models
    return render(request, 'orders/order_placed.html')
