# -*- coding: utf-8 -*-

# django-xicon
# xicon/conf.py


from typing import Dict, List, Iterable

from appconf import AppConf
from django.conf import settings


__all__: List[str] = ["settings"]


class DjangoXIconAppConf(AppConf):
    """Django X Icon settings."""

    FAVICONS: Iterable[Dict[str, str]] = getattr(settings, "XICON_FAVICONS", [])
    APPLE_TOUCH_ICONS: Iterable[Dict[str, str]] = getattr(
        settings, "XICON_APPLE_TOUCH_ICONS", []
    )
    APPLE_TOUCH_ICON_MASK_ICON_SRC: str = getattr(
        settings, "XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC", ""
    )
    APPLE_TOUCH_ICON_MASK_ICON_COLOR: str = getattr(
        settings, "XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR", ""
    )
    APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR: str = getattr(
        settings, "XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR", ""
    )
    APPLE_MOBILE_WEB_APP_TITLE: str = getattr(
        settings, "XICON_APPLE_MOBILE_WEB_APP_TITLE", ""
    )
    ANDROID_CHROME_THEME_COLOR: str = getattr(
        settings, "XICON_ANDROID_CHROME_THEME_COLOR", ""
    )
    ANDROID_CHROME_ICONS: Iterable[Dict[str, str]] = getattr(
        settings, "XICON_ANDROID_CHROME_ICONS", []
    )
    ANDROID_CHROME_NAME: str = getattr(settings, "XICON_ANDROID_CHROME_NAME", "")
    ANDROID_CHROME_SHORT_NAME: str = getattr(
        settings, "XICON_ANDROID_CHROME_SHORT_NAME", ""
    )
    ANDROID_CHROME_BACKGROUND_COLOR: str = getattr(
        settings, "XICON_ANDROID_CHROME_BACKGROUND_COLOR", ""
    )
    ANDROID_CHROME_DISPLAY: str = getattr(settings, "XICON_ANDROID_CHROME_DISPLAY", "")
    ANDROID_CHROME_ORIENTATION: str = getattr(
        settings, "XICON_ANDROID_CHROME_ORIENTATION", ""
    )
    MSAPPLICATION_NAME: str = getattr(settings, "XICON_MSAPPLICATION_NAME", "")
    MSAPPLICATION_TILE_COLOR: str = getattr(
        settings, "XICON_MSAPPLICATION_TILE_COLOR", ""
    )
    MSAPPLICATION_TILES: Iterable[Dict[str, str]] = getattr(
        settings, "XICON_MSAPPLICATION_TILES", []
    )

    class Meta:
        """Config settings."""

        prefix: str = "xicon"
