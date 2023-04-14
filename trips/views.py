from django.http import HttpResponseRedirect
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

from orders.models import Order
from .models import Trip
from .apps import TripsConfig

APP_NAME = TripsConfig.name


class AcceptOrderView(LoginRequiredMixin, ListView):
    model = Order
    template_name = APP_NAME + '/accept.html'
    context_object_name = 'orders'
    # TODO: provide valid url
    success_accept_url = ''

    def post(self, request, *args, **kwargs):
        order_pk = request.POST.get('order_pk', None)
        print(order_pk)
        order = Order.objects.filter(pk=order_pk).first()
        driver = request.user.driver
        Trip.objects.create(order=order, driver=driver)
        return HttpResponseRedirect(self.success_accept_url)
