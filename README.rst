.. django-xicon
.. README.rst


A django-xicon documentation
============================

|GitHub|_ |Coveralls|_ |pypi-license|_ |pypi-version|_ |pypi-python-version|_ |pypi-django-version|_ |pypi-format|_ |pypi-wheel|_ |pypi-status|_

    *django-xicon is a Django reusable application to handle a modern bunch of site icons*

.. contents::

Nowadays ``<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" sizes="16x16"/>`` is not enough for good site or web application.
`Apple <https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html>`_, `Microsoft <https://technet.microsoft.com/en-us/windows/dn320426(v=vs.60)#MainContent>`_ and `Google <https://developers.google.com/web/fundamentals/web-app-manifest/>`_ creates their own standards.
``django-xicon`` solve the boring problem of reading and implementing of these standards requirements through fast and simple Django project configuration. These standards requirements are not fully implemented, but enough to pass most of the checks.

Installation
------------
* Obtain your copy of source code from the git repository: ``$ git clone https://github.com/vint21h/django-xicon.git``. Or download the latest release from https://github.com/vint21h/django-xicon/tags/.
* Run ``$ python ./setup.py install`` from the repository source tree or unpacked archive. Or use pip: ``$ pip install django-xicon``.

Configuration
-------------
* Add ``"xicon"`` to ``settings.INSTALLED_APPS``:

.. code-block:: python

    # settings.py

    INSTALLED_APPS += [
        "xicon",
    ]

* Add ``"xicon"`` to your URLs definitions if you want to serve ``manifest.json`` or ``browserconfig.xml``:

.. code-block:: python

    # urls.py

    from django.urls import include, re_path


    urlpatterns += [
        re_path(r"^xicon/", include("xicon.urls")),
    ]

Settings
--------

``XICON_FAVICONS``
    Contains list of favicons. Defaults to ``[]``. Each element must be according to the next structure:

.. code-block:: python

    {
        "src": "favicon.ico",
        "type": "image/x-icon",
        "size": "16x16",
    }  # type: Dict[str, Optional[str]]

Where ``src`` key is a path to the favicon file in Django static directory, ``type`` is favicon file mime-type and ``size`` key contains icon's ``width`` and ``height`` and can be omitted.

``XICON_APPLE_TOUCH_ICONS``
    Contains list of apple touch icons. Defaults to ``[]``. Each element must be according to the next structure:

.. code-block:: python

    {
        "src": "apple-touch-icon-144x144.png",
        "size": "144x144",
    }  # type: Dict[str, Optional[str]]

Where ``src`` key is a path to the icon file in Django static directory and ``size`` contains icon's ``width`` and ``height`` and can be omitted.

``XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC``
    Contains path to Safari pinned tabs icon. Defaults to ``""``.

``XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR``
    Contains path to Safari pinned tab icon hover color. Defaults to ``""``, must start with ``#``.

``XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR``
    Contains iOS web application status bar color. Defaults to ``""``.

``XICON_APPLE_MOBILE_WEB_APP_TITLE``
    Contains iOS web application launch icon title. Defaults to ``""``.

``XICON_ANDROID_CHROME_THEME_COLOR``
    Contains android chrome web application toolbar color also used in ``manifest.json``. Defaults to ``""``, must start with ``#``.

``XICON_ANDROID_CHROME_ICONS``
    Contains a list of icons for ``manifest.json``. Defaults to ``[]``. Each element must be according to the next structure:

.. code-block:: python

    {
        "src": "android-chrome-64x64.png",
        "type": "image/png",
        "sizes": "64x64",
    }  # type: Dict[str, str]

Where ``src`` key is a path to the icon file in Django static directory, ``type`` is favicon file mime-type and ``size`` key contains icon's ``width`` and ``height``.

``XICON_ANDROID_CHROME_NAME``
    Contains android chrome web application name for ``manifest.json``. Defaults to ``""``.

``XICON_ANDROID_CHROME_SHORT_NAME``
    Contains android chrome web application short name for ``manifest.json``. Defaults to ``""``.

``XICON_ANDROID_CHROME_BACKGROUND_COLOR``
    Contains android chrome web application background color for ``manifest.json``. Defaults to ``""``, must start with ``#``.

``XICON_ANDROID_CHROME_DISPLAY``
    Contains android chrome web application browser UI mode for ``manifest.json``. Defaults to ``""``.

``XICON_ANDROID_CHROME_ORIENTATION``
    Contains android chrome web application screen orientation for ``manifest.json``. Defaults to ``""``.

``XICON_MSAPPLICATION_NAME``
    Contains microsoft application name. Defaults to ``""``.

