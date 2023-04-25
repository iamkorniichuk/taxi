from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import DetailView, RedirectView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .modes import set_mode
from .apps import APP_NAME
from .models import *


class MeRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = self.request.user.pk
        return reverse(APP_NAME + ':customer', args=[pk])


class CustomerDetailView(DetailView):
    model = Customer
    template_name = APP_NAME + '/customer.html'
    context_object_name = 'account'


class DriverDetailView(DetailView):
    model = Driver
    template_name = APP_NAME + '/driver.html'
    context_object_name = 'account'


class ManagerDetailView(DetailView):
    model = MyManager
    template_name = APP_NAME + '/manager.html'
    context_object_name = 'account'


class DirectorDetailView(DetailView):
    model = MyDirector
    template_name = APP_NAME + '/director.html'
    context_object_name = 'account'


class ModeView(LoginRequiredMixin, View):
    def post(self, request):
        if set_mode(request, request.POST.get('mode_name')):
            return redirect('home')
