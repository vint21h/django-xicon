# -*- coding: utf-8 -*-

# django-xicon
# xicon/apps.py


from typing import List  # pylint: disable=W0611

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__ = ["DjangoXIconConfig"]  # type: List[str]


class DjangoXIconConfig(AppConfig):
    """
    Django X Icon config.
    """

    name = "xicon"  # type: str
    verbose_name = _("Django X Icon")  # type: str
