from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppTiedostotConfig(AppConfig):
    name = "prodekoorg.app_tiedostot"
    verbose_name = _("Files")
