# -*- coding: utf-8 -*-

# django-xicon
# xicon/settings/settings.py


# secret key
SECRET_KEY = "xicon-test-key"  # type: str

# configure databases
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "test.sqlite3"}
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
ROOT_URLCONF = __name__  # type: str

# xicon settings
XICON_FAVICONS = [
    {"src": "favicon.ico", "type": "image/x-icon", "size": "16x16"},
    {"src": "favicon.png", "type": "image/png", "size": "32x32"},
    {"src": "favicon.svg", "type": "image/svg+xml"},
]  # list
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
]  # list
XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC = "apple-touch-icon.png"
XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR = "#00ffff"
XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR = "default"
XICON_APPLE_MOBILE_WEB_APP_TITLE = "Django X Icon"
