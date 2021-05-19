from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import SignUpView, CustomerLoginView, MyPasswordChangeView, order_detail

app_name = "accounts"
urlpatterns = [
    path("login/", CustomerLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("password_change/", MyPasswordChangeView.as_view(), name='password_change'),
    path("signup/", SignUpView.as_view(), name='signup'),
    path("order_detail/", views.order_detail, name='order_detail'),
]
