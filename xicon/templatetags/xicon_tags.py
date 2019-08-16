# -*- coding: utf-8 -*-

# django-xicon
# xicon/templatetags/xicon_tags.py


from typing import Dict, Union, Iterable

from django import template

from xicon.settings import FAVICONS


__all__ = ["xicon_favicon"]  # type: list


register = template.Library()


@register.inclusion_tag("xicon/templatetags/xicon_favicon.html", takes_context=True)
def xicon_favicon(
    context: template.Context,
    favicon: Iterable[Dict[str, Union[str, Dict[str, int], None]]],
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
def xicon_favicons(context: template.Context,) -> template.Context:
    """
    Render classic favicon meta tags.

    :param context: template context.
    :type context: django.template.Context.
    :return: updated template context.
    :rtype: django.template.Context.
    """

    context.update({"XICON_FAVICONS": FAVICONS})

    return context
