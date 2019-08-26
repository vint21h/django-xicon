# -*- coding: utf-8 -*-

# django-xicon
# tests/settings.py


import pathlib
import sys


# black magic to use imports from library code
sys.path.insert(0, str(pathlib.Path(__file__).absolute().parent.parent.parent))

# secret key
SECRET_KEY = "django-xicon-test-key"  # type: str

# configure databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "django-xicon-tests.sqlite3",
    }
}  # type: dict

# configure templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]  # type: list


# add nose test runner application and django-xicon
INSTALLED_APPS = ["django_nose", "xicon"]  # type: list

# add nose test runner
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"  # type: str

# configure nose test runner
NOSE_ARGS = [
    "--rednose",
    "--force-color",
    "--with-timer",
    "--with-doctest",
    "--with-coverage",
    "--cover-inclusive",
    "--cover-erase",
    "--cover-package=xicon",
    "--logging-clear-handlers",
]  # type: list

# configure urls
ROOT_URLCONF = "xicon.urls"  # type: str

# xicon settings
XICON_FAVICONS = [
    {"src": "favicon.ico", "type": "image/x-icon", "size": "16x16"},
    {"src": "favicon.png", "type": "image/png", "size": "32x32"},
    {"src": "favicon.svg", "type": "image/svg+xml"},
]  # type: list
XICON_APPLE_TOUCH_ICONS = [
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
]  # type: list
XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC = "apple-touch-icon.png"  # type: str
XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR = "#00ffff"  # type: str
XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR = "default"  # type: str
XICON_APPLE_MOBILE_WEB_APP_TITLE = "Django X Icon"  # type: str
XICON_ANDROID_CHROME_THEME_COLOR = "#00ffff"  # type: str
XICON_ANDROID_CHROME_ICONS = [
    {"src": "android-chrome-64x64.png", "sizes": "64x64", "type": "image/png"},
    {"src": "android-chrome-128x128.png", "sizes": "128x128", "type": "image/png"},
    {"src": "android-chrome-192x192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "android-chrome-512x512.png", "sizes": "512x512", "type": "image/png"},
]  # type: list
XICON_ANDROID_CHROME_NAME = "Django X Icon"  # type: str
XICON_ANDROID_CHROME_SHORT_NAME = "XI"  # type: str
XICON_ANDROID_CHROME_BACKGROUND_COLOR = "#00ffff"  # type: str
XICON_ANDROID_CHROME_DISPLAY = "fullscreen"  # type: str
XICON_ANDROID_CHROME_ORIENTATION = "portrait"  # type: str
XICON_MSAPPLICATION_NAME = "Django X Icon"  # type: str
XICON_MSAPPLICATION_TILE_COLOR = "#00ffff"  # type: str
XICON_MSAPPLICATION_TILES = [
    {"src": "mstile-70x70.png", "name": "square70x70logo"},
    {"src": "mstile-150x150.png", "name": "square150x150logo"},
    {"src": "mstile-310x150.png", "name": "wide310x150logo"},
    {"src": "mstile-310x310.png", "name": "square310x310logo"},
]  # type: list
