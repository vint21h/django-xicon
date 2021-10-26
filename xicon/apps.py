# -*- coding: utf-8 -*-

# django-xicon
# xicon/apps.py


from typing import List

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


__all__: List[str] = ["DjangoXIconConfig"]


class DjangoXIconConfig(AppConfig):
    """Django X Icon config."""

    name: str = "xicon"
    verbose_name: str = _("Django X Icon")
