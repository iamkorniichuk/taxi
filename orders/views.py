from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from trips.models import Trip

from .models import Order
from .apps import APP_NAME
from .forms import *


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = APP_NAME + '/detail.html'
    context_object_name = 'order'


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = APP_NAME + '/create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.customer = self.request.user
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class OrderAcceptView(LoginRequiredMixin, ListView):
    model = Order
    template_name = APP_NAME + '/accept_list.html'
    context_object_name = 'orders'
    success_accept_url = 'trips:detail'

    def get_queryset(self):
        return [order for order in self.model.objects.all() if order.is_open]

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk', None)
        order = Order.objects.get(pk=pk)
        driver = request.user
        Trip.objects.create(order=order, driver=driver)
        return HttpResponseRedirect(reverse_lazy(self.success_accept_url, args=[pk]))


class OrderCancelView(LoginRequiredMixin, View):
    success_url = APP_NAME + ':create'

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk', None)
        order = Order.objects.get(pk=pk)
        order.delete()
        return redirect(reverse(self.success_url))
