# -*- coding: utf-8 -*-

# django-xicon
# tests/urls.py


from typing import List, Union

from django.urls import re_path
from django.urls.resolvers import URLPattern, URLResolver

from xicon.views import android_chrome_manifest, msapplication_browserconfig


__all__: List[str] = ["urlpatterns"]


# django-xicon urls
urlpatterns: List[Union[URLPattern, URLResolver]] = [
    re_path(
        r"^manifest\.json$", android_chrome_manifest, name="android-chrome-manifest"
    ),  # android chrome manifest.json
    re_path(
        r"^browserconfig\.xml$",
        msapplication_browserconfig,
        name="msapplication-browserconfig",
    ),  # microsoft application browserconfig.xml
]
