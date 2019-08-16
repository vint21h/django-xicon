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

Add ``"xicon"`` to your urls definitions.

.. code-block:: python

    urlpatterns += [
        url(r"^xicon/", include("xicon.urls")),
    )

Load ``"xicon_tags"`` to your base template and place icons meta tags to <head> html tag by calling ``{% xicon_meta %}``.

For example:

.. code-block:: django

    {% load xicon_tags %}

    <head>
        {% xicon_meta %}
    </head>


xicon settings
--------------


Licensing
---------
django-xicon is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
For complete license text see COPYING file.

Contacts
--------
**Project Website**: https://github.com/vint21h/django-xicon/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.
