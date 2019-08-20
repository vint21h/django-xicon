# -*- coding: utf-8 -*-

# django-xicon
# xicon/settings/settings.py


# secret key minimum enough config for django
SECRET_KEY = "xicon-test-key"  # type: str

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
