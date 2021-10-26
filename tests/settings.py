# -*- coding: utf-8 -*-

# django-xicon
# tests/settings.py


import sys
import random
import pathlib
from typing import Dict, List, Union


# black magic to use imports from library code
sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent.parent))

# secret key
SECRET_KEY: str = "".join(
    [
        random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)")  # nosec
        for i in range(50)
    ]
)

# configure databases
DATABASES: Dict[str, Dict[str, str]] = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
}

# configure templates
TEMPLATES: List[Dict[str, Union[str, List[str], bool, Dict[str, str]]]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]


INSTALLED_APPS: List[str] = ["xicon"]

# configure urls
ROOT_URLCONF: str = "xicon.urls"

# xicon settings
XICON_FAVICONS: List[Dict[str, str]] = [
    {"src": "favicon.ico", "type": "image/x-icon", "size": "16x16"},
    {"src": "favicon.png", "type": "image/png", "size": "32x32"},
    {"src": "favicon.svg", "type": "image/svg+xml"},
]
XICON_APPLE_TOUCH_ICONS: List[Dict[str, str]] = [
    {"src": "apple-touch-icon.png"},
    {"src": "apple-touch-icon-57x57.png", "size": "57x57"},
    {"src": "apple-touch-icon-60x60.png", "size": "60x60"},
    {"src": "apple-touch-icon-72x72.png", "size": "72x72"},
    {"src": "apple-touch-icon-76x76.png", "size": "76x76"},
    {"src": "apple-touch-icon-114x114.png", "size": "114x114"},
    {"src": "apple-touch-icon-120x120.png", "size": "120x120"},
    {"src": "apple-touch-icon-144x144.png", "size": "144x144"},
    {"src": "apple-touch-icon-152x152.png", "size": "152x152"},
    {"src": "apple-touch-icon-180x180.png", "size": "180x180"},
]
XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC: str = "apple-touch-icon.png"
XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR: str = "#00ffff"
XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR: str = "default"
XICON_APPLE_MOBILE_WEB_APP_TITLE: str = "Django X Icon"
XICON_ANDROID_CHROME_THEME_COLOR: str = "#00ffff"
XICON_ANDROID_CHROME_ICONS: List[Dict[str, str]] = [
    {"src": "android-chrome-64x64.png", "sizes": "64x64", "type": "image/png"},
    {"src": "android-chrome-128x128.png", "sizes": "128x128", "type": "image/png"},
    {"src": "android-chrome-192x192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "android-chrome-512x512.png", "sizes": "512x512", "type": "image/png"},
]
XICON_ANDROID_CHROME_NAME: str = "Django X Icon"
XICON_ANDROID_CHROME_SHORT_NAME: str = "XI"
XICON_ANDROID_CHROME_BACKGROUND_COLOR: str = "#00ffff"
XICON_ANDROID_CHROME_DISPLAY: str = "fullscreen"
XICON_ANDROID_CHROME_ORIENTATION: str = "portrait"
XICON_MSAPPLICATION_NAME: str = "Django X Icon"
XICON_MSAPPLICATION_TILE_COLOR: str = "#00ffff"
XICON_MSAPPLICATION_TILES: List[Dict[str, str]] = [
    {"src": "mstile-70x70.png", "name": "square70x70logo"},
    {"src": "mstile-150x150.png", "name": "square150x150logo"},
    {"src": "mstile-310x150.png", "name": "wide310x150logo"},
    {"src": "mstile-310x310.png", "name": "square310x310logo"},
]
