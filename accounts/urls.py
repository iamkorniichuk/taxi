from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer'),
    path('', MyRedirectView.as_view(), name='my'),
    path('<int:pk>/customer', CustomerDetailView.as_view(), name='customer'),
    path('<int:pk>/driver', DriverDetailView.as_view(), name='driver'),
    path('<int:pk>/manager', ManagerDetailView.as_view(), name='manager'),
    path('<int:pk>/director', DirectorDetailView.as_view(), name='director'),
]
