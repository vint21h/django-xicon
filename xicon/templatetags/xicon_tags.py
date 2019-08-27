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


@register.inclusion_tag("xicon/templatetags/xicon_favicon.html", takes_context=True)
def xicon_favicon(
    context: template.Context, favicon: Dict[str, str]
) -> template.Context:
    """
    Render classic favicon meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :param favicon: dict containing favicon settings.
    :type favicon: Dict[str, str].
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update({"XICON_FAVICON": favicon})

    return context


@register.inclusion_tag("xicon/templatetags/xicon_favicons.html", takes_context=True)
def xicon_favicons(context: template.Context) -> template.Context:
    """
    Render classic favicon meta tags.

    :param context: template context.
    :type context: django.template.Context.
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update({"XICON_FAVICONS": settings.XICON_FAVICONS})

    return context


@register.inclusion_tag(
    "xicon/templatetags/xicon_apple_touch_icon.html", takes_context=True
)
def xicon_apple_touch_icon(
    context: template.Context, apple_touch_icon: Dict[str, str]
) -> template.Context:
    """
    Render apple touch icon meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :param apple_touch_icon: dict containing apple touch icon settings.
    :type apple_touch_icon: Dict[str, str].
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update({"XICON_APPLE_TOUCH_ICON": apple_touch_icon})

    return context


@register.inclusion_tag(
    "xicon/templatetags/xicon_apple_touch_icons.html", takes_context=True
)
def xicon_apple_touch_icons(context: template.Context) -> template.Context:
    """
    Render apple touch icon meta tags.

    :param context: template context.
    :type context: django.template.Context.
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update({"XICON_APPLE_TOUCH_ICONS": settings.XICON_APPLE_TOUCH_ICONS})

    return context


@register.inclusion_tag(
    "xicon/templatetags/xicon_apple_touch_icon_mask_icon.html", takes_context=True
)
def xicon_apple_touch_icon_mask_icon(context: template.Context) -> template.Context:
    """
    Render apple touch icon mask icon meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update(
        {
            "XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC": settings.XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC,  # noqa: E501
            "XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR": settings.XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR,  # noqa: E501
        }
    )

    return context


@register.inclusion_tag(
    "xicon/templatetags/xicon_apple_mobile_web_app_status_bar_style.html",
    takes_context=True,
)
def xicon_apple_mobile_web_app_status_bar_style(
    context: template.Context
) -> template.Context:
    """
    Render apple mobile web application status bar style color meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update(
        {
            "XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR": settings.XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR  # noqa: E501
        }
    )

    return context


@register.inclusion_tag(
    "xicon/templatetags/xicon_apple_mobile_web_app_title.html", takes_context=True
)
def xicon_apple_mobile_web_app_title(context: template.Context) -> template.Context:
    """
    Render apple mobile web application title meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update(
        {"XICON_APPLE_MOBILE_WEB_APP_TITLE": settings.XICON_APPLE_MOBILE_WEB_APP_TITLE}
    )

    return context


@register.inclusion_tag(
    "xicon/templatetags/xicon_android_chrome_theme_color.html", takes_context=True
)
def xicon_android_chrome_theme_color(context: template.Context) -> template.Context:
    """
    Render android chrome theme color meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update(
        {"XICON_ANDROID_CHROME_THEME_COLOR": settings.XICON_ANDROID_CHROME_THEME_COLOR}
    )

    return context


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
