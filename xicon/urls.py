# -*- coding: utf-8 -*-

# django-xicon
# tests/urls.py


from typing import List, Union  # pylint: disable=W0611

from django.urls import re_path
from django.urls.resolvers import URLPattern, URLResolver  # pylint: disable=W0611

from xicon.views import android_chrome_manifest, msapplication_browserconfig


__all__ = ["urlpatterns"]  # type: List[str]


# django-xicon urls
urlpatterns = [
    re_path(
        r"^manifest\.json$", android_chrome_manifest, name="android-chrome-manifest"
    ),  # android chrome manifest.json
    re_path(
        r"^browserconfig\.xml$",
        msapplication_browserconfig,
        name="msapplication-browserconfig",
    ),  # microsoft application browserconfig.xml
]  # type: List[Union[URLPattern, URLResolver]]
