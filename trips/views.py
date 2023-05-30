from django.utils import timezone
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Trip
from .apps import APP_NAME

# TODO: Restrict view for non related users
class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip
    template_name = APP_NAME + '/detail.html'
    context_object_name = 'trip'

@require_POST
def trip_end_view(request, *args, **kwargs):
    trip = request.POST.get('pk')
    trip.has_user_in_any_field(request.user, ['customer', 'driver'],
                               is_safe=False)

    trip.end_datetime = timezone.now()
    trip.save()

    success_url = reverse('orders:accept_list')
    return HttpResponseRedirect(success_url)
