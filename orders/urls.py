from django.urls import path
from .views import *


app_name = APP_NAME

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    path('accept/', OrderAcceptView.as_view(), name='accept'),
]
