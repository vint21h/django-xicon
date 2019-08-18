# -*- coding: utf-8 -*-

# django-xicon
# xicon/settings.py


from typing import Dict, Union, Iterable

from django.conf import settings


__all__ = [
    "FAVICONS",
    "APPLE_TOUCH_ICONS",
    "APPLE_TOUCH_ICON_MASK_ICON_SRC",
    "APPLE_TOUCH_ICON_MASK_ICON_COLOR",
    "APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR",
    "APPLE_MOBILE_WEB_APP_TITLE",
    "ANDROID_CHROME_THEME_COLOR",
    "ANDROID_CHROME_ICONS",
    "ANDROID_CHROME_NAME",
    "ANDROID_CHROME_SHORT_NAME",
    "ANDROID_CHROME_BACKGROUND_COLOR",
    "ANDROID_CHROME_DISPLAY",
    "ANDROID_CHROME_ORIENTATION",
]  # type: list


FAVICONS = getattr(
    settings, "XICON_FAVICONS", []
)  # type: Iterable[Dict[str, Union[str, Dict[str, int], None]]]
APPLE_TOUCH_ICONS = getattr(
    settings, "XICON_APPLE_TOUCH_ICONS", []
)  # type: Iterable[Dict[str, Union[str, Dict[str, int], None]]]
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
)  # type: Iterable[Dict[str, Union[str, Dict[str, int], None]]]
ANDROID_CHROME_NAME = getattr(settings, "XICON_ANDROID_CHROME_NAME", "")  # type: str
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
