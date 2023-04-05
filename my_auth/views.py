from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as LogOutView
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth import login

from .apps import MyAuthConfig
from .forms import *

APP_NAME = MyAuthConfig.name


class LogInView(BaseLoginView):
    template_name = APP_NAME + '/login.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = APP_NAME + '/signup.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)
