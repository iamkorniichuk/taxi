from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from trips.models import Trip
from commons.decorators import any_perm_required

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

# TODO: Create one listview, alter buttons due to user's groups, separate actions to post views
class OrderAcceptView(LoginRequiredMixin, ListView):
    model = Order
    template_name = APP_NAME + '/accept_list.html'
    context_object_name = 'orders'
    success_accept_url = 'trips:detail'

    def get_queryset(self):
        return self.model.objects.filter(trip__order=None)

    # TODO: Check
    @method_decorator(any_perm_required(APP_NAME + '.accept_order'))
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk', None)
        order = Order.objects.get(pk=pk)
        driver = request.user
        Trip.objects.create(order=order, driver=driver)
        return HttpResponseRedirect(reverse_lazy(self.success_accept_url, args=[pk]))


class OrderCancelView(LoginRequiredMixin, View):
    success_url = APP_NAME + ':create'

    @method_decorator(any_perm_required(APP_NAME + '.cancel_order'))
    def post(self, request, *args, **kwargs):
        pk = request.POST.get('pk', None)
        order = Order.objects.get(pk=pk)
        if request.user == order.customer:
            order.delete()
            return redirect(reverse(self.success_url))
        raise HttpResponseForbidden
