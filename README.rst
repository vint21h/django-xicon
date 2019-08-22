.. django-xicon
.. README.rst

A django-xicon documentation
============================

|Travis|_ |Codacy|_ |Requires|_

    *django-xicon is a Django reusable application to handle a modern bunch of site icons*

.. contents::

Nowadays ``<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" sizes="16x16"/>`` is not enough for good site or web application.
`Apple <https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html>`_, `Microsoft <https://technet.microsoft.com/en-us/windows/dn320426(v=vs.60)#MainContent>`_ and `Google <https://developers.google.com/web/fundamentals/web-app-manifest/>`_ creates their own standards.
``django-xicon`` solve the boring problem of reading and implementing of these standards requirements through fast and simple Django project configuration. These standards requirements are not fully implemented, but enough to pass most of the checks.

Installation
------------
* Obtain your copy of source code from the git repository: ``git clone https://github.com/vint21h/django-xicon.git``. Or download the latest release from https://github.com/vint21h/django-xicon/tags/.
* Run ``python ./setup.py install`` from the repository source tree or unpacked archive. Or use pip: ``pip install django-xicon``.


Configuration
-------------
Add ``"xicon"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS += (
        "xicon",
    )

Add ``"xicon"`` to your URLs definitions if you want to serve ``manifest.json`` or ``browserconfig.xml``.

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

Where ``src`` key is a path to the favicon file in Django static directory, ``type`` is favicon file mime-type and ``size`` key contains icon's ``width`` and ``height`` and can be omitted.

``XICON_APPLE_TOUCH_ICONS``
    Contains list of apple touch icons. Defaults to ``[]``. Each element must be according to the next structure:

.. code-block:: python

    {
        "src": "apple-touch-icon-144x144.png",  # type: str
        "size": "144x144",  # type: Optional
    }

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
        "src": "android-chrome-64x64.png",  # type: str
        "type": "image/png",  # type: str
        "sizes": "64x64",  # type: str
    }

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
        "src": "mstile-70x70.png",  # type: str
        "name": "square70x70logo",  # type: str
    }

Where ``src`` key is a path to the icon file in Django static directory and ``name`` contains tile name (type).

Licensing
---------
django-xicon is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.


Contacts
--------
**Project Website**: https://github.com/vint21h/django-xicon/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For complete authors list see AUTHORS file.

.. |Travis| image:: https://travis-ci.org/vint21h/django-xicon.svg?branch=master
.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/b68e596c87914612b83fb2d9872dd1c7
.. |Requires| image:: https://requires.io/github/vint21h/django-xicon/requirements.svg?branch=master
.. _Travis: https://travis-ci.org/vint21h/django-xicon/
.. _Codacy: https://www.codacy.com/app/vint21h/django-xicon/
.. _Requires: https://requires.io/github/vint21h/django-xicon/requirements/?branch=master


.. image:: https://api.codacy.com/project/badge/Grade/1fc70ffd575c4809ab9948b96d75c01d
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/vint21h/django-xicon?utm_source=github.com&utm_medium=referral&utm_content=vint21h/django-xicon&utm_campaign=Badge_Grade_Dashboard