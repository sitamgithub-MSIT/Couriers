from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    """
    Sends a welcome email to new users.

    Args:
        sender: The sender of the signal.
        instance: The instance of the User model.
        created: A boolean indicating if the user was created.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """

    # Send the email if the user was created and has an email address
    if created and instance.email:

        # Render the email body
        body = render_to_string(
                "core/welcome_email.html", {"name": instance.get_full_name()}
            )

        send_mail(
            "Welcome to Couriers!",
            body,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )
