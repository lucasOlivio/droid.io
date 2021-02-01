from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DemandConfig(AppConfig):
    name = "droidio.demands"
    verbose_name = _("Demands")

    def ready(self):
        try:
            import droidio.demands.signals  # noqa F401
        except ImportError:
            pass
