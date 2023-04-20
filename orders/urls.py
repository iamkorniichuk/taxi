from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='create'),
    path('accept_list/', AcceptOrderView.as_view(), name='accept_list'),
]
