from django.urls import path
from .views import *


app_name = APP_NAME

urlpatterns = [
    path('', ReportListView.as_view(), name='list'),
    path('<int:pk>', ReportDetailView.as_view(), name='detail'),
    path('accept/', report_accept_view, name='accept'),
]
