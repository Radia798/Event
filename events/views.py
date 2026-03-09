# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .models import Event, Participant, Category
# from .forms import EventForm, ParticipantForm, CategoryForm
# from django.urls import reverse_lazy
# from django.db.models import Count, Q
# from datetime import date
# from django.contrib.auth.models import User, Group
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# # Event Views
# class EventListView(ListView):
#     model = Event
#     template_name = 'events/event_list.html'
#     context_object_name = 'events'

#     def get_queryset(self):
#         queryset = Event.objects.select_related('category').prefetch_related('participants')
#         search = self.request.GET.get('search')
#         if search:
#             queryset = queryset.filter(Q(name__icontains=search) | Q(location__icontains=search))
#         return queryset

# class EventDetailView(DetailView):
#     model = Event
#     template_name = 'events/event_detail.html'
#     context_object_name = 'event'

# class EventCreateView(CreateView):
#     model = Event
#     form_class = EventForm
#     template_name = 'events/event_form.html'
#     success_url = reverse_lazy('event-list')

# class EventUpdateView(UpdateView):
#     model = Event
#     form_class = EventForm
#     template_name = 'events/event_form.html'
#     success_url = reverse_lazy('event-list')

# class EventDeleteView(DeleteView):
#     model = Event
#     template_name = 'events/event_confirm_delete.html'
#     success_url = reverse_lazy('event-list')

# # Similar Views for Participant and Category

# class CategoryListView(ListView):
#     model = Category
#     template_name = 'events/category_list.html'
#     context_object_name = 'categories'

# class CategoryDetailView(DetailView):
#     model = Category
#     template_name = 'events/category_detail.html'
#     context_object_name = 'category'

# class CategoryCreateView(CreateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'events/category_form.html'
#     success_url = reverse_lazy('category-list')

# class CategoryUpdateView(UpdateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'events/category_form.html'
#     success_url = reverse_lazy('category-list')

# class CategoryDeleteView(DeleteView):
#     model = Category
#     template_name = 'events/category_confirm_delete.html'
#     success_url = reverse_lazy('category-list')


# class ParticipantListView(ListView):
#     model = Participant
#     template_name = 'events/participant_list.html'
#     context_object_name = 'participants'

#     def get_queryset(self):
#         # Prefetch events for optimization
#         return Participant.objects.prefetch_related('events').all()

# class ParticipantDetailView(DetailView):
#     model = Participant
#     template_name = 'events/participant_detail.html'
#     context_object_name = 'participant'

# class ParticipantCreateView(CreateView):
#     model = Participant
#     form_class = ParticipantForm
#     template_name = 'events/participant_form.html'
#     success_url = reverse_lazy('participant-list')

# class ParticipantUpdateView(UpdateView):
#     model = Participant
#     form_class = ParticipantForm
#     template_name = 'events/participant_form.html'
#     success_url = reverse_lazy('participant-list')

# class ParticipantDeleteView(DeleteView):
#     model = Participant
#     template_name = 'events/participant_confirm_delete.html'
#     success_url = reverse_lazy('participant-list')



# # Dashboard View
# from django.views import View

# class DashboardView(View):
#     template_name = 'dashboard.html'

#     def get(self, request):
#         today = date.today()

#         # Total participants
#         total_participants = Participant.objects.count()

#         # Total events
#         total_events = Event.objects.count()

#         # Upcoming events
#         upcoming_events = Event.objects.filter(date__gte=today).count()

#         # Past events
#         past_events = Event.objects.filter(date__lt=today).count()

#         # Today's events
#         todays_events = Event.objects.filter(date=today).select_related('category')

#         context = {
#             'total_participants': total_participants,
#             'total_events': total_events,
#             'upcoming_events': upcoming_events,
#             'past_events': past_events,
#             'todays_events': todays_events,
#         }
#         return render(request, self.template_name, context)
    

# def signup_view(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         password = request.POST['password']

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists")
#             return redirect('signup')

#         user = User.objects.create_user(username=username, email=email, password=password,
#                                         first_name=first_name, last_name=last_name)
#         # Default role: Participant
#         participant_group, _ = Group.objects.get_or_create(name='Participant')
#         user.groups.add(participant_group)
#         user.is_active = False  # Will activate via email
#         user.save()

#         messages.success(request, "Account created! Please check your email to activate your account.")
#         return redirect('login')

