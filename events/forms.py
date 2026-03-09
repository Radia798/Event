from django import forms
from .models import Event, Category

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'border p-2 rounded'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'border p-2 rounded'}),
            'description': forms.Textarea(attrs={'class': 'border p-2 rounded'}),
        }

# class ParticipantForm(forms.ModelForm):
#     class Meta:
#         model = Participant
#         fields = '__all__'
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'border p-2 rounded'}),
#             'email': forms.EmailInput(attrs={'class': 'border p-2 rounded'}),
#             'events': forms.SelectMultiple(attrs={'class': 'border p-2 rounded'}),
#         }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border p-2 rounded'}),
            'description': forms.Textarea(attrs={'class': 'border p-2 rounded'}),
        }