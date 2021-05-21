from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime
from accounts.models import UserAccount
from cart.cart import Cart
from .models import Order


@login_required
def order_placed(request):
    cart = Cart(request)
    user = request.user
    profile = UserAccount.objects.get(user=user)
    active_order = Order.objects.get(client=profile, active=True)

    active_order.active = False
    active_order.order_status = 'PD'
    active_order.invoice_total = cart.get_total_price()
    active_order.date_of_submission = datetime.date.today()
    active_order.save()
    cart.clear()

    return render(request, 'orders/order_placed.html')


def order_detail(request):
    user = request.user
    profile = UserAccount.objects.get(user=user)
    final_orders = Order.objects.filter(client=profile, active=False).order_by('-id')

    items = []
    for order in final_orders:
        items += list(order.order_lines.all())

    return render(request, 'orders/order_detail.html', {'orders': final_orders, 'items': items})

