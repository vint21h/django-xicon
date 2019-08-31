# -*- coding: utf-8 -*-

# django-xicon
# xicon/__init__.py


from typing import List  # pylint: disable=W0611


__all__ = ["default_app_config"]  # type: List[str]


default_app_config = "xicon.apps.DjangoXIconConfig"  # type: str
