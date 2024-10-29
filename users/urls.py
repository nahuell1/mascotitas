from django.urls import path
from .views import UserDetailView

app_name = 'users'

urlpatterns = [
    path('', UserDetailView.as_view(), name='user_profile'),
]
