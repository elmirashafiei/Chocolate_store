import datetime

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from cart.cart import Cart
from orders.models import Order, OrderLine
from products.models import Product
from .forms import SignUpForm
from .models import UserAccount


class SignUpView(CreateView):
    template_name = 'accounts/login.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:login')


class CustomerLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        result = super().form_valid(form)

        user = self.request.user
        profile = UserAccount.objects.get(user=user)
        my_cart = Cart(self.request)  # this is the offline cart (before logging in)

        if len(my_cart) == 0:
            return result

        if Order.objects.filter(client=profile, active=True).exists():
            active_order = Order.objects.get(client=profile, active=True)
        else:
            active_order = Order.objects.create(client=profile, active=True,
                                                date_of_submission=datetime.date.today(),
                                                sum=0,
                                                )

        order_items = active_order.order_lines.all()
        my_cart_copy = {}  # make a copy of the products + quantities in that offline cart

        for key in my_cart.cart:  # update the session cart from the database
            my_cart_copy[key] = my_cart.cart[key].copy()

        for item in order_items:  # update the session cart from the database
            my_cart.add(item.product, item.quantity)

        for product_id in my_cart_copy:  # update the database with the copy of the offline cart
            my_product = Product.objects.get(id=int(product_id))
            if OrderLine.objects.filter(product=my_product, order=active_order).exists():
                item = OrderLine.objects.get(product=my_product, order=active_order)
                item.quantity += my_cart_copy[product_id]['quantity']
                item.save()
            else:
                OrderLine.objects.create(
                    order=active_order,
                    product=my_product,
                    price=my_product.price,
                    quantity=my_cart_copy[product_id]['quantity']
                )
        return result


def order_detail(request):
    user = request.user
    profile = UserAccount.objects.get(user=user)
    final_orders = Order.objects.filter(client=profile, active_cart=False).order_by('-id')

    return render(request, 'accounts/order_detail.html', {'orders': final_orders})
