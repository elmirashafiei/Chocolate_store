from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'accounts/login.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')


class LoginView(LoginView):
    template_name = 'accounts/login.html'


class PasswordChangeView(PasswordChangeView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:login')
