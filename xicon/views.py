# -*- coding: utf-8 -*-

# django-xicon
# xicon/views.py


from django.http import JsonResponse

from xicon.settings import (
    ANDROID_CHROME_NAME,
    ANDROID_CHROME_ICONS,
    ANDROID_CHROME_DISPLAY,
    ANDROID_CHROME_SHORT_NAME,
    ANDROID_CHROME_ORIENTATION,
    ANDROID_CHROME_THEME_COLOR,
    ANDROID_CHROME_BACKGROUND_COLOR,
)


__all__ = ["android_chrome_manifest"]  # type: list


def android_chrome_manifest(request):
    """
    Render android chrome manifest.json.

    :param request: django HTTP request instance.
    :type request: django.http.HttpRequest.
    :return: rendered manifest.
    :rtype: django.htp.JsonResponse.
    """

    manifest = {}  # type: dict

    if ANDROID_CHROME_NAME:
        manifest.update({"name": ANDROID_CHROME_NAME})

    if ANDROID_CHROME_SHORT_NAME:
        manifest.update({"short_name": ANDROID_CHROME_SHORT_NAME})

    if ANDROID_CHROME_ICONS:
        manifest.update({"icons": ANDROID_CHROME_ICONS})

    if ANDROID_CHROME_THEME_COLOR:
        manifest.update({"theme_color": ANDROID_CHROME_THEME_COLOR})

    if ANDROID_CHROME_BACKGROUND_COLOR:
        manifest.update({"background_color": ANDROID_CHROME_BACKGROUND_COLOR})

    if ANDROID_CHROME_DISPLAY:
        manifest.update({"display": ANDROID_CHROME_DISPLAY})

    if ANDROID_CHROME_ORIENTATION:
        manifest.update({"orientation": ANDROID_CHROME_ORIENTATION})

    return JsonResponse(manifest)
