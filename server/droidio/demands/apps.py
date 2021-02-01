from django.apps import AppConfig


class DemandsConfig(AppConfig):
    name = "droidio.demands"
    verbose_name = "Demands"

    def ready(self):
        try:
            import droidio.demands.signals  # noqa F401
        except ImportError:
            pass
