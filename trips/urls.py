from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', TripDetailView.as_view(), name='detail'),
]
