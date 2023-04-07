from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, RedirectView

from .apps import OrdersConfig
from .models import Order
from .forms import *

APP_NAME = OrdersConfig.name


class OrderListView(ListView):
    model = Order
    template_name = APP_NAME + '/list.html'
    context_object_name = 'orders'


class OrderCreateView(CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = APP_NAME + '/form.html'

class OrderRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        view_name = APP_NAME + ':'
        if user.is_driver: view_name += 'create'
        else: view_name += 'list'
        return reverse(view_name)
