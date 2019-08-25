# -*- coding: utf-8 -*-

# django-xicon
# tests/test_views.py


import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse

from xicon.views import android_chrome_manifest, msapplication_browserconfig


__all__ = [
    "MsapplicationBrowserconfigViewTest",
    "AndroidChromeManifestViewTest",
]  # type: list


class MsapplicationBrowserconfigViewTest(TestCase):
    """
    Microsoft application browserconfig.xml view tests.
    """

    def test_msapplication_browserconfig__return_response(self) -> None:
        """
        Test view returning response.

        :return: nothing.
        :rtype: None.
        """

        request = HttpRequest()

        self.assertIsInstance(
            obj=msapplication_browserconfig(request=request), cls=HttpResponse
        )

    def test_msapplication_browserconfig__render(self) -> None:
        """
        Test view rendering result.

        :return: nothing.
        :rtype: None.
        """

        expected = """
        <?xml version="1.0" encoding="utf-8"?>
        <browserconfig>
            <msapplication>
                <tile>
                    <square70x70logo src="mstile-70x70.png"/>
                    <square150x150logo src="mstile-150x150.png"/>
                    <wide310x150logo src="mstile-310x150.png"/>
                    <square310x310logo src="mstile-310x310.png"/>
                    <TileColor>#00ffff</TileColor>
                </tile>
            </msapplication>
        </browserconfig>
        """  # type: str
        response = self.client.get(path=reverse("msapplication-browserconfig"))

        self.assertIsNotNone(obj=response.context.get("XICON_MSAPPLICATION_TILES"))
        self.assertIsNotNone(obj=response.context.get("XICON_MSAPPLICATION_TILE_COLOR"))
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    def test_msapplication_browserconfig__render__template_used(self) -> None:
        """
        Test view right template usage .

        :return: nothing.
        :rtype: None.
        """

        response = self.client.get(path=reverse("msapplication-browserconfig"))

        self.assertTemplateUsed(
            response=response, template_name="xicon/browserconfig.xml"
        )

    @override_settings(XICON_MSAPPLICATION_TILE_COLOR="")
    def test_msapplication_browserconfig__render__without_color(self) -> None:
        """
        Test view rendering result without tile color setting.

        :return: nothing.
        :rtype: None.
        """

        expected = """
        <?xml version="1.0" encoding="utf-8"?>
        <browserconfig>
            <msapplication>
                <tile>
                    <square70x70logo src="mstile-70x70.png"/>
                    <square150x150logo src="mstile-150x150.png"/>
                    <wide310x150logo src="mstile-310x150.png"/>
                    <square310x310logo src="mstile-310x310.png"/>
                </tile>
            </msapplication>
        </browserconfig>
        """  # type: str
        response = self.client.get(path=reverse("msapplication-browserconfig"))

        self.assertEqual(
            first=response.context.get("XICON_MSAPPLICATION_TILE_COLOR"), second=""
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)

    @override_settings(XICON_MSAPPLICATION_TILES=[])
    def test_msapplication_browserconfig__render__without_tiles(self) -> None:
        """
        Test view rendering result without tiles setting.

        :return: nothing.
        :rtype: None.
        """

        expected = """
        <?xml version="1.0" encoding="utf-8"?>
        <browserconfig>
            <msapplication>
                <tile>
                    <TileColor>#00ffff</TileColor>
                </tile>
            </msapplication>
        </browserconfig>
        """  # type: str
        response = self.client.get(path=reverse("msapplication-browserconfig"))

        self.assertListEqual(
            list1=response.context.get("XICON_MSAPPLICATION_TILES"), list2=[]
        )
        self.assertHTMLEqual(html1=response.content.decode(), html2=expected)


