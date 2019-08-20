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
