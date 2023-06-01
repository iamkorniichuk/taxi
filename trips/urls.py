from django.urls import path
from .views import *


app_name = APP_NAME


urlpatterns = [
    path('<int:pk>/', TripDetailView.as_view(), name='detail'),
    path('', TripListView.as_view(), name='list'),
    path('end/', trip_end_view, name='end')
]
