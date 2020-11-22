# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve


def get_version():
    # Increment this when javascript translations change
    version = 1
    return version


handler500 = "prodekoorg.views.handler500"

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="misc/robots.txt", content_type="text/plain"
        ),
        name="robots_file",
    ),
    path(
        "browserconfig.xml",
        TemplateView.as_view(
            template_name="misc/browserconfig.xml", content_type="text/xml"
        ),
        name="browserconfig_file",
    ),
]

# Django filer
urlpatterns += [path("", include("filer.server.urls"))]

# Localization and internationalization
urlpatterns += i18n_patterns(
    path(
        "jsi18n/",
        cache_page(86400, key_prefix="js18n-%s" % get_version())(
            JavaScriptCatalog.as_view()
        ),
        name="javascript-catalog",
    ),
    # auth_prodeko
    path("", include("auth_prodeko.urls")),
    # app_infoscreen
    path("infoscreen/", include("prodekoorg.app_infoscreen.urls")),
    # tiedotteet.prodeko.org
    path(_("weekly-bulletin/"), include("tiedotteet.backend.urls")),
    # matrikkeli.prodeko.org
    path(_("matrikkeli/"), include("alumnirekisteri.rekisteri.urls")),
    # Misc
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("cms.urls")),
)

# This is only needed when using runserver.
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = (
        [
            re_path(
                r"^media/(?P<path>.*)$",
                serve,
                {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
            ),
            path("__debug__/", include(debug_toolbar.urls)),
        ]
        + staticfiles_urlpatterns()
        + urlpatterns
    )
