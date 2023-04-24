from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from trips.models import Trip

from .models import Order
from .apps import OrdersConfig
from .forms import *

APP_NAME = OrdersConfig.name


class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = APP_NAME + '/create.html'
    # TODO: Provide valid url
    success_url = ''

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.customer = self.request.user.customer
        instance.save()
        return super().form_valid(form)


class AcceptOrderView(LoginRequiredMixin, ListView):
    model = Order
    template_name = APP_NAME + '/accept_list.html'
    context_object_name = 'orders'
    success_accept_url = 'trips:detail'

    def get_queryset(self):
        return [order for order in self.model.objects.all() if order.is_open]

    def post(self, request, *args, **kwargs):
        order_pk = request.POST.get('order_pk', None)
        order = Order.objects.filter(pk=order_pk).first()
        driver = request.user.driver
        Trip.objects.create(order=order, driver=driver)
        return HttpResponseRedirect(reverse_lazy(self.success_accept_url, args=[order_pk]))
