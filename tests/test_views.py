# -*- coding: utf-8 -*-

# django-xicon
# tests/test_views.py


import json
from typing import Dict, List, Union  # pylint: disable=W0611

from django.test import TestCase
from django.shortcuts import resolve_url
from django.test.utils import override_settings
from django.http import HttpRequest, HttpResponse, JsonResponse

from xicon.views import android_chrome_manifest, msapplication_browserconfig


__all__ = [
    "MsapplicationBrowserconfigViewTest",
    "AndroidChromeManifestViewTest",
]  # type: List[str]


class MsapplicationBrowserconfigViewTest(TestCase):
    """
    Microsoft application browserconfig.xml view tests.
    """

    def test_msapplication_browserconfig__return_response(self) -> None:
        """
        Test view returning response.
        """

        request = HttpRequest()  # type: HttpRequest

        self.assertIsInstance(
            obj=msapplication_browserconfig(request=request), cls=HttpResponse
        )

    def test_msapplication_browserconfig__render(self) -> None:
        """
        Test view rendering result.
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
        result = self.client.get(
            path=resolve_url(to="msapplication-browserconfig")
        )  # type: HttpResponse

        self.assertIsNotNone(
            obj=result.context.get("XICON_MSAPPLICATION_TILES")
            if result.context
            else None
        )
        self.assertIsNotNone(
            obj=result.context.get("XICON_MSAPPLICATION_TILE_COLOR")
            if result.context
            else None
        )
        self.assertXMLEqual(xml1=result.content.decode(), xml2=expected)

    def test_msapplication_browserconfig__render__template_used(self) -> None:
        """
        Test view right template usage.
        """

        response = self.client.get(
            path=resolve_url(to="msapplication-browserconfig")
        )  # type: HttpResponse

        self.assertTemplateUsed(
            response=response, template_name="xicon/browserconfig.xml"
        )

    @override_settings(XICON_MSAPPLICATION_TILE_COLOR="")
    def test_msapplication_browserconfig__render__without_color(self) -> None:
        """
        Test view rendering result without tile color setting.
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
        result = self.client.get(
            path=resolve_url(to="msapplication-browserconfig")
        )  # type: HttpResponse

        self.assertEqual(
            first=result.context.get("XICON_MSAPPLICATION_TILE_COLOR")
            if result.context
            else None,
            second="",
        )
        self.assertXMLEqual(xml1=result.content.decode(), xml2=expected)

    @override_settings(XICON_MSAPPLICATION_TILES=[])
    def test_msapplication_browserconfig__render__without_tiles(self) -> None:
        """
        Test view rendering result without tiles setting.
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
        result = self.client.get(
            path=resolve_url(to="msapplication-browserconfig")
        )  # type: HttpResponse

        self.assertListEqual(
            list1=result.context.get("XICON_MSAPPLICATION_TILES", [])  # type: ignore
            if result.context
            else [],
            list2=[],
        )
        self.assertXMLEqual(xml1=result.content.decode(), xml2=expected)


class AndroidChromeManifestViewTest(TestCase):
    """
    Android chrome manifest.json view tests.
    """

    def test_android_chrome_manifest__return_response(self) -> None:
        """
        Test view returning response.
        """

        request = HttpRequest()  # type: HttpRequest

        self.assertIsInstance(
            obj=android_chrome_manifest(request=request), cls=JsonResponse
        )

    def test_android_chrome_manifest__render(self) -> None:
        """
        Test view rendering result.
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
        }  # type: Dict[str, Union[str, List[Dict[str, str]]]]
        result = json.loads(
            self.client.get(
                path=resolve_url(to="android-chrome-manifest")
            ).content.decode()
        )  # type: Dict[str, Union[str, List[Dict[str, str]]]]

        self.assertDictEqual(d1=result, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_THEME_COLOR="")
    def test_android_chrome_manifest__render__without_theme_color(self) -> None:
        """
        Test view rendering result without theme color setting.
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
        }  # type: Dict[str, Union[str, List[Dict[str, str]]]]
        result = json.loads(
            self.client.get(
                path=resolve_url(to="android-chrome-manifest")
            ).content.decode()
        )  # type: Dict[str, Union[str, List[Dict[str, str]]]]

        self.assertDictEqual(d1=result, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_ICONS=[])
    def test_android_chrome_manifest__render__without_icons(self) -> None:
        """
        Test view rendering result without icons setting.
        """

        expected = {
            "name": "Django X Icon",
            "short_name": "XI",
            "theme_color": "#00ffff",
            "background_color": "#00ffff",
            "display": "fullscreen",
            "orientation": "portrait",
        }  # type: Dict[str, Union[str, List[Dict[str, str]]]]
        result = json.loads(
            self.client.get(
                path=resolve_url(to="android-chrome-manifest")
            ).content.decode()
        )  # type: Dict[str, Union[str, List[Dict[str, str]]]]

        self.assertDictEqual(d1=result, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_NAME="")
    def test_android_chrome_manifest__render__without_name(self) -> None:
        """
        Test view rendering result without name setting.
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
        }  # type: Dict[str, Union[str, List[Dict[str, str]]]]
        result = json.loads(
            self.client.get(
                path=resolve_url(to="android-chrome-manifest")
            ).content.decode()
        )  # type: Dict[str, Union[str, List[Dict[str, str]]]]

        self.assertDictEqual(d1=result, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_SHORT_NAME="")
    def test_android_chrome_manifest__render__without_short_name(self) -> None:
        """
        Test view rendering result without short name setting.
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
        }  # type: Dict[str, Union[str, List[Dict[str, str]]]]
        result = json.loads(
            self.client.get(
                path=resolve_url(to="android-chrome-manifest")
            ).content.decode()
        )  # type: Dict[str, Union[str, List[Dict[str, str]]]]

        self.assertDictEqual(d1=result, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_BACKGROUND_COLOR="")
    def test_android_chrome_manifest__render__without_background_color(self) -> None:
        """
        Test view rendering result without background color setting.
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
        }  # type: Dict[str, Union[str, List[Dict[str, str]]]]
        result = json.loads(
            self.client.get(
                path=resolve_url(to="android-chrome-manifest")
            ).content.decode()
        )  # type: Dict[str, Union[str, List[Dict[str, str]]]]

        self.assertDictEqual(d1=result, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_DISPLAY="")
    def test_android_chrome_manifest__render__without_display(self) -> None:
        """
        Test view rendering result without display setting.
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
        }  # type: Dict[str, Union[str, List[Dict[str, str]]]]
        result = json.loads(
            self.client.get(
                path=resolve_url(to="android-chrome-manifest")
            ).content.decode()
        )  # type: Dict[str, Union[str, List[Dict[str, str]]]]

        self.assertDictEqual(d1=result, d2=expected)

    @override_settings(XICON_ANDROID_CHROME_ORIENTATION="")
    def test_android_chrome_manifest__render__without_orientation(self) -> None:
        """
        Test view rendering result without orientation setting.
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
        }  # type: Dict[str, Union[str, List[Dict[str, str]]]]
        result = json.loads(
            self.client.get(
                path=resolve_url(to="android-chrome-manifest")
            ).content.decode()
        )  # type: Dict[str, Union[str, List[Dict[str, str]]]]

        self.assertDictEqual(d1=result, d2=expected)
