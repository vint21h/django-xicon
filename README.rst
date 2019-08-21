.. django-xicon
.. README.rst

A django-xicon documentation
============================

    *django-xicon is a django reusable application to handle modern bunch of site icons*

.. contents::

Installation
------------
* Obtain your copy of source code from the git repository: ``git clone https://github.com/vint21h/django-xicon.git``. Or download the latest release from https://github.com/vint21h/django-xicon/tags/.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-xicon``.


Configuration
-------------
Add ``"xicon"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS += (
        "xicon",
    )

Add ``"xicon"`` to your urls definitions if you want to serve ``manifest.json`` or ``browserconfig.xml``.

.. code-block:: python

    urlpatterns += [
        url(r"^xicon/", include("xicon.urls")),
    ]


django-xicon settings
---------------------

``XICON_FAVICONS``
    Contains list of favicons. Defaults to ``[]``. Each element must be according to the next structure:

.. code-block:: python

    {
        "src": "favicon.ico",  # type: str
        "type": "image/x-icon",  # type: str
        "size": "16x16",  # type: Optional
    }

Where ``src`` key is a path to the favicon file in Django static directory, ``type`` is favicon file mime-type and ``size`` key contains icon ``width`` and ``height`` and can be omitted.

``XICON_APPLE_TOUCH_ICONS``
    Contains list of apple touch icons. Defaults to ``[]``. Each element must be according to the next structure:

.. code-block:: python

    {
        "src": "apple-touch-icon-144x144.png",  # type: str
        "size": "144x144",  # type: Optional
    }

Where ``src`` key is a path to the icon file in Django static directory and ``size`` contains icon ``width`` and ``height`` and can be omitted.

``XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC``
    Contains path to Safari pinned tabs icon. Defaults to ``""``.

``XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR``
    Contains path to Safari pinned tab icon hover color. Defaults to ``""``, must starts with ``#``.

``XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR``
    Contains iOS web application status bar color. Defaults to ``""``.

``XICON_APPLE_MOBILE_WEB_APP_TITLE``
    Contains iOS web application launch icon title. Defaults to ``""``.

``XICON_ANDROID_CHROME_THEME_COLOR``
    Contains android chrome web application toolbar color also using in ``manifest.json``. Defaults to ``""``, must starts with ``#``.

``XICON_ANDROID_CHROME_ICONS``
    Contains list of icons for ``manifest.json``. Defaults to ``[]``. Each element must be according to the next structure:

.. code-block:: python

    {
        "src": "android-chrome-64x64.png",  # type: str
        "type": "image/png",  # type: str
        "sizes": "64x64",  # type: str
    }

Where ``src`` key is a path to the icon file in Django static directory, ``type`` is favicon file mime-type and ``size`` key contains icon ``width`` and ``height``.

``XICON_ANDROID_CHROME_NAME``
    Contains android chrome web application name for ``manifest.json``. Defaults to ``""``.

``XICON_ANDROID_CHROME_SHORT_NAME``
    Contains android chrome web application short name for ``manifest.json``. Defaults to ``""``.

``XICON_ANDROID_CHROME_BACKGROUND_COLOR``
    Contains android chrome web application background color for ``manifest.json``. Defaults to ``""``, must starts with ``#``.

``XICON_ANDROID_CHROME_DISPLAY``
    Contains android chrome web application browser UI mode for ``manifest.json``. Defaults to ``""``.

``XICON_ANDROID_CHROME_ORIENTATION``
    Contains android chrome web application screen orientation for ``manifest.json``. Defaults to ``""``.

``XICON_MSAPPLICATION_NAME``
    Contains microsoft application name. Defaults to ``""``.

``XICON_MSAPPLICATION_TILE_COLOR``
    Contains microsoft application tile color also using in ``browserconfig.xml``. Defaults to ``""``, must starts with ``#``.

``XICON_MSAPPLICATION_TILES``
    Contains list of icons for microsoft application meta tags and also using in ``browserconfig.xml``. Defaults to ``[]``. Each element must be according to the next structure:

.. code-block:: python

    {
        "src": "mstile-70x70.png",  # type: str
        "name": "square70x70logo",  # type: str
    }


Licensing
---------
django-xicon is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.


Contacts
--------
**Project Website**: https://github.com/vint21h/django-xicon/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.
