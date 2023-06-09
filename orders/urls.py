from django.urls import path

from .apps import OrdersConfig
from .views import *


app_name = OrdersConfig.name

urlpatterns = [
    path("", OrderListView.as_view(), name="list"),
    path("<int:pk>", OrderDetailView.as_view(), name="detail"),
    path("create/", OrderCreateView.as_view(), name="create"),
    path("accept/", order_accept_view, name="accept"),
    path("cancel/", order_cancel_view, name="cancel"),
]