``XICON_MSAPPLICATION_TILE_COLOR``
    Contains Microsoft application tile color also used in ``browserconfig.xml``. Defaults to ``""``, must start with ``#``.

``XICON_MSAPPLICATION_TILES``
    Contains list of icons for Microsoft application meta tags and also used in ``browserconfig.xml``. Defaults to ``[]``. Each element must be according to the next structure:

.. code-block:: python

    {
        "src": "mstile-70x70.png",
        "name": "square70x70logo",
    }  # type: Dict[str, str]

Where ``src`` key is a path to the icon file in Django static directory and ``name`` contains tile name (type).

Usage
-----
If you want to use all power of ``django-xicon``, just set up all settings and include ``"xicon/includes/xicon.html"`` to your base template ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    <head>
        {% include "xicon/includes/xicon.html" %}
    </head>

Or just for favicons, setup ``XICON_FAVICONS`` setting, load ``"xicon_tags"`` to your base template and place ``"xicon_favicons"`` in ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    {% load xicon_tags %}

    <head>
        {% xicon_favicons %}
    </head>

If you want to setup web application for `apple devices <https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html>`_, setup all settings prefixed with ``XICON_APPLE_`` and include ``"xicon/includes/apple.html"`` to your base template ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    <head>
        {% include "xicon/includes/apple.html" %}
    </head>

Or just for apple touch icons, setup ``APPLE_TOUCH_ICONS`` setting, load ``"xicon_tags"`` to your base template and place ``"xicon_apple_touch_icons"`` in ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    {% load xicon_tags %}

    <head>
        {% xicon_apple_touch_icons %}
    </head>

To use Safari pinned tabs mask icon setup ``XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC`` and ``XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR`` settings, load ``"xicon_tags"`` to your base template and place ``"xicon_apple_touch_icon_mask_icon"`` in ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    {% load xicon_tags %}

    <head>
        {% xicon_apple_touch_icon_mask_icon %}
    </head>

To configure iOS web application bar style color setup ``XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR`` setting, load ``"xicon_tags"`` to your base template and place ``"xicon_apple_mobile_web_app_status_bar_style"`` in ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    {% load xicon_tags %}

    <head>
        {% xicon_apple_mobile_web_app_status_bar_style %}
    </head>

To configure iOS web application launch icon title setup ``XICON_APPLE_MOBILE_WEB_APP_TITLE`` setting, load ``"xicon_tags"`` to your base template and place ``"xicon_apple_mobile_web_app_title"`` in ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    {% load xicon_tags %}

    <head>
        {% xicon_apple_mobile_web_app_title %}
    </head>

If you want to use `android chrome <https://developers.google.com/web/fundamentals/web-app-manifest/>`_ related things, just setup all settings prefixed with ``XICON_ANDROID_CHROME_`` and include ``"xicon/includes/android-chrome.html"`` to your base template ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    <head>
        {% include "xicon/includes/android-chrome.html" %}
    </head>

Or if you need only configure android chrome web application toolbar color, setup ``XICON_ANDROID_CHROME_THEME_COLOR``, load ``"xicon_tags"`` to your base template and place ``"xicon_android_chrome_theme_color"`` in ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    {% load xicon_tags %}

    <head>
        {% xicon_android_chrome_theme_color %}
    </head>

If you need generate and serve ``manifest.json``, add ``"xicon"`` to your URLs definitions, setup next settings: ``XICON_ANDROID_CHROME_THEME_COLOR``, ``XICON_ANDROID_CHROME_ICONS``, ``XICON_ANDROID_CHROME_NAME``, ``XICON_ANDROID_CHROME_SHORT_NAME``, ``XICON_ANDROID_CHROME_BACKGROUND_COLOR``, ``XICON_ANDROID_CHROME_DISPLAY`` and `XICON_ANDROID_CHROME_ORIENTATION``, and then include ``"xicon/includes/android-chrome-manifest-meta.html"`` to your base template ``<head>`` HTML tag:

.. code-block:: python

    # urls.py

    from django.urls import include, re_path


    urlpatterns += [
        re_path(r"^xicon/", include("xicon.urls")),
    ]

.. code-block:: django

    {# base.html #}

    <head>
        {% include "xicon/includes/android-chrome-manifest-meta.html" %}
    </head>

If you want to setup `microsoft application <https://technet.microsoft.com/en-us/windows/dn320426(v=vs.60)#MainContent>`_ configure all settings prefixed with ``XICON_MSAPPLICATION_`` and include ``"xicon/includes/msapplication.html"`` to your base template ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    <head>
        {% include "xicon/includes/msapplication.html" %}
    </head>


