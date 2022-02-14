# -*- coding: utf-8 -*-

# django-xicon
# tests/templatetags/test_xicon_tags.py


from typing import Dict, List, Iterable

from django.test import TestCase
from django.template import Context, Template
from django.test.utils import override_settings

from xicon.templatetags.xicon_tags import (
    xicon_mstile,
    xicon_favicon,
    xicon_mstiles,
    xicon_favicons,
    xicon_apple_touch_icon,
    xicon_apple_touch_icons,
    xicon_msapplication_name,
    xicon_msapplication_tile_color,
    xicon_android_chrome_theme_color,
    xicon_apple_mobile_web_app_title,
    xicon_apple_touch_icon_mask_icon,
    xicon_apple_mobile_web_app_status_bar_style,
)


__all__: List[str] = [
    "XiconFaviconTemplatetagTest",
    "XiconFaviconsTemplatetagTest",
    "XiconAppleTouchIconTemplatetagTest",
    "XiconAppleTouchIconsTemplatetagTest",
    "XiconAppleTouchMaskIconTemplatetagTest",
    "XiconAppleMobileWebAppStatusBarStyleTemplatetagTest",
    "XiconAppleMobileWebAppTitleTemplatetagTest",
    "XiconAndroidChromeThemeColorTemplatetagTest",
    "XiconMsapplicationNameTemplatetagTest",
    "XiconMsapplicationTileColorTemplatetagTest",
    "XiconMsTileTemplatetagTest",
    "XiconMsTilesTemplatetagTest",
]


