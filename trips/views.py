from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from commons.responses import refresh
from reports.models import Report

from .models import Trip
from .filter_sets import TripFilterSet


class TripListView(LoginRequiredMixin, FilterView):
    model = Trip
    template_name = "trips/list.html"
    filterset_class = TripFilterSet


# TODO: Restrict view for non related users
class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip
    template_name = "trips/detail.html"
    context_object_name = "trip"


@require_POST
def trip_end_view(request, *args, **kwargs):
    pk = request.POST.get("pk")
    trip = Trip.objects.get(pk=pk)
    user = request.user
    if trip.driver != user and trip.order.customer != user:
        raise PermissionDenied

    trip.complete_datetime = timezone.now()
    trip.save()

    return refresh(request)


@require_POST
def trip_rating_view(request, *args, **kwargs):
    pk = request.POST.get("pk")
    rating = request.POST.get("rating")
    trip = Trip.objects.get(pk=pk)
    user = request.user
    if trip.order.customer != user:
        raise PermissionDenied

    trip.rating = rating
    trip.save()

    return refresh(request)


@require_POST
def trip_tip_view(request, *args, **kwargs):
    pk = request.POST.get("pk")
    tip = request.POST.get("tip")
    trip = Trip.objects.get(pk=pk)
    user = request.user
    if trip.order.customer != user:
        raise PermissionDenied

    trip.tip = tip
    trip.save()

    return refresh(request)


@require_POST
def trip_report_view(request, *args, **kwargs):
    pk = request.POST.get("pk")
    message = request.POST.get("message")
    trip = Trip.objects.get(pk=pk)
    user = request.user

    if trip.order.customer != user:
        raise PermissionDenied

    report = Report.objects.create(trip=trip, message=message)

    return redirect(report.get_absolute_url())
