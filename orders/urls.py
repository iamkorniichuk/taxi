from django.urls import path

from .views import *

urlpatterns = [
    path('', OrderRedirectView.as_view(), name='main'),
    path('main/', OrderRedirectView.as_view(), name='main'),
    path('customer/', OrderListView.as_view(), name='create'),
    path('driver/', OrderCreateView.as_view(), name='list'),
]
