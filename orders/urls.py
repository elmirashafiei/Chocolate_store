from django.urls import path

<<<<<<< HEAD
from orders import views
=======
from . import views
>>>>>>> feature/Order-Models

app_name = "orders"
urlpatterns = [
    path('order_placed/', views.order_placed, name='order_placed'),
]
