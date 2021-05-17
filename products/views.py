import json

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from cart.forms import CartAddProductForm
from products.models import Product, Category


def home(request, s0):
    s1 = request.GET.get('s1', '')  # Get the variable s1 from the URL encoder
    return render(
        request, template_name='viewer/hello.html',  # Template is the file you want to load
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}  # context are the variable you send to the template
    )


def index(request):
    return render(
        request, template_name='products/index.html',  # Template is the file you want to load
    )


def search_products(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')

        products = Product.objects.filter(
            title__startswith=search_str) | Product.objects.filter(
            description__icontains=search_str)
        data = products.values()
        print(data)
        return JsonResponse(list(data), safe=False)


class CategoriesViewList(ListView):
    template_name = "categories/categories.html"
    model = Category


class CategoryDetailView(DetailView):
    template_name = "categories/category-detail.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        category = context['category']
        context['category_products'] = category.products.all()
        return context


class ProductsViewList(ListView):
    template_name = "products/products.html"
    model = Product


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, StaffRequiredMixin, DeleteView):
    template_name = "products/delete_form.html"
    model = Product
    success_url = reverse_lazy("products")
    permission_required = "products.delete_product"

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser


class ProductDetailView(DetailView):
    template_name = "products/product_detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['form'] = CartAddProductForm
        return context
