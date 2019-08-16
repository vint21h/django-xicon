# -*- coding: utf-8 -*-

# django-xicon
# xicon/templatetags/xicon_tags.py


from typing import Dict, Union

from django import template

from xicon.settings import (
    FAVICONS,
    APPLE_TOUCH_ICONS,
    APPLE_MOBILE_WEB_APP_TITLE,
    APPLE_TOUCH_ICON_MASK_ICON_PATH,
    APPLE_TOUCH_ICON_MASK_ICON_COLOR,
    APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR,
)


__all__ = [
    "xicon_favicon",
    "xicon_favicons",
    "xicon_apple_touch_icon",
    "xicon_apple_touch_icons",
    "xicon_apple_touch_icon_mask_icon",
    "xicon_apple_mobile_web_app_status_bar_style",
    "xicon_apple_mobile_web_app_title",
]  # type: list


register = template.Library()


@register.inclusion_tag("xicon/templatetags/xicon_favicon.html", takes_context=True)
def xicon_favicon(
    context: template.Context, favicon: Dict[str, Union[str, Dict[str, int], None]]
) -> template.Context:
    """
    Render classic favicon meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :param favicon: dict containing favicon settings.
    :type favicon: Iterable[Dict[str, Union[str, Dict[str, int], None]]].
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

    context.update({"XICON_FAVICONS": FAVICONS})

    return context


@register.inclusion_tag(
    "xicon/templatetags/xicon_apple_touch_icon.html", takes_context=True
)
def xicon_apple_touch_icon(
    context: template.Context,
    apple_touch_icon: Dict[str, Union[str, Dict[str, int], None]],
) -> template.Context:
    """
    Render apple touch icon meta tag.

    :param context: template context.
    :type context: django.template.Context.
    :param apple_touch_icon: dict containing favicon settings.
    :type apple_touch_icon: Iterable[Dict[str, Union[str, Dict[str, int], None]]].
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

    context.update({"XICON_APPLE_TOUCH_ICONS": APPLE_TOUCH_ICONS})

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
            "XICON_APPLE_TOUCH_ICON_MASK_ICON_PATH": APPLE_TOUCH_ICON_MASK_ICON_PATH,
            "XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR": APPLE_TOUCH_ICON_MASK_ICON_COLOR,
        }
    )

    return context


@register.inclusion_tag(
    "xicon/templatetags/xicon_apple_touch_icon_mask_icon.html", takes_context=True
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
            "XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR": APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR
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

    context.update({"XICON_APPLE_MOBILE_WEB_APP_TITLE": APPLE_MOBILE_WEB_APP_TITLE})

    return context
