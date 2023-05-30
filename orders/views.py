from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin

from trips.models import Trip
from commons.decorators import perm_required
from commons.mixins import PermissionRequiredMixin

from .models import Order
from .apps import APP_NAME
from .forms import *

# TODO: Restrict view for non related users
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = APP_NAME + '/detail.html'
    context_object_name = 'order'


class OrderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = APP_NAME + '/create.html'

    required_perm = 'add_order'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.customer = self.request.user
        instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class OrderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Order
    template_name = APP_NAME + '/list.html'
    context_object_name = 'orders'

    required_perm = 'view_order'


@require_POST
@perm_required('accept_order')
def order_accept_view(request, *args, **kwargs):
    pk = request.POST.get('pk')
    order = Order.objects.get(pk=pk)
    driver = request.user
    Trip.objects.create(order=order, driver=driver)

    success_url = reverse('trips:detail', args=[pk])
    return HttpResponseRedirect(success_url)


@require_POST
def order_cancel_view(request, *args, **kwargs):
    pk = request.POST.get('pk')
    order = Order.objects.get(pk=pk)

    order.has_user_in_field(request.user, 'customer', is_safe=False)
    order.delete()
    
    success_url = reverse(APP_NAME + ':create')
    return redirect(success_url)
