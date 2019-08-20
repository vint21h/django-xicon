# -*- coding: utf-8 -*-

# django-xicon
# xicon/tests/templatetags/test_xicon_tags.py


from django.template import Context, Template
from django.test import TestCase

from xicon.templatetags.xicon_tags import xicon_favicon


__all__ = ["XiconFaviconTest"]  # type: list


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
        rendered = template.render(context)  # type: str
        result = '<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" sizes="16x16"/>'  # type: str

        self.assertInHTML(needle=result, haystack=rendered)

    def test_xicon_favicon__render__without_size(self) -> None:
        """
        Test templatetag rendering result for favicon without size.

        :return: nothing.
        :rtype: None.
        """

        favicon = {"src": "favicon.svg", "type": "image/svg+xml"}  # type: dict
        context = Context({"XICON_FAVICON": favicon})
        template = Template("{% load xicon_tags %}" "{% xicon_favicon XICON_FAVICON %}")
        rendered = template.render(context)  # type: str
        result = '<link rel="shortcut icon" href="favicon.svg" type="image/svg+xml" sizes="any"/>'  # type: str

        self.assertInHTML(needle=result, haystack=rendered)
