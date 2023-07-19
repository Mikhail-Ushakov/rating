"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from rating import views
from registration.views import RegistrView, LoginView_, ProfileView, LogoutSystemView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:pk>/', views.RatingDetail.as_view(), name='detail'),
    path('forms/', views.SimpleView.as_view()),
    path('', views.RatingListView.as_view(), name='based'),
    path('registr/', RegistrView.as_view()),
    path('login/', LoginView_.as_view(), name='login'),
    path('accounts/profile/', ProfileView.as_view()),
    path('logout/', LogoutSystemView.as_view(), name='logout_path'),
]