class AndroidChromeManifestViewTest(TestCase):
    """
    Android chrome manifest.json view tests.
    """

    def test_android_chrome_manifest__return_response(self) -> None:
        """
        Test view returning response.

        :return: nothing.
        :rtype: None.
        """

        request = HttpRequest()

        self.assertIsInstance(
            obj=android_chrome_manifest(request=request), cls=JsonResponse
        )

    def test_android_chrome_manifest__render(self) -> None:
        """
        Test view rendering result.

        :return: nothing.
        :rtype: None.
        """

        expected = {
            "name": "Django X Icon",
            "short_name": "XI",
            "icons": [
                {
                    "src": "android-chrome-64x64.png",
                    "sizes": "64x64",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-128x128.png",
                    "sizes": "128x128",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-192x192.png",
                    "sizes": "192x192",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-512x512.png",
                    "sizes": "512x512",
                    "type": "image/png",
                },
            ],
            "theme_color": "#00ffff",
            "background_color": "#00ffff",
            "display": "fullscreen",
            "orientation": "portrait",
        }  # type: dict
        response = json.loads(
            self.client.get(path=reverse("android-chrome-manifest")).content.decode()
        )  # type: dict

        self.assertDictEqual(d1=response, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_THEME_COLOR="")
    def test_android_chrome_manifest__render__without_theme_color(self) -> None:
        """
        Test view rendering result without theme color setting.

        :return: nothing.
        :rtype: None.
        """

        expected = {
            "name": "Django X Icon",
            "short_name": "XI",
            "icons": [
                {
                    "src": "android-chrome-64x64.png",
                    "sizes": "64x64",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-128x128.png",
                    "sizes": "128x128",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-192x192.png",
                    "sizes": "192x192",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-512x512.png",
                    "sizes": "512x512",
                    "type": "image/png",
                },
            ],
            "background_color": "#00ffff",
            "display": "fullscreen",
            "orientation": "portrait",
        }  # type: dict
        response = json.loads(
            self.client.get(path=reverse("android-chrome-manifest")).content.decode()
        )  # type: dict

        self.assertDictEqual(d1=response, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_ICONS=[])
    def test_android_chrome_manifest__render__without_icons(self) -> None:
        """
        Test view rendering result without icons setting.

        :return: nothing.
        :rtype: None.
        """

        expected = {
            "name": "Django X Icon",
            "short_name": "XI",
            "theme_color": "#00ffff",
            "background_color": "#00ffff",
            "display": "fullscreen",
            "orientation": "portrait",
        }  # type: dict
        response = json.loads(
            self.client.get(path=reverse("android-chrome-manifest")).content.decode()
        )  # type: dict

        self.assertDictEqual(d1=response, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_NAME="")
    def test_android_chrome_manifest__render__without_name(self) -> None:
        """
        Test view rendering result without name setting.

        :return: nothing.
        :rtype: None.
        """

        expected = {
            "short_name": "XI",
            "icons": [
                {
                    "src": "android-chrome-64x64.png",
                    "sizes": "64x64",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-128x128.png",
                    "sizes": "128x128",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-192x192.png",
                    "sizes": "192x192",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-512x512.png",
                    "sizes": "512x512",
                    "type": "image/png",
                },
            ],
            "theme_color": "#00ffff",
            "background_color": "#00ffff",
            "display": "fullscreen",
            "orientation": "portrait",
        }  # type: dict
        response = json.loads(
            self.client.get(path=reverse("android-chrome-manifest")).content.decode()
        )

        self.assertDictEqual(d1=response, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_SHORT_NAME="")
    def test_android_chrome_manifest__render__without_short_name(self) -> None:
        """
        Test view rendering result without short name setting.

        :return: nothing.
        :rtype: None.
        """

        expected = {
            "name": "Django X Icon",
            "icons": [
                {
                    "src": "android-chrome-64x64.png",
                    "sizes": "64x64",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-128x128.png",
                    "sizes": "128x128",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-192x192.png",
                    "sizes": "192x192",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-512x512.png",
                    "sizes": "512x512",
                    "type": "image/png",
                },
            ],
            "theme_color": "#00ffff",
            "background_color": "#00ffff",
            "display": "fullscreen",
            "orientation": "portrait",
        }  # type: dict
        response = json.loads(
            self.client.get(path=reverse("android-chrome-manifest")).content.decode()
        )  # type: dict

        self.assertDictEqual(d1=response, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_BACKGROUND_COLOR="")
    def test_android_chrome_manifest__render__without_background_color(self) -> None:
        """
        Test view rendering result without background color setting.

        :return: nothing.
        :rtype: None.
        """

        expected = {
            "name": "Django X Icon",
            "short_name": "XI",
            "icons": [
                {
                    "src": "android-chrome-64x64.png",
                    "sizes": "64x64",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-128x128.png",
                    "sizes": "128x128",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-192x192.png",
                    "sizes": "192x192",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-512x512.png",
                    "sizes": "512x512",
                    "type": "image/png",
                },
            ],
            "theme_color": "#00ffff",
            "display": "fullscreen",
            "orientation": "portrait",
        }  # type: dict
        response = json.loads(
            self.client.get(path=reverse("android-chrome-manifest")).content.decode()
        )  # type: dict

        self.assertDictEqual(d1=response, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_DISPLAY="")
    def test_android_chrome_manifest__render__without_display(self) -> None:
        """
        Test view rendering result without display setting.

        :return: nothing.
        :rtype: None.
        """

        expected = {
            "name": "Django X Icon",
            "short_name": "XI",
            "icons": [
                {
                    "src": "android-chrome-64x64.png",
                    "sizes": "64x64",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-128x128.png",
                    "sizes": "128x128",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-192x192.png",
                    "sizes": "192x192",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-512x512.png",
                    "sizes": "512x512",
                    "type": "image/png",
                },
            ],
            "theme_color": "#00ffff",
            "background_color": "#00ffff",
            "orientation": "portrait",
        }  # type: dict
        response = json.loads(
            self.client.get(path=reverse("android-chrome-manifest")).content.decode()
        )  # type: dict

        self.assertDictEqual(d1=response, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_ORIENTATION="")
    def test_android_chrome_manifest__render__without_orientation(self) -> None:
        """
        Test view rendering result without orientation setting.

        :return: nothing.
        :rtype: None.
        """

        expected = {
            "name": "Django X Icon",
            "short_name": "XI",
            "icons": [
                {
                    "src": "android-chrome-64x64.png",
                    "sizes": "64x64",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-128x128.png",
                    "sizes": "128x128",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-192x192.png",
                    "sizes": "192x192",
                    "type": "image/png",
                },
                {
                    "src": "android-chrome-512x512.png",
                    "sizes": "512x512",
                    "type": "image/png",
                },
            ],
            "theme_color": "#00ffff",
            "background_color": "#00ffff",
            "display": "fullscreen",
        }  # type: dict
        response = json.loads(
            self.client.get(path=reverse("android-chrome-manifest")).content.decode()
        )  # type: dict

        self.assertDictEqual(d1=response, d2=expected)
