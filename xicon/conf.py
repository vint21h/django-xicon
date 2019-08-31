# -*- coding: utf-8 -*-

# django-xicon
# xicon/conf.py


from typing import Dict, List, Iterable  # pylint: disable=W0611

from appconf import AppConf
from django.conf import settings


__all__ = ["settings"]  # type: List[str]


class DjangoXIconAppConf(AppConf):
    """
    Django X Icon settings.
    """

    FAVICONS = getattr(settings, "XICON_FAVICONS", [])  # type: Iterable[Dict[str, str]]
    APPLE_TOUCH_ICONS = getattr(
        settings, "XICON_APPLE_TOUCH_ICONS", []
    )  # type: Iterable[Dict[str, str]]
    APPLE_TOUCH_ICON_MASK_ICON_SRC = getattr(
        settings, "XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC", ""
    )  # type: str
    APPLE_TOUCH_ICON_MASK_ICON_COLOR = getattr(
        settings, "XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR", ""
    )  # type: str
    APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR = getattr(
        settings, "XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR", ""
    )  # type: str
    APPLE_MOBILE_WEB_APP_TITLE = getattr(
        settings, "XICON_APPLE_MOBILE_WEB_APP_TITLE", ""
    )  # type: str
    ANDROID_CHROME_THEME_COLOR = getattr(
        settings, "XICON_ANDROID_CHROME_THEME_COLOR", ""
    )  # type: str
    ANDROID_CHROME_ICONS = getattr(
        settings, "XICON_ANDROID_CHROME_ICONS", []
    )  # type: Iterable[Dict[str, str]]
    ANDROID_CHROME_NAME = getattr(
        settings, "XICON_ANDROID_CHROME_NAME", ""
    )  # type: str
    ANDROID_CHROME_SHORT_NAME = getattr(
        settings, "XICON_ANDROID_CHROME_SHORT_NAME", ""
    )  # type: str
    ANDROID_CHROME_BACKGROUND_COLOR = getattr(
        settings, "XICON_ANDROID_CHROME_BACKGROUND_COLOR", ""
    )  # type: str
    ANDROID_CHROME_DISPLAY = getattr(
        settings, "XICON_ANDROID_CHROME_DISPLAY", ""
    )  # type: str
    ANDROID_CHROME_ORIENTATION = getattr(
        settings, "XICON_ANDROID_CHROME_ORIENTATION", ""
    )  # type: str
    MSAPPLICATION_NAME = getattr(settings, "XICON_MSAPPLICATION_NAME", "")  # type: str
    MSAPPLICATION_TILE_COLOR = getattr(
        settings, "XICON_MSAPPLICATION_TILE_COLOR", ""
    )  # type: str
    MSAPPLICATION_TILES = getattr(
        settings, "XICON_MSAPPLICATION_TILES", []
    )  # type: Iterable[Dict[str, str]]

    class Meta:

        prefix = "xicon"  # type: str
