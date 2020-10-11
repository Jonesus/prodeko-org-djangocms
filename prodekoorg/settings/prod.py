import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration

from .base import *

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration(), RedisIntegration()],
    send_default_pii=True,
)

DEBUG = False
ALLOWED_HOSTS = ["prodeko.org", ".prodeko.org", "prodeko.fi", ".prodeko.fi"]

# When DEBUG = False, all errors with level ERROR or
# higher get mailed to ADMINS according to LOGGING conf
ADMINS = [("CTO", "cto@prodeko.org")]
# When DEBUG = False, all broken links get emailed to MANAGERS
MANAGERS = [("CTO", "cto@prodeko.org")]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME_DEFAULT,
        "USER": DB_USER,
        "PASSWORD": DB_PSWD,
        "HOST": "pgbouncer",
        "PORT": "5439",
        "CONN_MAX_AGE": 600,
        "DISABLE_SERVER_SIDE_CURSORS": True,
    }
}

INSTALLED_APPS += ("storages",)

CDN_URL = "static.prodeko.org"
AZURE_CUSTOM_DOMAIN = CDN_URL
AZURE_CACHE_CONTROL = "public,max-age=31536000,immutable"

DEFAULT_FILE_STORAGE = "prodekoorg.custom_azure.AzureMediaStorage"
STATICFILES_STORAGE = "prodekoorg.custom_azure.AzureStaticStorage"
THUMBNAIL_DEFAULT_STORAGE = "prodekoorg.custom_azure.AzureMediaStorage"

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

STATIC_URL = f"https://{CDN_URL}/{STATIC_LOCATION}/"
MEDIA_URL = f"https://{CDN_URL}/{MEDIA_LOCATION}/"

CKEDITOR_BASEPATH = f"https://{CDN_URL}/static/ckeditor/ckeditor/"

# Django filer config
FILER_STORAGES = {
    "public": {
        "main": {
            "ENGINE": "prodekoorg.custom_azure.AzureMediaStorage",
            "UPLOAD_TO": "filer.utils.generate_filename.by_date",
            "UPLOAD_TO_PREFIX": "public",
        },
        "thumbnails": {"ENGINE": "prodekoorg.custom_azure.AzureMediaStorage"},
    },
    "private": {
        "main": {
            "ENGINE": "prodekoorg.custom_azure.AzureMediaStorage",
            "UPLOAD_TO": "filer.utils.generate_filename.randomized",
            "UPLOAD_TO_PREFIX": "private",
        },
        "thumbnails": {"ENGINE": "prodekoorg.custom_azure.AzureMediaStorage"},
    },
}

# Loggin config. On DEBUG = FALSE, email ADMINS
# on ERROR (or higher) level events, otherwise log
# to standard output.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"},
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {"handlers": ["console", "mail_admins"], "level": "INFO"},
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
