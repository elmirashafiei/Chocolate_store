from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from accounts.models import UserAccount
from products.models import Product
from orders.models import Order
from orders.orders import add_product_to_basket, remove_product_from_basket
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        cart.add(product=product, quantity=quantity)

        if request.user.is_authenticated:
            account = UserAccount.objects.get(user=request.user)
            if Order.objects.filter(client=account, active=True).exists():
                active_order = Order.objects.get(client=account, active=True)
            else:
                active_order = Order.objects.create(client=profile, active=True)

            add_product_to_basket(active_order, product_id, quantity)



    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    if request.user.is_authenticated:
        account = UserAccount.objects.get(user=request.user)
        if Order.objects.filter(client=account, active=True).exists():
            active_order = Order.objects.get(client=account, active=True)
        else:
            active_order = Order.objects.create(client=profile, active=True)

        remove_product_from_basket(active_order, product_id)

    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
