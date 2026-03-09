from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event, Participant, Category
from .forms import EventForm, ParticipantForm, CategoryForm
from django.urls import reverse_lazy
from django.db.models import Count, Q
from datetime import date
from django.utils import timezone
from django.db.models import Count

# Event Views
class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Event.objects.select_related('category').prefetch_related('participants')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(location__icontains=search))
        return queryset

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event-list')

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event-list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')

# Similar Views for Participant and Category

class CategoryListView(ListView):
    model = Category
    template_name = 'events/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'events/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'events/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')


class ParticipantListView(ListView):
    model = Participant
    template_name = 'events/participant_list.html'
    context_object_name = 'participants'

    def get_queryset(self):
        # Prefetch events for optimization
        return Participant.objects.prefetch_related('events').all()

class ParticipantDetailView(DetailView):
    model = Participant
    template_name = 'events/participant_detail.html'
    context_object_name = 'participant'

class ParticipantCreateView(CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'events/participant_form.html'
    success_url = reverse_lazy('participant-list')

class ParticipantUpdateView(UpdateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'events/participant_form.html'
    success_url = reverse_lazy('participant-list')

class ParticipantDeleteView(DeleteView):
    model = Participant
    template_name = 'events/participant_confirm_delete.html'
    success_url = reverse_lazy('participant-list')



# Dashboard View
from django.views import View

class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request):
        today = date.today()

        # Total participants
        total_participants = Participant.objects.count()

        # Total events
        total_events = Event.objects.count()

        # Upcoming events
        upcoming_events = Event.objects.filter(date__gte=today).count()

        # Past events
        past_events = Event.objects.filter(date__lt=today).count()

        # Today's events
        todays_events = Event.objects.filter(date=today).select_related('category')

        context = {
            'total_participants': total_participants,
            'total_events': total_events,
            'upcoming_events': upcoming_events,
            'past_events': past_events,
            'todays_events': todays_events,
        }
        return render(request, self.template_name, context)