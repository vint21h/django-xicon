# -*- coding: utf-8 -*-

# django-xicon
# xicon/urls.py

from django.conf.urls import url

from xicon.views import android_chrome_manifest


__all__ = ["urlpatterns"]  # type: list


# django-xicon urls
urlpatterns = [
    url(
        r"^manifest\.json$", android_chrome_manifest, name="android-chrome-manifest"
    )  # android chrome manifest.jsn
]  # type: list
