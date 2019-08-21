# -*- coding: utf-8 -*-

# django-xicon
# xicon/tests/templatetags/test_xicon_tags.py


from django.template import Context, Template
from django.test import TestCase
from django.test.utils import override_settings

from xicon.templatetags.xicon_tags import (
    xicon_favicon,
    xicon_favicons,
    xicon_apple_touch_icon,
    xicon_apple_touch_icons,
    xicon_android_chrome_theme_color,
    xicon_apple_mobile_web_app_title,
    xicon_apple_touch_icon_mask_icon,
    xicon_apple_mobile_web_app_status_bar_style,
)


__all__ = [
    "XiconFaviconTest",
    "XiconFaviconsTest",
    "XiconAppleTouchIconTest",
    "XiconAppleTouchIconsTest",
    "XiconAppleTouchMaskIconTest",
    "XiconAppleMobileWebAppStatusBarStyleTest",
    "XiconAppleMobileWebAppTitleTest",
    "XiconAndroidChromeThemeColorTest",
]  # type: list


class XiconFaviconTest(TestCase):
    """
    Favicon templatetag tests.
    """

    def test_xicon_favicon__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        favicon = {
            "src": "favicon.ico",
            "type": "image/x-icon",
            "size": "16x16",
        }  # type: dict
        context = Context({"XICON_FAVICON": favicon})

        self.assertIsInstance(
            obj=xicon_favicon(context=context, favicon=favicon), cls=Context
        )

    def test_xicon_favicon__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        favicon = {
            "src": "favicon.ico",
            "type": "image/x-icon",
            "size": "16x16",
        }  # type: dict
        context = Context({"XICON_FAVICON": favicon})
        template = Template("{% load xicon_tags %}" "{% xicon_favicon XICON_FAVICON %}")
        response = template.render(context)  # type: str
        expected = '<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" sizes="16x16"/>'  # type: str

        self.assertInHTML(needle=expected, haystack=response)

    def test_xicon_favicon__render__without_size(self) -> None:
        """
        Test templatetag rendering result for favicon without size.

        :return: nothing.
        :rtype: None.
        """

        favicon = {"src": "favicon.svg", "type": "image/svg+xml"}  # type: dict
        context = Context({"XICON_FAVICON": favicon})
        template = Template("{% load xicon_tags %}" "{% xicon_favicon XICON_FAVICON %}")
        response = template.render(context)  # type: str
        expected = '<link rel="shortcut icon" href="favicon.svg" type="image/svg+xml" sizes="any"/>'  # type: str

        self.assertInHTML(needle=expected, haystack=response)


class XiconFaviconsTest(TestCase):
    """
    Favicons templatetag tests.
    """

    def test_xicon_favicons__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        context = Context()

        self.assertIsInstance(obj=xicon_favicons(context=context), cls=Context)

    def test_xicon_favicons__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template("{% load xicon_tags %}" "{% xicon_favicons %}")
        response = template.render(context)  # type: str
        expected = """
        <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" sizes="16x16"/>
        <link rel="shortcut icon" href="favicon.png" type="image/png" sizes="32x32"/>
        <link rel="shortcut icon" href="favicon.svg" type="image/svg+xml" sizes="any"/>
        """  # type: str

        self.assertInHTML(needle=expected, haystack=response)


class XiconAppleTouchIconTest(TestCase):
    """
    Apple touch icon templatetag tests.
    """

    def test_xicon_apple_touch_icon__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        apple_touch_icon = {
            "src": "apple-touch-icon-57x57.png",
            "size": "57x57",
        }  # type: dict
        context = Context({"XICON_APPLE_TOUCH_ICON": apple_touch_icon})

        self.assertIsInstance(
            obj=xicon_apple_touch_icon(
                context=context, apple_touch_icon=apple_touch_icon
            ),
            cls=Context,
        )

    def test_xicon_apple_touch_icon__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        apple_touch_icon = {
            "src": "apple-touch-icon-57x57.png",
            "size": "57x57",
        }  # type: dict
        context = Context({"XICON_APPLE_TOUCH_ICON": apple_touch_icon})
        template = Template(
            "{% load xicon_tags %}"
            "{% xicon_apple_touch_icon XICON_APPLE_TOUCH_ICON %}"
        )
        response = template.render(context)  # type: str
        expected = '<link rel="apple-touch-icon" href="apple-touch-icon-57x57.png" sizes="57x57"/>'  # type: str

        self.assertInHTML(needle=expected, haystack=response)

    def test_xicon_apple_touch_icon__render__without_size(self) -> None:
        """
        Test templatetag rendering result for icon without size.

        :return: nothing.
        :rtype: None.
        """

        apple_touch_icon = {"src": "apple-touch-icon.png"}  # type: dict
        context = Context({"XICON_APPLE_TOUCH_ICON": apple_touch_icon})
        template = Template(
            "{% load xicon_tags %}"
            "{% xicon_apple_touch_icon XICON_APPLE_TOUCH_ICON %}"
        )
        response = template.render(context)  # type: str
        expected = (
            '<link rel="apple-touch-icon" href="apple-touch-icon.png"/>'
        )  # type: str

        self.assertInHTML(needle=expected, haystack=response)


