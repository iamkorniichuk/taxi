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


class AccountDetailView(DetailView):
    template_name = APP_NAME + '/account.html'
    context_object_name = 'account'


class ModeView(LoginRequiredMixin, View):
    def post(self, request):
        if set_mode(request, request.POST.get('mode_name')):
            return redirect('home')
