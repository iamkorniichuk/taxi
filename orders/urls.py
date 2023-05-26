from django.urls import path
from .views import *


app_name = APP_NAME

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    path('accept/', OrderAcceptView.as_view(), name='accept'),
    path('<int:pk>', OrderDetailView.as_view(), name='detail'),
    path('cancel/', OrderCancelView.as_view(), name='cancel'),
]
