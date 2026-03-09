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
    # Participant Views
    ParticipantListView, ParticipantDetailView, ParticipantCreateView, ParticipantUpdateView, ParticipantDeleteView,
)

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

    # Participant URLs
    path('participants/', ParticipantListView.as_view(), name='participant-list'),
    path('participants/create/', ParticipantCreateView.as_view(), name='participant-create'),
    path('participants/<int:pk>/', ParticipantDetailView.as_view(), name='participant-detail'),
    path('participants/<int:pk>/update/', ParticipantUpdateView.as_view(), name='participant-update'),
    path('participants/<int:pk>/delete/', ParticipantDeleteView.as_view(), name='participant-delete'),
]