from django.urls import path

from .views import *

urlpatterns = [
    path('', MeRedirectView.as_view(), name='me'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer'),
    path('<int:pk>/customer', CustomerDetailView.as_view(), name='customer'),
    path('<int:pk>/driver', DriverDetailView.as_view(), name='driver'),
    path('<int:pk>/manager', ManagerDetailView.as_view(), name='manager'),
    path('<int:pk>/director', DirectorDetailView.as_view(), name='director'),
    path('mode', ModeView.as_view(), name='mode'),
]
