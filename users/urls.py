from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogOutView.as_view(), name='logout'),
]
