# -*- coding: utf-8 -*-

# django-xicon
# xicon/tests/test_views.py


from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse


__all__ = ["MsapplicationBrowserconfigTest"]  # type: list


class MsapplicationBrowserconfigTest(TestCase):
    """
    Microsoft application browserconfig.xml view tests.
    """

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
        response = self.client.get(
            path=reverse("msapplication-browserconfig")
        ).content.decode()

        self.assertInHTML(needle=expected, haystack=response)

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
        response = self.client.get(
            path=reverse("msapplication-browserconfig")
        ).content.decode()

        self.assertInHTML(needle=expected, haystack=response)

    @override_settings(XICON_MSAPPLICATION_TILES="")
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
        response = self.client.get(
            path=reverse("msapplication-browserconfig")
        ).content.decode()

        self.assertInHTML(needle=expected, haystack=response)
