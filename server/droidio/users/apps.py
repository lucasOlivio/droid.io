from django.apps import AppConfig


class UsersConfig(AppConfig):
    """ App configuration for users app
    """

    name = "droidio.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import droidio.users.signals  # noqa F401
        except ImportError:
            pass
