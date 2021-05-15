from django.urls import path
from products import views


app_name = "products"
urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.ProductsViewList.as_view(), name="products"),
    path('product/detail/<pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/search_products/', views.search_products, name="search_products"),
]