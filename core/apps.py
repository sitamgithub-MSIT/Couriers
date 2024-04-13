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

    def ready(self):
        """
        Method called when the app is ready.

        This method is called when the app is ready. It imports the signals module
        to ensure that the signals are registered when the app is loaded.
        """
        import core.signals
