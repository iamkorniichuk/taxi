from orders.views import CreateOrderView, AcceptOrderView
from django.views.generic import *
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request, *args, **kwargs):
    user = request.user
    view = None
    if user.is_customer:
        view = CreateOrderView.as_view()
    elif user.is_driver:
        view = AcceptOrderView.as_view()
    return view(request)
