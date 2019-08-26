# -*- coding: utf-8 -*-

# django-xicon
# xicon/apps.py


from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


__all__ = ["DjangoXIconConfig"]  # type: list


class DjangoXIconConfig(AppConfig):
    """
    Django X Icon config.
    """

    name = "xicon"  # type: str
    verbose_name = _("Django X Icon")  # type: str