Or if you need only configure microsoft application name, setup ``XICON_MSAPPLICATION_NAME``, load ``"xicon_tags"`` to your base template and place ``"xicon_msapplication_name"`` in ``<head>`` HTML tag of your base template:

.. code-block:: django

    {# base.html #}

    {% load xicon_tags %}

    <head>
        {% xicon_msapplication_name %}
    </head>

If you need configure microsoft application tile color, setup ``XICON_MSAPPLICATION_TILE_COLOR``, load ``"xicon_tags"`` to your base template and place ``"xicon_msapplication_tile_color"`` in ``<head>`` HTML tag of your base template:

.. code-block:: django

    {# base.html #}

    {% load xicon_tags %}

    <head>
        {% xicon_msapplication_tile_color %}
    </head>

If you need generate and serve ``browserconfig.xml``, add ``"xicon"`` to your URLs definitions, setup next settings: ``XICON_MSAPPLICATION_TILE_COLOR`` and ``XICON_MSAPPLICATION_TILES``, and then include ``"xicon/includes/msapplication-browserconfig-meta.html"`` to your base template ``<head>`` HTML tag:

.. code-block:: python

    # urls.py

    from django.urls import include, re_path


    urlpatterns += [
        re_path(r"^xicon/", include("xicon.urls")),
    ]

.. code-block:: django

    {# base.html #}

    <head>
        {% include "xicon/includes/msapplication-browserconfig-meta.html" %}
    </head>

Or just for microsoft application tiles, setup ``MSAPPLICATION_TILES`` setting, load ``"xicon_tags"`` to your base template and place ``"xicon_mstiles"`` in ``<head>`` HTML tag:

.. code-block:: django

    {# base.html #}

    {% load xicon_tags %}

    <head>
        {% xicon_mstiles %}
    </head>

Contributing
------------
1. `Fork it <https://github.com/vint21h/django-xicon/>`_
2. Install `GNU Make <https://www.gnu.org/software/make/>`_
3. Install and configure `pyenv <https://github.com/pyenv/pyenv/>`_ and `pyenv-virtualenv plugin <https://github.com/pyenv/pyenv-virtualenv/>`_
4. Install and configure `direnv <https://github.com/direnv/direnv/>`_
5. Create environment config from example

.. code-block:: bash

    cp .env.example .env

6. Install development dependencies:

.. code-block:: bash

    make install

7. Create your fix/feature branch:

.. code-block:: bash

    git checkout -b my-new-fix-or-feature

8. Check code style and moreover:

.. code-block:: bash

    make check

9. Run tests:

.. code-block:: bash

    make test

10. Push to the branch:

.. code-block:: bash

    git push origin my-new-fix-or-feature

11. `Create a new Pull Request <https://github.com/vint21h/django-xicon/compare/>`_

Licensing
---------
django-xicon is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-xicon/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For complete authors list see AUTHORS file.

.. |GitHub| image:: https://github.com/vint21h/django-xicon/workflows/build/badge.svg
    :alt: GitHub
.. |Coveralls| image:: https://coveralls.io/repos/github/vint21h/django-xicon/badge.svg?branch=master
    :alt: Coveralls
.. |pypi-license| image:: https://img.shields.io/pypi/l/django-xicon
    :alt: License
.. |pypi-version| image:: https://img.shields.io/pypi/v/django-xicon
    :alt: Version
.. |pypi-django-version| image:: https://img.shields.io/pypi/djversions/django-xicon
    :alt: Supported Django version
.. |pypi-python-version| image:: https://img.shields.io/pypi/pyversions/django-xicon
    :alt: Supported Python version
.. |pypi-format| image:: https://img.shields.io/pypi/format/django-xicon
    :alt: Package format
.. |pypi-wheel| image:: https://img.shields.io/pypi/wheel/django-xicon
    :alt: Python wheel support
.. |pypi-status| image:: https://img.shields.io/pypi/status/django-xicon
    :alt: Package status
.. _GitHub: https://github.com/vint21h/django-xicon/actions/
.. _Coveralls: https://coveralls.io/github/vint21h/django-xicon?branch=master
.. _pypi-license: https://pypi.org/project/django-xicon/
.. _pypi-version: https://pypi.org/project/django-xicon/
.. _pypi-django-version: https://pypi.org/project/django-xicon/
.. _pypi-python-version: https://pypi.org/project/django-xicon/
.. _pypi-format: https://pypi.org/project/django-xicon/
.. _pypi-wheel: https://pypi.org/project/django-xicon/
.. _pypi-status: https://pypi.org/project/django-xicon/
