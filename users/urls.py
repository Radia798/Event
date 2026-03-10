from django.urls import path
from .views import ProfileView, ProfileUpdateView, CustomPasswordChangeView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit-profile'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change-password'),
]