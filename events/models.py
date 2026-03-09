# from django.db import models
# from django.contrib.auth.models import User

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name

# class Event(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     date = models.DateField()
#     time = models.TimeField()
#     location = models.CharField(max_length=200)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')

#     def __str__(self):
#         return self.name

# class Participant(models.Model):
#     name = models.CharField(max_length=150)
#     email = models.EmailField()
#     events = models.ManyToManyField(Event, related_name='participants')

#     def __str__(self):
#         return self.name

# events/models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

# class Event(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     date = models.DateField()
#     time = models.TimeField()
#     location = models.CharField(max_length=200)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     participants = models.ManyToManyField(User, related_name='rsvped_events', blank=True)
#     image = models.ImageField(upload_to='events/', default='events/default.jpg', blank=True, null=True)

#     def __str__(self):
#         return self.name

# events/models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    
    # ManyToMany with User (RSVP system)
    participants = models.ManyToManyField(
        User, 
        related_name='rsvped_events', 
        blank=True
    )
    
    # Event image with default
    image = models.ImageField(
        upload_to='events/', 
        default='events/default.jpg', 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.name