#     return render(request, 'events/signup.html')


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 # Redirect based on role
#                 if user.groups.filter(name='Admin').exists():
#                     return redirect('admin-dashboard')
#                 elif user.groups.filter(name='Organizer').exists():
#                     return redirect('organizer-dashboard')
#                 else:
#                     return redirect('participant-dashboard')
#             else:
#                 messages.error(request, "Account not activated. Check your email.")
#                 return redirect('login')
#         else:
#             messages.error(request, "Invalid credentials")
#             return redirect('login')

#     return render(request, 'events/login.html')


# def logout_view(request):
#     logout(request)
#     return redirect('login')

# from .decorators import role_required

# @role_required('Organizer')
# def create_event(request):
#     # Only organizers can create events
#     pass

# @role_required('Admin')
# def delete_participant(request, pk):
#     # Only admin can delete participants
#     pass


# # events/views.py
# from django.contrib.auth.models import User, Group
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.core.mail import send_mail
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
# from django.template.loader import render_to_string

# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         password = request.POST['password']

#         user = User.objects.create_user(username=username, email=email,
#                                         first_name=first_name, last_name=last_name,
#                                         password=password, is_active=False)

#         # Assign participant role
#         participant_group, _ = Group.objects.get_or_create(name='Participant')
#         user.groups.add(participant_group)

#         # Send activation email
#         uid = urlsafe_base64_encode(force_bytes(user.pk))
#         token = default_token_generator.make_token(user)
#         activation_link = request.build_absolute_uri(f'/activate/{uid}/{token}/')
#         message = render_to_string('events/activation_email.html', {'activation_link': activation_link, 'user': user})

#         send_mail(
#             'Activate Your Account',
#             message,
#             'noreply@example.com',
#             [user.email],
#         )

#         messages.success(request, "Signup successful! Check your email to activate your account.")
#         return redirect('login')

#     return render(request, 'events/signup.html')

# # events/views.py
# from django.utils.http import urlsafe_base64_decode
# from django.utils.encoding import force_str
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib import messages

# def activate_account(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except:
#         user = None

#     if user and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(request, "Account activated! You can now login.")
#         return redirect('login')
#     else:
#         messages.error(request, "Activation link invalid")
#         return redirect('signup')
    
# # events/views.py
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404, redirect
# from django.contrib import messages
# from django.core.mail import send_mail
# from .models import Event

# @login_required
# def rsvp_event(request, event_id):
#     event = get_object_or_404(Event, pk=event_id)
#     if request.user in event.participants.all():
#         messages.info(request, "You already RSVPed for this event.")
#     else:
#         event.participants.add(request.user)
#         messages.success(request, "RSVP successful! Confirmation email sent.")

#         # Send confirmation email
#         send_mail(
#             subject=f"RSVP Confirmation: {event.name}",
#             message=f"Hi {request.user.first_name}, you have successfully RSVPed to {event.name}.",
#             from_email="noreply@example.com",
#             recipient_list=[request.user.email],
#         )

#     return redirect('participant-dashboard')

# # events/views.py
# from django.contrib.auth.decorators import login_required

# @login_required
# def participant_dashboard(request):
#     rsvped_events = request.user.rsvped_events.all()
#     return render(request, 'events/participant_dashboard.html', {'rsvped_events': rsvped_events})

# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.models import User
# from django.utils import timezone
# from .models import Event

# def admin_check(user):
#     return user.groups.filter(name='Admin').exists() or user.is_superuser

# @user_passes_test(admin_check)
# def admin_dashboard(request):
#     today = timezone.now().date()
#     total_events = Event.objects.count()
#     upcoming_events = Event.objects.filter(date__gte=today).count()
#     past_events = Event.objects.filter(date__lt=today).count()
#     total_participants = User.objects.filter(groups__name='Participant').count()
#     participants = User.objects.filter(groups__name='Participant')

#     context = {
#         'total_events': total_events,
#         'upcoming_events': upcoming_events,
#         'past_events': past_events,
#         'total_participants': total_participants,
#         'participants': participants,
#     }
#     return render(request, 'events/admin_dashboard.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event, Category
from .forms import EventForm, CategoryForm
from django.urls import reverse_lazy
from django.db.models import Q
from datetime import date
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from .decorators import role_required
from django.utils import timezone
from django.utils.decorators import method_decorator


# ------------------------
# EVENT VIEWS
# ------------------------
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

