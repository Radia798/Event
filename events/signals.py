from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Event

# Send email when a user RSVPs
@receiver(m2m_changed, sender=Event.participants.through)
def send_rsvp_email(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for user_id in pk_set:
            user = User.objects.get(pk=user_id)
            send_mail(
                f'RSVP Confirmation: {instance.name}',
                f'Hi {user.first_name}, you have successfully RSVPed to {instance.name}.',
                'noreply@example.com',
                [user.email],
            )