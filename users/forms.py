from django import forms
from .models import CustomUser

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'profile_picture'
        ]