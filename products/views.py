from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


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

class ProductsViewList(ListView):
    template_name = "products/products.html"
    model = Product
