# -*- coding: utf-8 -*-

# django-xicon
# xicon/settings.py


from typing import Dict, Union, Iterable

from django.conf import settings


__all__ = [
    "FAVICONS",
    "APPLE_TOUCH_ICONS",
    "APPLE_TOUCH_ICON_MASK_COLOR",
    "APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR",
    "APPLE_MOBILE_WEB_APP_TITLE",
]  # type: list


FAVICONS = getattr(
    settings, "XICON_FAVICONS", []
)  # type: Iterable[Dict[str, Union[str, Dict[str, int], None]]]
APPLE_TOUCH_ICONS = getattr(
    settings, "XICON_APPLE_TOUCH_ICONS", []
)  # type: Iterable[Dict[str, Union[str, Dict[str, int], None]]]
APPLE_TOUCH_ICON_MASK_COLOR = getattr(
    settings, "XICON_APPLE_TOUCH_ICON_MASK_COLOR", ""
)  # type: str
APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR = getattr(
    settings, "XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR", ""
)  # type: str
APPLE_MOBILE_WEB_APP_TITLE = getattr(
    settings, "XICON_APPLE_MOBILE_WEB_APP_TITLE", ""
)  # type: str
