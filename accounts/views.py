from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'accounts/login.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')


class PasswordChangeView(PasswordChangeView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:login')


class CustomerLoginView(LoginView):
    template_name = 'accounts/login.html'

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     user = self.request.user
    #     profile = Profile.objects.get(user=user)
    #     active_order = Order.objects.get(client=profile, active_basket=True)
    #     order_items = active_order.items.all()
    #     my_basket = Basket(self.request)    # this is the offline basket (before logging in)
    #     my_basket_copy = my_basket.basket.copy()   # make a copy of the products + quantities in that offline basket
    #     for item in order_items:    # update the session basket from the database
    #         my_basket.add(item.product, item.quantity)
    #     for product_id in my_basket_copy:   # update the database with the copy of the offline basket
    #         my_product = Product.objects.get(id=int(product_id))
    #         if OrderItem.objects.filter(product=my_product, order=active_order).exists():
    #             item = OrderItem.objects.get(product=my_product, order=active_order)
    #             item.quantity += my_basket_copy[product_id]['qty']
    #             item.save()
    #         else:
    #             OrderItem.objects.create(
    #                 order=active_order,
    #                 product=my_product,
    #                 price=my_product.price,
    #                 quantity=my_basket_copy[product_id]['qty']
    #             )
    #     return result