# -*- coding: utf-8 -*-

# django-xicon
# tests/templatetags/test_xicon_tags.py


from django.template import Context, Template
from django.test import TestCase
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
]  # type: list


class XiconFaviconTemplatetagTest(TestCase):
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

        self.assertHTMLEqual(html1=response, html2=expected)

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

        self.assertHTMLEqual(html1=response, html2=expected)


class XiconFaviconsTemplatetagTest(TestCase):
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

        self.assertHTMLEqual(html1=response, html2=expected)

    @override_settings(XICON_FAVICONS=[])
    def test_xicon_favicons__render__without_favicons(self) -> None:
        """
        Test templatetag rendering result with empty favicons list.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template("{% load xicon_tags %}" "{% xicon_favicons %}")
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)


class XiconAppleTouchIconTemplatetagTest(TestCase):
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

        self.assertHTMLEqual(html1=response, html2=expected)

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

        self.assertHTMLEqual(html1=response, html2=expected)


class XiconAppleTouchIconsTemplatetagTest(TestCase):
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

        self.assertHTMLEqual(html1=response, html2=expected)

    @override_settings(XICON_APPLE_TOUCH_ICONS=[])
    def test_xicon_apple_touch_icons__render__without_apple_touch_icons(self) -> None:
        """
        Test templatetag rendering result with empty apple touch icons list.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template("{% load xicon_tags %}" "{% xicon_apple_touch_icons %}")
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)


class XiconAppleTouchMaskIconTemplatetagTest(TestCase):
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

        self.assertHTMLEqual(html1=response, html2=expected)

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


class XiconAppleMobileWebAppStatusBarStyleTemplatetagTest(TestCase):
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

        self.assertHTMLEqual(html1=response, html2=expected)

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


class XiconAppleMobileWebAppTitleTemplatetagTest(TestCase):
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

        self.assertHTMLEqual(html1=response, html2=expected)

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


class XiconAndroidChromeThemeColorTemplatetagTest(TestCase):
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

        self.assertHTMLEqual(html1=response, html2=expected)

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


class XiconMsapplicationNameTemplatetagTest(TestCase):
    """
    Android microsoft application name templatetag tests.
    """

    def test_xicon_msapplication_name__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        context = Context()

        self.assertIsInstance(
            obj=xicon_msapplication_name(context=context), cls=Context
        )

    def test_xicon_msapplication_name__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template("{% load xicon_tags %}" "{% xicon_msapplication_name %}")
        response = template.render(context)  # type: str
        expected = '<meta name="application-name" content="Django X Icon">'  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)

    @override_settings(XICON_MSAPPLICATION_NAME="")
    def test_xicon_msapplication_name__render__without_name(self) -> None:
        """
        Test templatetag rendering result without title setting.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template("{% load xicon_tags %}" "{% xicon_msapplication_name %}")
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)


class XiconMsapplicationTileColorTemplatetagTest(TestCase):
    """
    Android microsoft application tile color templatetag tests.
    """

    def test_xicon_msapplication_tile_color__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        context = Context()

        self.assertIsInstance(
            obj=xicon_msapplication_tile_color(context=context), cls=Context
        )

    def test_xicon_msapplication_tile_color__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_msapplication_tile_color %}"
        )
        response = template.render(context)  # type: str
        expected = (
            '<meta name="msapplication-TileColor" content="#00ffff">'
        )  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)

    @override_settings(XICON_MSAPPLICATION_TILE_COLOR="")
    def test_xicon_msapplication_name__render__without_name(self) -> None:
        """
        Test templatetag rendering result without title setting.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template(
            "{% load xicon_tags %}" "{% xicon_msapplication_tile_color %}"
        )
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)


class XiconMsTileTemplatetagTest(TestCase):
    """
    Microsoft application tile templatetag tests.
    """

    def test_xicon_mstile__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        mstile = {
            "src": "mstile-150x150.png",
            "name": "square150x150logo",
        }  # type: dict
        context = Context({"XICON_MSTILE": mstile})

        self.assertIsInstance(
            obj=xicon_mstile(context=context, mstile=mstile), cls=Context
        )

    def test_xicon_mstile__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        mstile = {
            "src": "mstile-150x150.png",
            "name": "square150x150logo",
        }  # type: dict
        context = Context({"XICON_MSTILE": mstile})
        template = Template("{% load xicon_tags %}" "{% xicon_mstile XICON_MSTILE %}")
        response = template.render(context)  # type: str
        expected = (
            '<meta name="msapplication-square150x150logo" content="mstile-150x150.png">'
        )  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)


class XiconMsTilesTemplatetagTest(TestCase):
    """
    Microsoft application tiles templatetag tests.
    """

    def test_xicon_mstiles__return_context(self) -> None:
        """
        Test templatetag returning context.

        :return: nothing.
        :rtype: None.
        """

        context = Context()

        self.assertIsInstance(obj=xicon_mstiles(context=context), cls=Context)

    def test_xicon_mstiles__render(self) -> None:
        """
        Test templatetag rendering result.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template("{% load xicon_tags %}" "{% xicon_mstiles %}")
        response = template.render(context)  # type: str
        expected = """
        <meta name="msapplication-square70x70logo" content="mstile-70x70.png">
        <meta name="msapplication-square150x150logo" content="mstile-150x150.png">
        <meta name="msapplication-wide310x150logo" content="mstile-310x150.png">
        <meta name="msapplication-square310x310logo" content="mstile-310x310.png">
        """  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)

    @override_settings(XICON_MSAPPLICATION_TILES=[])
    def test_xicon_mstiles__render__without_tiles(self) -> None:
        """
        Test templatetag rendering result with empty microsoft application icons list.

        :return: nothing.
        :rtype: None.
        """

        context = Context()
        template = Template("{% load xicon_tags %}" "{% xicon_mstiles %}")
        response = template.render(context)  # type: str
        expected = ""  # type: str

        self.assertHTMLEqual(html1=response, html2=expected)
