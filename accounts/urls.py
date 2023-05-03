from django.urls import path

from .views import *

urlpatterns = [
    path('', MeRedirectView.as_view(), name='me'),
    path('<int:pk>/customer', AccountDetailView.as_view(model=Customer), name='customer'),
    path('<int:pk>/driver', AccountDetailView.as_view(model=Driver), name='driver'),
    path('<int:pk>/manager', AccountDetailView.as_view(model=MyManager), name='manager'),
    path('<int:pk>/director', AccountDetailView.as_view(model=MyDirector), name='director'),
    path('mode', ModeView.as_view(), name='mode'),
]
