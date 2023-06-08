from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from trips.models import Trip
from commons.decorators import perm_required
from commons.mixins import PermissionRequiredMixin

from .models import Order
from .apps import APP_NAME
from .forms import *
from .filter_sets import OrderFilterSet

# TODO: Restrict view for non related users


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = APP_NAME + '/detail.html'
    context_object_name = 'order'


class OrderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = APP_NAME + '/create.html'

    required_perm = APP_NAME + '.add_order'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.customer = self.request.user
        instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.object.get_absolute_url()


class OrderListView(LoginRequiredMixin, FilterView):
    model = Order
    template_name = APP_NAME + '/list.html'
    filterset_class = OrderFilterSet


@require_POST
@perm_required('accept_order')
def order_accept_view(request, *args, **kwargs):
    pk = request.POST.get('pk')
    order = Order.objects.get(pk=pk)
    if order.is_open:
        driver = request.user
        Trip.objects.create(order=order, driver=driver)

        success_url = reverse('trips:detail', args=[pk])
        return HttpResponseRedirect(success_url)


@require_POST
def order_cancel_view(request, *args, **kwargs):
    pk = request.POST.get('pk')
    order = Order.objects.get(pk=pk)
    if order.is_open:
        order.has_user_in_field(request.user, 'customer', is_safe=False)
        order.delete()

        success_url = reverse(APP_NAME + ':create')
        return redirect(success_url)
