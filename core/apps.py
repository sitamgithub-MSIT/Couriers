from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    AppConfig for the 'core' app.

    This class represents the configuration for the 'core' app in Django.
    It sets the default auto field to 'django.db.models.BigAutoField'
    and specifies the name of the app as 'core'.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
