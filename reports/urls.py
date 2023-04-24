from django.urls import path
from .views import *

urlpatterns = [
    path('', AcceptReportView.as_view(), name='accept_list'),
]
