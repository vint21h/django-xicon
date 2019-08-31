# -*- coding: utf-8 -*-

# django-xicon
# xicon/templatetags/xicon_tags.py


from typing import Dict

from django import template

from xicon.conf import settings


__all__ = [
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
]  # type: list


register = template.Library()


@register.inclusion_tag("xicon/templatetags/xicon_favicon.html")
def xicon_favicon(favicon: Dict[str, Dict[str, str]]) -> dict:
    """
    Render classic favicon meta tag.

    :param favicon: dict containing favicon settings.
    :type favicon: Dict[str, str].
    :return: favicon.
    :rtype: dict.
    """

    return {"XICON_FAVICON": favicon}


@register.inclusion_tag("xicon/templatetags/xicon_favicons.html")
def xicon_favicons() -> dict:
    """
    Render classic favicon meta tags.

    :return: favicons.
    :rtype: dict.
    """

    return {"XICON_FAVICONS": settings.XICON_FAVICONS}


@register.inclusion_tag("xicon/templatetags/xicon_apple_touch_icon.html")
def xicon_apple_touch_icon(apple_touch_icon: Dict[str, Dict[str, str]]) -> dict:
    """
    Render apple touch icon meta tag.

    :param apple_touch_icon: dict containing apple touch icon settings.
    :type apple_touch_icon: Dict[str, str].
    :return: apple touch icon.
    :rtype: dict.
    """

    return {"XICON_APPLE_TOUCH_ICON": apple_touch_icon}


@register.inclusion_tag("xicon/templatetags/xicon_apple_touch_icons.html")
def xicon_apple_touch_icons() -> dict:
    """
    Render apple touch icon meta tags.

    :return: apple touch icons.
    :rtype: dict.
    """

    return {"XICON_APPLE_TOUCH_ICONS": settings.XICON_APPLE_TOUCH_ICONS}


@register.inclusion_tag("xicon/templatetags/xicon_apple_touch_icon_mask_icon.html")
def xicon_apple_touch_icon_mask_icon() -> dict:
    """
    Render apple touch icon mask icon meta tag.

    :return: mask icon.
    :rtype: dict.
    """

    return {
        "XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC": settings.XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC,  # noqa: E501
        "XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR": settings.XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR,  # noqa: E501
    }


@register.inclusion_tag(
    "xicon/templatetags/xicon_apple_mobile_web_app_status_bar_style.html"
)
def xicon_apple_mobile_web_app_status_bar_style() -> dict:
    """
    Render apple mobile web application status bar style color meta tag.

    :return: web app status bar style.
    :rtype: dict.
    """

    return {
        "XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR": settings.XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR  # noqa: E501
    }


@register.inclusion_tag("xicon/templatetags/xicon_apple_mobile_web_app_title.html")
def xicon_apple_mobile_web_app_title() -> dict:
    """
    Render apple mobile web application title meta tag.

    :return: web app title.
    :rtype: dict.
    """

    return {
        "XICON_APPLE_MOBILE_WEB_APP_TITLE": settings.XICON_APPLE_MOBILE_WEB_APP_TITLE
    }


@register.inclusion_tag("xicon/templatetags/xicon_android_chrome_theme_color.html")
def xicon_android_chrome_theme_color() -> dict:
    """
    Render android chrome theme color meta tag.

    :return: theme color.
    :rtype: dict.
    """

    return {
        "XICON_ANDROID_CHROME_THEME_COLOR": settings.XICON_ANDROID_CHROME_THEME_COLOR
    }


@register.inclusion_tag(
    "xicon/templatetags/xicon_msapplication_name.html", takes_context=True
)
def xicon_msapplication_name(context: template.Context) -> template.Context:
    """
    Render microsoft application name meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update({"XICON_MSAPPLICATION_NAME": settings.XICON_MSAPPLICATION_NAME})

    return context


@register.inclusion_tag(
    "xicon/templatetags/xicon_msapplication_tile_color.html", takes_context=True
)
def xicon_msapplication_tile_color(context: template.Context) -> template.Context:
    """
    Render microsoft application tile color meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update(
        {"XICON_MSAPPLICATION_TILE_COLOR": settings.XICON_MSAPPLICATION_TILE_COLOR}
    )

    return context


@register.inclusion_tag("xicon/templatetags/xicon_mstile.html", takes_context=True)
def xicon_mstile(context: template.Context, mstile: Dict[str, str]) -> template.Context:
    """
    Render msapplication tile meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :param mstile: dict containing tile settings.
    :type mstile: Dict[str, str].
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update({"XICON_MSTILE": mstile})

    return context


@register.inclusion_tag("xicon/templatetags/xicon_mstiles.html", takes_context=True)
def xicon_mstiles(context: template.Context) -> template.Context:
    """
    Render msapplication tiles meta tags.

    :param context: template context.
    :type context: django.template.Context.
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update({"XICON_MSAPPLICATION_TILES": settings.XICON_MSAPPLICATION_TILES})

    return context
