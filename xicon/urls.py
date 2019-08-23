# -*- coding: utf-8 -*-

# django-xicon
# tests/urls.py


from django.conf.urls import url

from xicon.views import android_chrome_manifest, msapplication_browserconfig


__all__ = ["urlpatterns"]  # type: list


# django-xicon urls
urlpatterns = [
    url(
        r"^manifest\.json$", android_chrome_manifest, name="android-chrome-manifest"
    ),  # android chrome manifest.json
    url(
        r"^browserconfig\.xml$",
        msapplication_browserconfig,
        name="msapplication-browserconfig",
    ),  # microsoft application browserconfig.xml
]  # type: list
