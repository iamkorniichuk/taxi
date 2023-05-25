from django.urls import path
from .views import *


app_name = APP_NAME

urlpatterns = [
    path('', ReportAcceptView.as_view(), name='accept'),
]
