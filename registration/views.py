from typing import Any, Dict
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .forms import RegistrForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rating.models import Rate

class RegistrView(CreateView):
    form_class = RegistrForm
    success_url = reverse_lazy('based')
    template_name = 'registration/register.html'

class LoginView_(LoginView):
    template_name = 'registration/login.html'

@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    template_name = 'registration/profile.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        self.user_object = self.get_object()
        users_rate = Rate.objects.filter(user=self.user_object.id)
        kwargs['users_rate'] = users_rate
        return super().get_context_data(**kwargs)
    def get_object(self):
        return get_object_or_404(get_user_model(), username=self.request.user.username)
    
class LogoutSystemView(LogoutView):
    pass