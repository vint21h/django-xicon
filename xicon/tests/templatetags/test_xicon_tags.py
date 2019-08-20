# -*- coding: utf-8 -*-

# django-xicon
# xicon/tests/templatetags/test_xicon_tags.py


from django.template import Context, Template
from django.test import TestCase

from xicon.templatetags.xicon_tags import (
    xicon_favicon,
    xicon_favicons,
    xicon_apple_touch_icon,
    xicon_apple_touch_icons,
)


__all__ = [
    "XiconFaviconTest",
    "XiconFaviconsTest",
    "XiconAppleTouchIconTest",
    "XiconAppleTouchIconsTest",
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