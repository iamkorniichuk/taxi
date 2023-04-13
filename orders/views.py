from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

from orders.models import Order

from .apps import OrdersConfig
from .forms import *

APP_NAME = OrdersConfig.name


class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = APP_NAME + '/create.html'
    # TODO: Provide valid url
    success_url = 'home'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.customer = self.request.user.customer
        instance.save()
        return super().form_valid(form)


class AcceptOrderView(LoginRequiredMixin, ListView):
    model = Order
    template_name = APP_NAME + '/accept.html'
    context_object_name = 'orders'
