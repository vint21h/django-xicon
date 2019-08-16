# -*- coding: utf-8 -*-

# django-xicon
# xicon/settings.py


from typing import Dict, Union, Iterable

from django.conf import settings


__all__ = ["FAVICONS"]  # type: list


FAVICONS = getattr(
    settings, "XICON_FAVICONS", []
)  # type: Iterable[Dict[str, Union[str, Dict[str, int], None]]]
