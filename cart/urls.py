from django.urls import path
<<<<<<< HEAD
=======

>>>>>>> feature/Order-Models
from . import views

app_name = "cart"
urlpatterns = [
<<<<<<< HEAD
    path('', views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add,name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove,name='cart_remove'),
]
=======
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
>>>>>>> feature/Order-Models
