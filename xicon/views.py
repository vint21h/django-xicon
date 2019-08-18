# -*- coding: utf-8 -*-

# django-xicon
# xicon/views.py


from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render_to_response

from xicon.settings import (
    ANDROID_CHROME_NAME,
    MSAPPLICATION_TILES,
    ANDROID_CHROME_ICONS,
    ANDROID_CHROME_DISPLAY,
    MSAPPLICATION_TILE_COLOR,
    ANDROID_CHROME_SHORT_NAME,
    ANDROID_CHROME_ORIENTATION,
    ANDROID_CHROME_THEME_COLOR,
    ANDROID_CHROME_BACKGROUND_COLOR,
)


__all__ = ["android_chrome_manifest", "msapplication_browserconfig"]  # type: list


def android_chrome_manifest(request: HttpRequest) -> JsonResponse:
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


def msapplication_browserconfig(request: HttpRequest) -> HttpResponse:
    """
    Render microsoft application browserconfig.xml.

    :param request: django HTTP request instance.
    :type request: django.http.HttpRequest.
    :return: rendered browserconfig.
    :rtype: django.http.HttpResponse.
    """

    context = {
        "MSAPPLICATION_TILE_COLOR": MSAPPLICATION_TILE_COLOR,
        "MSAPPLICATION_TILES": MSAPPLICATION_TILES,
    }  # type: dict

    return render_to_response(
        "xicon/browserconfig.xml", context=context, content_type="application/xml"
    )
