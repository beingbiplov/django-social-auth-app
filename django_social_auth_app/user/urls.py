from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', LogoutView.as_view(), name='logout'),
]