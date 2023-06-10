from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as LogOutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, RedirectView
from django.contrib.auth import login


from .apps import APP_NAME
from .forms import *


class LogInView(BaseLoginView):
    template_name = APP_NAME + '/login.html'
    form_class = LogInForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = APP_NAME + '/signup.html'
    success_url = reverse_lazy('about')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = APP_NAME + '/update.html'
    form_class = UpdateForm
    success_url = reverse_lazy(APP_NAME + ':my_profile')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileView(DetailView):
    model = get_user_model()
    template_name = APP_NAME + '/profile.html'
    context_object_name = 'profile'


class MyProfileView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse(APP_NAME + ':profile', kwargs={'pk': self.request.user.pk})
