# -*- coding: utf-8 -*-

# django-xicon
# xicon/templatetags/xicon_tags.py


from typing import Dict, List, Iterable

from django import template

from xicon.conf import settings


__all__: List[str] = [
    "xicon_favicon",
    "xicon_favicons",
    "xicon_apple_touch_icon",
    "xicon_apple_touch_icons",
    "xicon_apple_touch_icon_mask_icon",
    "xicon_apple_mobile_web_app_status_bar_style",
    "xicon_apple_mobile_web_app_title",
    "xicon_android_chrome_theme_color",
    "xicon_msapplication_name",
    "xicon_msapplication_tile_color",
    "xicon_mstile",
    "xicon_mstiles",
]


register = template.Library()


@register.inclusion_tag("xicon/templatetags/xicon_favicon.html")
def xicon_favicon(favicon: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    """
    Render classic favicon meta tag.

    :param favicon: dict containing favicon settings
    :type favicon: Dict[str, str]
    :return: favicon
    :rtype: Dict[str, Dict[str, str]]
    """
    return {"XICON_FAVICON": favicon}


@register.inclusion_tag("xicon/templatetags/xicon_favicons.html")
def xicon_favicons() -> Dict[str, Iterable[Dict[str, str]]]:
    """
    Render classic favicon meta tags.

    :return: favicons
    :rtype: Dict[str, Iterable[Dict[str, str]]]
    """
    return {"XICON_FAVICONS": settings.XICON_FAVICONS}


@register.inclusion_tag("xicon/templatetags/xicon_apple_touch_icon.html")
def xicon_apple_touch_icon(
    apple_touch_icon: Dict[str, str]
) -> Dict[str, Dict[str, str]]:
    """
    Render apple touch icon meta tag.

    :param apple_touch_icon: dict containing apple touch icon settings
    :type apple_touch_icon: Dict[str, str]
    :return: apple touch icon
    :rtype: Dict[str, Dict[str, str]]
    """
    return {"XICON_APPLE_TOUCH_ICON": apple_touch_icon}


@register.inclusion_tag("xicon/templatetags/xicon_apple_touch_icons.html")
def xicon_apple_touch_icons() -> Dict[str, Iterable[Dict[str, str]]]:
    """
    Render apple touch icon meta tags.

    :return: apple touch icons
    :rtype: Dict[str, Iterable[Dict[str, str]]]
    """
    return {"XICON_APPLE_TOUCH_ICONS": settings.XICON_APPLE_TOUCH_ICONS}


@register.inclusion_tag("xicon/templatetags/xicon_apple_touch_icon_mask_icon.html")
def xicon_apple_touch_icon_mask_icon() -> Dict[str, str]:
    """
    Render apple touch icon mask icon meta tag.

    :return: mask icon
    :rtype: Dict[str, str]
    """
    return {
        "XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC": settings.XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC,  # noqa: E501
        "XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR": settings.XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR,  # noqa: E501
    }


@register.inclusion_tag(
    "xicon/templatetags/xicon_apple_mobile_web_app_status_bar_style.html"
)
def xicon_apple_mobile_web_app_status_bar_style() -> Dict[str, str]:
    """
    Render apple mobile web application status bar style color meta tag.

    :return: web app status bar style
    :rtype: Dict[str, str]
    """
    return {
        "XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR": settings.XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR  # noqa: E501
    }


@register.inclusion_tag("xicon/templatetags/xicon_apple_mobile_web_app_title.html")
def xicon_apple_mobile_web_app_title() -> Dict[str, str]:
    """
    Render apple mobile web application title meta tag.

    :return: web app title
    :rtype: Dict[str, str]
    """
    return {
        "XICON_APPLE_MOBILE_WEB_APP_TITLE": settings.XICON_APPLE_MOBILE_WEB_APP_TITLE
    }


@register.inclusion_tag("xicon/templatetags/xicon_android_chrome_theme_color.html")
def xicon_android_chrome_theme_color() -> Dict[str, str]:
    """
    Render android chrome theme color meta tag.

    :return: theme color
    :rtype: Dict[str, str]
    """
    return {
        "XICON_ANDROID_CHROME_THEME_COLOR": settings.XICON_ANDROID_CHROME_THEME_COLOR
    }


@register.inclusion_tag("xicon/templatetags/xicon_msapplication_name.html")
def xicon_msapplication_name() -> Dict[str, str]:
    """
    Render microsoft application name meta tag.

    :return: application name
    :rtype: Dict[str, str]
    """
    return {"XICON_MSAPPLICATION_NAME": settings.XICON_MSAPPLICATION_NAME}


@register.inclusion_tag("xicon/templatetags/xicon_msapplication_tile_color.html")
def xicon_msapplication_tile_color() -> Dict[str, str]:
    """
    Render microsoft application tile color meta tag.

    :return: tile color
    :rtype: Dict[str, str]
    """
    return {"XICON_MSAPPLICATION_TILE_COLOR": settings.XICON_MSAPPLICATION_TILE_COLOR}


@register.inclusion_tag("xicon/templatetags/xicon_mstile.html")
def xicon_mstile(mstile: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    """
    Render msapplication tile meta tag.

    :param mstile: dict containing tile settings
    :type mstile: Dict[str, str]
    :return: tile
    :rtype: Dict[str, Dict[str, str]]
    """
    return {"XICON_MSTILE": mstile}


@register.inclusion_tag("xicon/templatetags/xicon_mstiles.html")
def xicon_mstiles() -> Dict[str, Iterable[Dict[str, str]]]:
    """
    Render msapplication tiles meta tags.

    :return: tiles
    :rtype: Dict[str, Iterable[Dict[str, str]]]
    """
    return {"XICON_MSAPPLICATION_TILES": settings.XICON_MSAPPLICATION_TILES}
