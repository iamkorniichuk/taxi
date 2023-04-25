from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as LogOutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login


from .apps import APP_NAME
from .forms import *


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


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = APP_NAME + '/update_user.html'
    fields = ('first_name', 'last_name', 'image')
    success_url = reverse_lazy('accounts:me')

    def get_object(self, queryset=None):
        return self.request.user
