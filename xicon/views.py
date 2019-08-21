# -*- coding: utf-8 -*-

# django-xicon
# xicon/views.py


from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render_to_response

from xicon.conf import settings


__all__ = ["android_chrome_manifest", "msapplication_browserconfig"]  # type: list


def android_chrome_manifest(request: HttpRequest) -> JsonResponse:
    """
    Render android chrome manifest.json.

    :param request: django HTTP request instance.
    :type request: django.http.HttpRequest.
    :return: rendered manifest.
    :rtype: django.http.JsonResponse.
    """

    manifest = {}  # type: dict

    if settings.XICON_ANDROID_CHROME_NAME:
        manifest.update({"name": settings.XICON_ANDROID_CHROME_NAME})

    if settings.XICON_ANDROID_CHROME_SHORT_NAME:
        manifest.update({"short_name": settings.XICON_ANDROID_CHROME_SHORT_NAME})

    if settings.XICON_ANDROID_CHROME_ICONS:
        manifest.update({"icons": settings.XICON_ANDROID_CHROME_ICONS})

    if settings.XICON_ANDROID_CHROME_THEME_COLOR:
        manifest.update({"theme_color": settings.XICON_ANDROID_CHROME_THEME_COLOR})

    if settings.XICON_ANDROID_CHROME_BACKGROUND_COLOR:
        manifest.update(
            {"background_color": settings.XICON_ANDROID_CHROME_BACKGROUND_COLOR}
        )

    if settings.XICON_ANDROID_CHROME_DISPLAY:
        manifest.update({"display": settings.XICON_ANDROID_CHROME_DISPLAY})

    if settings.XICON_ANDROID_CHROME_ORIENTATION:
        manifest.update({"orientation": settings.XICON_ANDROID_CHROME_ORIENTATION})

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
        "MSAPPLICATION_TILE_COLOR": settings.XICON_MSAPPLICATION_TILE_COLOR,
        "MSAPPLICATION_TILES": settings.XICON_MSAPPLICATION_TILES,
    }  # type: dict

    return render_to_response(
        "xicon/browserconfig.xml", context=context, content_type="application/xml"
    )
