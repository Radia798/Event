from django.contrib import admin
from .models import Event, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'location', 'category')
    list_filter = ('category', 'date')

# @admin.register(User)
# class ParticipantAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email')
#     filter_horizontal = ('events',)
