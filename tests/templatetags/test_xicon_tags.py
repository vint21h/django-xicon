# -*- coding: utf-8 -*-

# django-xicon
# tests/templatetags/test_xicon_tags.py


from typing import Dict, List, Iterable  # pylint: disable=W0611

from django.test import TestCase
from django.template import Context, Template
from django.test.utils import override_settings

from xicon.conf import settings
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


__all__ = [
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
]  # type: List[str]


class XiconFaviconTemplatetagTest(TestCase):
    """
    Favicon templatetag tests.
    """

    def test_xicon_favicon__return(self) -> None:
        """
        Test templatetag returning value.
        """

        favicon = {
            "src": "favicon.ico",
            "type": "image/x-icon",
            "size": "16x16",
        }  # type: Dict[str, str]
        result = xicon_favicon(favicon=favicon)  # type: Dict[str, Dict[str, str]]
        expected = {"XICON_FAVICON": favicon}  # type: Dict[str, Dict[str, str]]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_favicon__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        favicon = {
            "src": "favicon.ico",
            "type": "image/x-icon",
            "size": "16x16",
        }  # type: Dict[str, str]
        context = Context({"XICON_FAVICON": favicon})  # type: Context
        template = Template(
            "{% load xicon_tags %}" "{% xicon_favicon XICON_FAVICON %}"
        )  # type: Template
        result = template.render(context=context)  # type: str
        expected = '<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" sizes="16x16"/>'  # type: str  # noqa: E501

        self.assertHTMLEqual(html1=result, html2=expected)

    def test_xicon_favicon__render__without_size(self) -> None:
        """
        Test templatetag rendering result for favicon without size.
        """

        favicon = {
            "src": "favicon.svg",
            "type": "image/svg+xml",
        }  # type: Dict[str, str]
        context = Context({"XICON_FAVICON": favicon})  # type: Context
        template = Template(
            "{% load xicon_tags %}" "{% xicon_favicon XICON_FAVICON %}"
        )  # type: Template
        result = template.render(context=context)  # type: str
        expected = '<link rel="shortcut icon" href="favicon.svg" type="image/svg+xml" sizes="any"/>'  # type: str  # noqa: E501

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconFaviconsTemplatetagTest(TestCase):
    """
    Favicons templatetag tests.
    """

    def test_xicon_favicons__return(self) -> None:
        """
        Test templatetag returning value.
        """

        result = xicon_favicons()  # type: Dict[str, Iterable[Dict[str, str]]]
        expected = {
            "XICON_FAVICONS": settings.XICON_FAVICONS
        }  # type: Dict[str, List[Dict[str, str]]]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_favicons__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_favicons %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = """
        <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" sizes="16x16"/>
        <link rel="shortcut icon" href="favicon.png" type="image/png" sizes="32x32"/>
        <link rel="shortcut icon" href="favicon.svg" type="image/svg+xml" sizes="any"/>
        """  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_FAVICONS=[])
    def test_xicon_favicons__render__without_favicons(self) -> None:
        """
        Test templatetag rendering result with empty favicons list.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_favicons %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAppleTouchIconTemplatetagTest(TestCase):
    """
    Apple touch icon templatetag tests.
    """

    def test_xicon_apple_touch_icon__return(self) -> None:
        """
        Test templatetag returning value.
        """

        apple_touch_icon = {
            "src": "apple-touch-icon-57x57.png",
            "size": "57x57",
        }  # type: Dict[str, str]
        result = xicon_apple_touch_icon(
            apple_touch_icon=apple_touch_icon
        )  # type: Dict[str, Dict[str, str]]
        expected = {
            "XICON_APPLE_TOUCH_ICON": apple_touch_icon
        }  # type: Dict[str, Dict[str, str]]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_apple_touch_icon__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        apple_touch_icon = {
            "src": "apple-touch-icon-57x57.png",
            "size": "57x57",
        }  # type: Dict[str, str]
        context = Context({"XICON_APPLE_TOUCH_ICON": apple_touch_icon})  # type: Context
        template = Template(
            "{% load xicon_tags %}"
            "{% xicon_apple_touch_icon XICON_APPLE_TOUCH_ICON %}"
        )  # type: Template
        result = template.render(context=context)  # type: str
        expected = '<link rel="apple-touch-icon" href="apple-touch-icon-57x57.png" sizes="57x57"/>'  # type: str  # noqa: E501

        self.assertHTMLEqual(html1=result, html2=expected)

    def test_xicon_apple_touch_icon__render__without_size(self) -> None:
        """
        Test templatetag rendering result for icon without size.
        """

        apple_touch_icon = {"src": "apple-touch-icon.png"}  # type: Dict[str, str]
        context = Context({"XICON_APPLE_TOUCH_ICON": apple_touch_icon})  # type: Context
        template = Template(
            "{% load xicon_tags %}"
            "{% xicon_apple_touch_icon XICON_APPLE_TOUCH_ICON %}"
        )  # type: Template
        result = template.render(context=context)  # type: str
        expected = (
            '<link rel="apple-touch-icon" href="apple-touch-icon.png"/>'
        )  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAppleTouchIconsTemplatetagTest(TestCase):
    """
    Apple touch icons templatetag tests.
    """

    def test_xicon_apple_touch_icons__return(self) -> None:
        """
        Test templatetag returning value.
        """

        result = xicon_apple_touch_icons()  # type: Dict[str, Iterable[Dict[str, str]]]
        expected = {
            "XICON_APPLE_TOUCH_ICONS": settings.XICON_APPLE_TOUCH_ICONS
        }  # type: Dict[str, List[Dict[str, str]]]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_apple_touch_icons__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_touch_icons %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = """
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
        """  # type: str  # noqa: E501

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_APPLE_TOUCH_ICONS=[])
    def test_xicon_apple_touch_icons__render__without_apple_touch_icons(self) -> None:
        """
        Test templatetag rendering result with empty apple touch icons list.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_touch_icons %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAppleTouchMaskIconTemplatetagTest(TestCase):
    """
    Apple touch mask icon templatetag tests.
    """

    def test_xicon_xicon_apple_touch_icon_mask_icon__return(self) -> None:
        """
        Test templatetag returning value.
        """

        result = xicon_apple_touch_icon_mask_icon()  # type: Dict[str, str]
        expected = {
            "XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC": settings.XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC,  # noqa: E501
            "XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR": settings.XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR,  # noqa: E501
        }  # type: Dict[str, str]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_xicon_apple_touch_icon_mask_icon__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_touch_icon_mask_icon %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = (
            '<link rel="mask-icon" href="apple-touch-icon.png" color="#00ffff">'
        )  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC="")
    def test_xicon_xicon_apple_touch_icon_mask_icon__render__without_src(self) -> None:
        """
        Test templatetag rendering result without icon source setting.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_touch_icon_mask_icon %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR="")
    def test_xicon_xicon_apple_touch_icon_mask_icon__render__without_color(
        self,
    ) -> None:
        """
        Test templatetag rendering result without icon color setting.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_touch_icon_mask_icon %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAppleMobileWebAppStatusBarStyleTemplatetagTest(TestCase):
    """
    Apple iOS web application status bar style templatetag tests.
    """

    def test_xicon_apple_mobile_web_app_status_bar_style__return(self) -> None:
        """
        Test templatetag returning value.
        """

        result = xicon_apple_mobile_web_app_status_bar_style()  # type: Dict[str, str]
        expected = {
            "XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR": settings.XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR  # noqa: E501
        }  # type: Dict[str, str]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_apple_mobile_web_app_status_bar_style__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_mobile_web_app_status_bar_style %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = (
            '<meta name="apple-mobile-web-app-status-bar-style" content="default">'
        )  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR="")
    def test_xicon_apple_touch_icon_mask_icon__render__without_color(self) -> None:
        """
        Test templatetag rendering result without icon color setting.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_mobile_web_app_status_bar_style %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAppleMobileWebAppTitleTemplatetagTest(TestCase):
    """
    Apple iOS web application title templatetag tests.
    """

    def test_xicon_apple_mobile_web_app_title__return(self) -> None:
        """
        Test templatetag returning value.
        """

        result = xicon_apple_mobile_web_app_title()  # type: Dict[str, str]
        expected = {
            "XICON_APPLE_MOBILE_WEB_APP_TITLE": settings.XICON_APPLE_MOBILE_WEB_APP_TITLE  # noqa: E501
        }  # type: Dict[str, str]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_apple_mobile_web_app_title__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_mobile_web_app_title %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = (
            '<meta name="apple-mobile-web-app-title" content="Django X Icon">'
        )  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_APPLE_MOBILE_WEB_APP_TITLE="")
    def test_xicon_apple_mobile_web_app_title__render__without_title(self) -> None:
        """
        Test templatetag rendering result without title setting.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_mobile_web_app_title %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconAndroidChromeThemeColorTemplatetagTest(TestCase):
    """
    Android chrome web application toolbar color templatetag tests.
    """

    def test_xicon_android_chrome_theme_color__return(self) -> None:
        """
        Test templatetag returning value.
        """

        result = xicon_android_chrome_theme_color()  # type: Dict[str, str]
        expected = {
            "XICON_ANDROID_CHROME_THEME_COLOR": settings.XICON_ANDROID_CHROME_THEME_COLOR  # noqa: E501
        }  # type: Dict[str, str]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_android_chrome_theme_color__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_android_chrome_theme_color %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = '<meta name="theme-color" content="#00ffff">'  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_ANDROID_CHROME_THEME_COLOR="")
    def test_xicon_android_chrome_theme_color__render__without_color(self) -> None:
        """
        Test templatetag rendering result without title setting.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_android_chrome_theme_color %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconMsapplicationNameTemplatetagTest(TestCase):
    """
    Android microsoft application name templatetag tests.
    """

    def test_xicon_msapplication_name__return(self) -> None:
        """
        Test templatetag returning value.
        """

        result = xicon_msapplication_name()  # type: Dict[str, str]
        expected = {
            "XICON_MSAPPLICATION_NAME": settings.XICON_MSAPPLICATION_NAME
        }  # type: Dict[str, str]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_msapplication_name__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_msapplication_name %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = '<meta name="application-name" content="Django X Icon">'  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_MSAPPLICATION_NAME="")
    def test_xicon_msapplication_name__render__without_name(self) -> None:
        """
        Test templatetag rendering result without title setting.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_msapplication_name %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconMsapplicationTileColorTemplatetagTest(TestCase):
    """
    Android microsoft application tile color templatetag tests.
    """

    def test_xicon_msapplication_tile_color__return(self) -> None:
        """
        Test templatetag returning value.
        """

        result = xicon_msapplication_tile_color()  # type: Dict[str ,str]
        expected = {
            "XICON_MSAPPLICATION_TILE_COLOR": settings.XICON_MSAPPLICATION_TILE_COLOR
        }  # type: Dict[str, str]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_msapplication_tile_color__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_msapplication_tile_color %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = (
            '<meta name="msapplication-TileColor" content="#00ffff">'
        )  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_MSAPPLICATION_TILE_COLOR="")
    def test_xicon_msapplication_name__render__without_name(self) -> None:
        """
        Test templatetag rendering result without title setting.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_msapplication_tile_color %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconMsTileTemplatetagTest(TestCase):
    """
    Microsoft application tile templatetag tests.
    """

    def test_xicon_mstile__return(self) -> None:
        """
        Test templatetag returning value.
        """

        mstile = {
            "src": "mstile-150x150.png",
            "name": "square150x150logo",
        }  # type: Dict[str ,str]
        result = xicon_mstile(mstile=mstile)  # type: Dict[str, Dict[str, str]]
        expected = {"XICON_MSTILE": mstile}  # type: Dict[str, Dict[str, str]]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_mstile__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        mstile = {
            "src": "mstile-150x150.png",
            "name": "square150x150logo",
        }  # type: Dict[str, str]
        context = Context({"XICON_MSTILE": mstile})  # type: Context
        template = Template(
            "{% load xicon_tags %}" "{% xicon_mstile XICON_MSTILE %}"
        )  # type: Template
        result = template.render(context=context)  # type: str
        expected = (
            '<meta name="msapplication-square150x150logo" content="mstile-150x150.png">'
        )  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)


class XiconMsTilesTemplatetagTest(TestCase):
    """
    Microsoft application tiles templatetag tests.
    """

    def test_xicon_mstiles__return(self) -> None:
        """
        Test templatetag returning value.
        """

        result = xicon_mstiles()  # type: Dict[str, Iterable[Dict[str, str]]]
        expected = {
            "XICON_MSAPPLICATION_TILES": settings.XICON_MSAPPLICATION_TILES
        }  # type: Dict[str, List[Dict[str, str]]]

        self.assertIsInstance(obj=result, cls=dict)
        self.assertDictEqual(d1=result, d2=expected)

    def test_xicon_mstiles__render(self) -> None:
        """
        Test templatetag rendering result.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_mstiles %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = """
        <meta name="msapplication-square70x70logo" content="mstile-70x70.png">
        <meta name="msapplication-square150x150logo" content="mstile-150x150.png">
        <meta name="msapplication-wide310x150logo" content="mstile-310x150.png">
        <meta name="msapplication-square310x310logo" content="mstile-310x310.png">
        """  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)

    @override_settings(XICON_MSAPPLICATION_TILES=[])
    def test_xicon_mstiles__render__without_tiles(self) -> None:
        """
        Test templatetag rendering result with empty microsoft application icons list.
        """

        template = Template(
            "{% load xicon_tags %}" "{% xicon_mstiles %}"
        )  # type: Template
        result = template.render(context=Context())  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=result, html2=expected)
