from django.urls import path

from .apps import ReportsConfig
from .views import *


app_name = ReportsConfig.name

urlpatterns = [
    path('', ReportListView.as_view(), name='list'),
    path('<int:pk>', ReportDetailView.as_view(), name='detail'),
    path('answer', report_answer_view, name='answer')
]
