# from django.urls import path
# from .views import (
#     EventListView, EventDetailView, EventCreateView,
#     EventUpdateView, EventDeleteView
# )

# urlpatterns = [
#     path('', EventListView.as_view(), name='event-list'),
#     path('create/', EventCreateView.as_view(), name='event-create'),
#     path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
#     path('<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
#     path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
#     # Category URLs
# path('categories/', CategoryListView.as_view(), name='category-list'),
# path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
# path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
# path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
# path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

# # Participant URLs
# path('participants/', ParticipantListView.as_view(), name='participant-list'),
# path('participants/create/', ParticipantCreateView.as_view(), name='participant-create'),
# path('participants/<int:pk>/', ParticipantDetailView.as_view(), name='participant-detail'),
# path('participants/<int:pk>/update/', ParticipantUpdateView.as_view(), name='participant-update'),
# path('participants/<int:pk>/delete/', ParticipantDeleteView.as_view(), name='participant-delete'),
# ]

# events/urls.py
from django.urls import path
from .views import (
    # Event Views
    EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView,
    # Category Views
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    
   
)
from . import views
from .views import UserListView
urlpatterns = [
    # Event URLs
    path('', EventListView.as_view(), name='event-list'),
    path('create/', EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),

    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    # # Participant URLs
    # path('participants/', ParticipantListView.as_view(), name='participant-list'),
    # path('participants/create/', ParticipantCreateView.as_view(), name='participant-create'),
    # path('participants/<int:pk>/', ParticipantDetailView.as_view(), name='participant-detail'),
    # path('participants/<int:pk>/update/', ParticipantUpdateView.as_view(), name='participant-update'),
    # path('participants/<int:pk>/delete/', ParticipantDeleteView.as_view(), name='participant-delete'),

   path('change-role/<int:user_id>/', views.change_user_role, name='change-role'),
   path('delete-participant/<int:user_id>/', views.delete_participant, name='delete-participant') ,

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view,  name='login'),
    path('logout/', views.logout_view, name='logout'),

    
    path('activate/<uidb64>/<token>/', views.activate_account, name='activate-account'),
    path('rsvp/<int:event_id>/', views.rsvp_event, name='rsvp-event'),
    path('dashboard/', views.participant_dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('users/', UserListView.as_view(), name='user-list'),
]