"""django_social_auth_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('django_social_auth_app.core.urls') ),

    path(r'repo/', include('django_social_auth_app.repository.urls')),
    
    path(r'user/', include('django_social_auth_app.user.urls')),

    path(r'oauth/', include('social_django.urls', namespace='social')),
    path(r'select2/', include('django_select2.urls')),
]
