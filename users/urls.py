from django.urls import path
from .views import *


app_name = APP_NAME

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('<int:pk>', ProfileView.as_view(), name='profile'),
    path('my', MyProfileView.as_view(), name='my_profile'),
]
