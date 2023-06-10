from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView

from .models import Trip
from .filter_sets import TripFilterSet
from .apps import APP_NAME


class TripListView(LoginRequiredMixin, FilterView):
    model = Trip
    template_name = APP_NAME + '/list.html'
    filterset_class = TripFilterSet


# TODO: Restrict view for non related users
class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip
    template_name = APP_NAME + '/detail.html'
    context_object_name = 'trip'


@require_POST
def trip_end_view(request, *args, **kwargs):
    pk = request.POST.get('pk')
    trip = Trip.objects.get(pk=pk)
    user = request.user
    if trip.driver != user and trip.order.customer != user:
        raise PermissionDenied

    trip.complete_datetime = timezone.now()
    trip.save()

    success_url = reverse('orders:list')
    return HttpResponseRedirect(success_url)
