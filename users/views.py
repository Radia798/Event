from django.shortcuts import render

from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import ProfileUpdateForm

class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'user_obj'

    def get_object(self):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('profile')