@method_decorator(role_required('Organizer'), name='dispatch')
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event-list')

@method_decorator(role_required('Organizer'), name='dispatch')
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event-list')
@method_decorator(role_required('Organizer'), name='dispatch')
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')

# ------------------------
# CATEGORY VIEWS
# ------------------------
class CategoryListView(ListView):
    model = Category
    template_name = 'events/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'events/category_detail.html'
    context_object_name = 'category'

@method_decorator(role_required('Organizer'), name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'
    success_url = reverse_lazy('category-list')

@method_decorator(role_required('Organizer'), name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'
    success_url = reverse_lazy('category-list')

@method_decorator(role_required('Organizer'), name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'events/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')

# ------------------------
# DASHBOARD VIEW
# ------------------------
class DashboardView(ListView):
    template_name = 'dashboard.html'

    def get(self, request):
        today = date.today()

        # Total participants
        total_participants = User.objects.filter(groups__name='Participant').count()

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

# ------------------------
# AUTHENTICATION
# ------------------------
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_active=False
        )

        # Assign default role: Participant
        participant_group, _ = Group.objects.get_or_create(name='Participant')
        user.groups.add(participant_group)

        # Send activation email
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        activation_link = request.build_absolute_uri(f'/activate/{uid}/{token}/')
        message = render_to_string('events/activation_email.html', {'activation_link': activation_link, 'user': user})

        send_mail(
            'Activate Your Account',
            message,
            'noreply@example.com',
            [user.email],
        )

        messages.success(request, "Signup successful! Check your email to activate your account.")
        return redirect('login')

    return render(request, 'events/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect based on role
                if user.groups.filter(name='Admin').exists():
                    return redirect('admin-dashboard')
                elif user.groups.filter(name='Organizer').exists():
                    return redirect('organizer-dashboard')
                else:
                    return redirect('dashboard')
            else:
                messages.error(request, "Account not activated. Check your email.")
        else:
            messages.error(request, "Invalid credentials")
        return redirect('login')

    return render(request, 'events/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Account activated! You can now login.")
        return redirect('login')
    else:
        messages.error(request, "Activation link invalid")
        return redirect('signup')

# ------------------------
# RSVP
# ------------------------
@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.user in event.participants.all():
        messages.info(request, "You already RSVPed for this event.")
    else:
        event.participants.add(request.user)
        messages.success(request, "RSVP successful! Confirmation email sent.")

        # Send confirmation email
        send_mail(
            subject=f"RSVP Confirmation: {event.name}",
            message=f"Hi {request.user.first_name}, you have successfully RSVPed to {event.name}.",
            from_email="noreply@example.com",
            recipient_list=[request.user.email],
        )

    return redirect('participant-dashboard')


@login_required
def participant_dashboard(request):
    rsvped_events = request.user.rsvped_events.all()
    return render(request, 'events/participant_dashboard.html', {'rsvped_events': rsvped_events})

# ------------------------
# ADMIN DASHBOARD & MANAGEMENT
# ------------------------
def admin_check(user):
    return user.groups.filter(name='Admin').exists() or user.is_superuser

@user_passes_test(admin_check)
def admin_dashboard(request):
    today = timezone.now().date()
    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(date__gte=today).count()
    past_events = Event.objects.filter(date__lt=today).count()
    total_participants = User.objects.filter(groups__name='Participant').count()
    participants = User.objects.filter(groups__name='Participant')

    context = {
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'total_participants': total_participants,
        'participants': participants,
    }
    return render(request, 'events/admin_dashboard.html', context)


@user_passes_test(admin_check)
def change_user_role(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        role = request.POST.get('role')  # 'Admin', 'Organizer', 'Participant'
        for g in user.groups.all():
            user.groups.remove(g)
        group, _ = Group.objects.get_or_create(name=role)
        user.groups.add(group)
        messages.success(request, f"{user.username}'s role changed to {role}.")
        return redirect('admin-dashboard')
    return render(request, 'events/change_role.html', {'user': user})


@user_passes_test(admin_check)
def delete_participant(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "Participant deleted successfully.")
        return redirect('admin-dashboard')
    return render(request, 'events/delete_participant.html', {'user': user})

from django.contrib.auth.models import User
from django.views.generic import ListView

class UserListView(ListView):
    model = User
    template_name = 'events/user_list.html'  # create this template
    context_object_name = 'users'