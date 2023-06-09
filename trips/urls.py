from django.urls import path

from .apps import TripsConfig
from .views import *


app_name = TripsConfig.name


urlpatterns = [
    path("<int:pk>/", TripDetailView.as_view(), name="detail"),
    path("", TripListView.as_view(), name="list"),
    path("end/", trip_end_view, name="end"),
    path("rating/", trip_rating_view, name="rating"),
    path("tip/", trip_tip_view, name="tip"),
    path("report/", trip_report_view, name="report"),
]