class XiconFaviconTemplatetagTest(TestCase):
    """Favicon templatetag tests."""

    def test_xicon_favicon__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, Dict[str, str]] = xicon_favicon(
            favicon={
                "src": "favicon.ico",
                "type": "image/x-icon",
                "size": "16x16",
            }
        )
        expected: Dict[str, Dict[str, str]] = {
            "XICON_FAVICON": {
                "src": "favicon.ico",
                "type": "image/x-icon",
                "size": "16x16",
            }
        }

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_favicon__render(self) -> None:
        """Test templatetag rendering result."""
        context: Context = Context(
            {
                "XICON_FAVICON": {
                    "src": "favicon.ico",
                    "type": "image/x-icon",
                    "size": "16x16",
                }
            }
        )
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_favicon XICON_FAVICON %}
            """
        )
        result: str = template.render(context=context)
        expected: str = '<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" sizes="16x16"/>'  # noqa: E501

        self.assertHTMLEqual(html1=result, html2=expected)

    def test_xicon_favicon__render__without_size(self) -> None:
        """Test templatetag rendering result for favicon without size."""
        context: Context = Context(
            {
                "XICON_FAVICON": {
                    "src": "favicon.svg",
                    "type": "image/svg+xml",
                }
            }
        )
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_favicon XICON_FAVICON %}
            """
        )
        result: str = template.render(context=context)
        expected: str = '<link rel="shortcut icon" href="favicon.svg" type="image/svg+xml" sizes="any"/>'  # noqa: E501

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconFaviconsTemplatetagTest(TestCase):
    """Favicons templatetag tests."""

    def test_xicon_favicons__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, Iterable[Dict[str, str]]] = xicon_favicons()
        expected: Dict[str, List[Dict[str, str]]] = {
            "XICON_FAVICONS": [
                {"src": "favicon.ico", "type": "image/x-icon", "size": "16x16"},
                {"src": "favicon.png", "type": "image/png", "size": "32x32"},
                {"src": "favicon.svg", "type": "image/svg+xml"},
            ]
        }

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_favicons__render(self) -> None:
        """Test templatetag rendering result."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_favicons %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = """
        <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" sizes="16x16"/>
        <link rel="shortcut icon" href="favicon.png" type="image/png" sizes="32x32"/>
        <link rel="shortcut icon" href="favicon.svg" type="image/svg+xml" sizes="any"/>
        """

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_FAVICONS=[])
    def test_xicon_favicons__render__without_favicons(self) -> None:
        """Test templatetag rendering result with empty favicons list."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_favicons %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAppleTouchIconTemplatetagTest(TestCase):
    """Apple touch icon templatetag tests."""

    def test_xicon_apple_touch_icon__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, Dict[str, str]] = xicon_apple_touch_icon(
            apple_touch_icon={
                "src": "apple-touch-icon-57x57.png",
                "size": "57x57",
            }
        )
        expected: Dict[str, Dict[str, str]] = {
            "XICON_APPLE_TOUCH_ICON": {
                "src": "apple-touch-icon-57x57.png",
                "size": "57x57",
            }
        }

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_apple_touch_icon__render(self) -> None:
        """Test templatetag rendering result."""
        context: Context = Context(
            {
                "XICON_APPLE_TOUCH_ICON": {
                    "src": "apple-touch-icon-57x57.png",
                    "size": "57x57",
                }
            }
        )
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_touch_icon XICON_APPLE_TOUCH_ICON %}
            """
        )
        result: str = template.render(context=context)
        expected: str = '<link rel="apple-touch-icon" href="apple-touch-icon-57x57.png" sizes="57x57"/>'  # noqa: E501

        self.assertHTMLEqual(html1=result, html2=expected)

    def test_xicon_apple_touch_icon__render__without_size(self) -> None:
        """Test templatetag rendering result for icon without size."""
        apple_touch_icon: Dict[str, str] = {"src": "apple-touch-icon.png"}
        context: Context = Context({"XICON_APPLE_TOUCH_ICON": apple_touch_icon})
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_touch_icon XICON_APPLE_TOUCH_ICON %}
            """
        )
        result: str = template.render(context=context)
        expected: str = '<link rel="apple-touch-icon" href="apple-touch-icon.png"/>'

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAppleTouchIconsTemplatetagTest(TestCase):
    """Apple touch icons templatetag tests."""

    def test_xicon_apple_touch_icons__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, Iterable[Dict[str, str]]] = xicon_apple_touch_icons()
        expected: Dict[str, List[Dict[str, str]]] = {
            "XICON_APPLE_TOUCH_ICONS": [
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
            ]
        }

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_apple_touch_icons__render(self) -> None:
        """Test templatetag rendering result."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_touch_icons %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = """
        <link rel="apple-touch-icon" href="apple-touch-icon.png"/>
        <link rel="apple-touch-icon" href="apple-touch-icon-57x57.png" sizes="57x57"/>
        <link rel="apple-touch-icon" href="apple-touch-icon-60x60.png" sizes="60x60"/>
        <link rel="apple-touch-icon" href="apple-touch-icon-72x72.png" sizes="72x72"/>
        <link rel="apple-touch-icon" href="apple-touch-icon-76x76.png" sizes="76x76"/>
        <link rel="apple-touch-icon" href="apple-touch-icon-114x114.png" sizes="114x114"/>
        <link rel="apple-touch-icon" href="apple-touch-icon-120x120.png" sizes="120x120"/>
        <link rel="apple-touch-icon" href="apple-touch-icon-144x144.png" sizes="144x144"/>
        <link rel="apple-touch-icon" href="apple-touch-icon-152x152.png" sizes="152x152"/>
        <link rel="apple-touch-icon" href="apple-touch-icon-180x180.png" sizes="180x180"/>
        """  # noqa: E501

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_APPLE_TOUCH_ICONS=[])
    def test_xicon_apple_touch_icons__render__without_apple_touch_icons(self) -> None:
        """Test templatetag rendering result with empty apple touch icons list."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_touch_icons %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAppleTouchMaskIconTemplatetagTest(TestCase):
    """Apple touch mask icon templatetag tests."""

    def test_xicon_xicon_apple_touch_icon_mask_icon__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, str] = xicon_apple_touch_icon_mask_icon()
        expected: Dict[str, str] = {
            "XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC": "apple-touch-icon.png",
            "XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR": "#00ffff",
        }

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_xicon_apple_touch_icon_mask_icon__render(self) -> None:
        """Test templatetag rendering result."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_touch_icon_mask_icon %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = (
            '<link rel="mask-icon" href="apple-touch-icon.png" color="#00ffff">'
        )

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC="")
    def test_xicon_xicon_apple_touch_icon_mask_icon__render__without_src(self) -> None:
        """Test templatetag rendering result without icon source setting."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_touch_icon_mask_icon %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR="")
    def test_xicon_xicon_apple_touch_icon_mask_icon__render__without_color(
        self,
    ) -> None:
        """Test templatetag rendering result without icon color setting."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_touch_icon_mask_icon %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAppleMobileWebAppStatusBarStyleTemplatetagTest(TestCase):
    """Apple iOS web application status bar style templatetag tests."""

    def test_xicon_apple_mobile_web_app_status_bar_style__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, str] = xicon_apple_mobile_web_app_status_bar_style()
        expected: Dict[str, str] = {
            "XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR": "default"
        }

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_apple_mobile_web_app_status_bar_style__render(self) -> None:
        """Test templatetag rendering result."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_mobile_web_app_status_bar_style %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = (
            '<meta name="apple-mobile-web-app-status-bar-style" content="default">'
        )

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR="")
    def test_xicon_apple_touch_icon_mask_icon__render__without_color(self) -> None:
        """Test templatetag rendering result without icon color setting."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_mobile_web_app_status_bar_style %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAppleMobileWebAppTitleTemplatetagTest(TestCase):
    """Apple iOS web application title templatetag tests."""

    def test_xicon_apple_mobile_web_app_title__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, str] = xicon_apple_mobile_web_app_title()
        expected: Dict[str, str] = {"XICON_APPLE_MOBILE_WEB_APP_TITLE": "Django X Icon"}

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_apple_mobile_web_app_title__render(self) -> None:
        """Test templatetag rendering result."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_mobile_web_app_title %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = (
            '<meta name="apple-mobile-web-app-title" content="Django X Icon">'
        )

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_APPLE_MOBILE_WEB_APP_TITLE="")
    def test_xicon_apple_mobile_web_app_title__render__without_title(self) -> None:
        """Test templatetag rendering result without title setting."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_apple_mobile_web_app_title %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAndroidChromeThemeColorTemplatetagTest(TestCase):
    """Android chrome web application toolbar color templatetag tests."""

    def test_xicon_android_chrome_theme_color__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, str] = xicon_android_chrome_theme_color()
        expected: Dict[str, str] = {"XICON_ANDROID_CHROME_THEME_COLOR": "#00ffff"}

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_android_chrome_theme_color__render(self) -> None:
        """Test templatetag rendering result."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_android_chrome_theme_color %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = '<meta name="theme-color" content="#00ffff">'

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_ANDROID_CHROME_THEME_COLOR="")
    def test_xicon_android_chrome_theme_color__render__without_color(self) -> None:
        """Test templatetag rendering result without title setting."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_android_chrome_theme_color %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconMsapplicationNameTemplatetagTest(TestCase):
    """Android microsoft application name templatetag tests."""

    def test_xicon_msapplication_name__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, str] = xicon_msapplication_name()
        expected: Dict[str, str] = {"XICON_MSAPPLICATION_NAME": "Django X Icon"}

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_msapplication_name__render(self) -> None:
        """Test templatetag rendering result."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_msapplication_name %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = '<meta name="application-name" content="Django X Icon">'

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_MSAPPLICATION_NAME="")
    def test_xicon_msapplication_name__render__without_name(self) -> None:
        """Test templatetag rendering result without title setting."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_msapplication_name %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconMsapplicationTileColorTemplatetagTest(TestCase):
    """Android microsoft application tile color templatetag tests."""

    def test_xicon_msapplication_tile_color__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, str] = xicon_msapplication_tile_color()
        expected: Dict[str, str] = {"XICON_MSAPPLICATION_TILE_COLOR": "#00ffff"}

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_msapplication_tile_color__render(self) -> None:
        """Test templatetag rendering result."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_msapplication_tile_color %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = '<meta name="msapplication-TileColor" content="#00ffff">'

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_MSAPPLICATION_TILE_COLOR="")
    def test_xicon_msapplication_name__render__without_name(self) -> None:
        """Test templatetag rendering result without title setting."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_msapplication_tile_color %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconMsTileTemplatetagTest(TestCase):
    """Microsoft application tile templatetag tests."""

    def test_xicon_mstile__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, Dict[str, str]] = xicon_mstile(
            mstile={
                "src": "mstile-150x150.png",
                "name": "square150x150logo",
            }
        )
        expected: Dict[str, Dict[str, str]] = {
            "XICON_MSTILE": {
                "src": "mstile-150x150.png",
                "name": "square150x150logo",
            }
        }

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_mstile__render(self) -> None:
        """Test templatetag rendering result."""
        context: Context = Context(
            {
                "XICON_MSTILE": {
                    "src": "mstile-150x150.png",
                    "name": "square150x150logo",
                }
            }
        )
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_mstile XICON_MSTILE %}
            """
        )
        result: str = template.render(context=context)
        expected: str = (
            '<meta name="msapplication-square150x150logo" content="mstile-150x150.png">'
        )

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconMsTilesTemplatetagTest(TestCase):
    """Microsoft application tiles templatetag tests."""

    def test_xicon_mstiles__return(self) -> None:
        """Test templatetag returning value."""
        result: Dict[str, Iterable[Dict[str, str]]] = xicon_mstiles()
        expected: Dict[str, List[Dict[str, str]]] = {
            "XICON_MSAPPLICATION_TILES": [
                {"src": "mstile-70x70.png", "name": "square70x70logo"},
                {"src": "mstile-150x150.png", "name": "square150x150logo"},
                {"src": "mstile-310x150.png", "name": "wide310x150logo"},
                {"src": "mstile-310x310.png", "name": "square310x310logo"},
            ]
        }

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_mstiles__render(self) -> None:
        """Test templatetag rendering result."""
        template: Template = Template(
            """
            {% load xicon_tags %}
            {% xicon_mstiles %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = """
        <meta name="msapplication-square70x70logo" content="mstile-70x70.png">
        <meta name="msapplication-square150x150logo" content="mstile-150x150.png">
        <meta name="msapplication-wide310x150logo" content="mstile-310x150.png">
        <meta name="msapplication-square310x310logo" content="mstile-310x310.png">
        """

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_MSAPPLICATION_TILES=[])
    def test_xicon_mstiles__render__without_tiles(self) -> None:
        """Test templatetag rendering result with empty microsoft application icons list."""  # noqa: E501
        template: Template = Template(
            """{% load xicon_tags %}
            {% xicon_mstiles %}
            """
        )
        result: str = template.render(context=Context())
        expected: str = ""

        self.assertHTMLEqual(html1=result, html2=expected)
