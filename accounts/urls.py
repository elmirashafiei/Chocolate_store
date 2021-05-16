from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.urls import path

from .views import SignUpView, CustomerLoginView

app_name = "accounts"
urlpatterns = [
    path("login/", CustomerLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("password_change/", PasswordChangeView.as_view(), name='password_change'),
    path("signup/", SignUpView.as_view(), name='signup')
]