class XiconAppleTouchIconsTest(TestCase):
    """
    Apple touch icons templatetag tests.
    """

    def test_xicon_apple_touch_icons__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        context = Context()

        self.assertIsInstance(obj=xicon_apple_touch_icons(context=context), cls=Context)

    def test_xicon_apple_touch_icons__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template("{% load xicon_tags %}" "{% xicon_apple_touch_icons %}")
        response = template.render(context)  # type: str
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
        """  # type: str

        self.assertInHTML(needle=expected, haystack=response)


class XiconAppleTouchMaskIconTest(TestCase):
    """
    Apple touch mask icon templatetag tests.
    """

    def test_xicon_xicon_apple_touch_icon_mask_icon__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        context = Context()

        self.assertIsInstance(
            obj=xicon_apple_touch_icon_mask_icon(context=context), cls=Context
        )

    def test_xicon_xicon_apple_touch_icon_mask_icon__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_touch_icon_mask_icon %}"
        )
        response = template.render(context)  # type: str
        expected = (
            '<link rel="mask-icon" href="apple-touch-icon.png" color="#00ffff">'
        )  # type: str

        self.assertInHTML(needle=expected, haystack=response)

    @override_settings(XICON_APPLE_TOUCH_ICON_MASK_ICON_SRC="")
    def test_xicon_xicon_apple_touch_icon_mask_icon__render__without_src(self) -> None:
        """
        Test templatetag rendering result without icon source setting.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_touch_icon_mask_icon %}"
        )
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)

    @override_settings(XICON_APPLE_TOUCH_ICON_MASK_ICON_COLOR="")
    def test_xicon_xicon_apple_touch_icon_mask_icon__render__without_color(
        self
    ) -> None:
        """
        Test templatetag rendering result without icon color setting.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_touch_icon_mask_icon %}"
        )
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)


class XiconAppleMobileWebAppStatusBarStyleTest(TestCase):
    """
    Apple iOS web application status bar style templatetag tests.
    """

    def test_xicon_apple_mobile_web_app_status_bar_style__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        context = Context()

        self.assertIsInstance(
            obj=xicon_apple_mobile_web_app_status_bar_style(context=context),
            cls=Context,
        )

    def test_xicon_apple_mobile_web_app_status_bar_style__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_mobile_web_app_status_bar_style %}"
        )
        response = template.render(context)  # type: str
        expected = (
            '<meta name="apple-mobile-web-app-status-bar-style" content="default">'
        )  # type: str

        self.assertInHTML(needle=expected, haystack=response)

    @override_settings(XICON_APPLE_MOBILE_WEB_APP_STATUS_BAR_STYLE_COLOR="")
    def test_xicon_apple_touch_icon_mask_icon__render__without_color(self) -> None:
        """
        Test templatetag rendering result without icon color setting.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_mobile_web_app_status_bar_style %}"
        )
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)


class XiconAppleMobileWebAppTitleTest(TestCase):
    """
    Apple iOS web application title templatetag tests.
    """

    def test_xicon_apple_mobile_web_app_title__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        context = Context()

        self.assertIsInstance(
            obj=xicon_apple_mobile_web_app_title(context=context), cls=Context
        )

    def test_xicon_apple_mobile_web_app_title__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_mobile_web_app_title %}"
        )
        response = template.render(context)  # type: str
        expected = (
            '<meta name="apple-mobile-web-app-title" content="Django X Icon">'
        )  # type: str

        self.assertInHTML(needle=expected, haystack=response)

    @override_settings(XICON_APPLE_MOBILE_WEB_APP_TITLE="")
    def test_xicon_apple_mobile_web_app_title__render__without_title(self) -> None:
        """
        Test templatetag rendering result without title setting.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_apple_mobile_web_app_title %}"
        )
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)


class XiconAndroidChromeThemeColorTest(TestCase):
    """
    Android chrome web application toolbar color templatetag tests.
    """

    def test_xicon_android_chrome_theme_color__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        context = Context()

        self.assertIsInstance(
            obj=xicon_android_chrome_theme_color(context=context), cls=Context
        )

    def test_xicon_android_chrome_theme_color__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_android_chrome_theme_color %}"
        )
        response = template.render(context)  # type: str
        expected = '<meta name="theme-color" content="#00ffff">'  # type: str

        self.assertInHTML(needle=expected, haystack=response)

    @override_settings(XICON_ANDROID_CHROME_THEME_COLOR="")
    def test_xicon_android_chrome_theme_color__render__without_color(self) -> None:
        """
        Test templatetag rendering result without title setting.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_android_chrome_theme_color %}"
        )
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)
