from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Trip
from .apps import APP_NAME


class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip
    template_name = APP_NAME + '/detail.html'
    context_object_name = 'trip'
    success_ended_url = reverse_lazy('orders:accept_list')

    def post(self, request, *args, **kwargs):
        trip = Trip.objects.get(pk=kwargs['pk'])
        trip.end_datetime = timezone.now()
        trip.save()
        return HttpResponseRedirect(self.success_ended_url)
