# -*- coding: utf-8 -*-

# django-xicon
# xicon/apps.py


from django.apps import AppConfig


__all__ = ["DjangoXIconConfig"]  # type: list


class DjangoXIconConfig(AppConfig):
    """
    Application config.
    """

    name = "xicon"
    verbose_name = "Django X Icon"
