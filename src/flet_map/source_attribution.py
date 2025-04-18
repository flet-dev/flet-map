from dataclasses import dataclass

import flet as ft

__all__ = ["ImageSourceAttribution", "SourceAttribution", "TextSourceAttribution"]


@dataclass(kw_only=True)
class SourceAttribution(ft.BaseControl):
    pass


@ft.control("ImageSourceAttribution")
class ImageSourceAttribution(SourceAttribution):
    """
    An image attribution permanently displayed adjacent to the open/ close icon of a RichAttribution control.
    For it to be displayed, it should be part of a RichAttribution.attributions list.

    -----

    Online docs: https://flet.dev/docs/controls/mapimagesourceattribution
    """

    content: ft.Image
    height: ft.OptionalNumber = 24.0
    tooltip: ft.OptionalString = None
    on_click: ft.OptionalControlEventCallable = None

    def before_update(self):
        super().before_update()
        assert self.content.visible, "content must be visible"


@ft.control("TextSourceAttribution")
class TextSourceAttribution(SourceAttribution):
    """
    A text source attribution displayed on the Map.
    For it to be displayed, it should be part of a RichAttribution.attributions list.

    -----

    Online docs: https://flet.dev/docs/controls/maptextsourceattribution
    """

    text: str
    text_style: ft.OptionalTextStyle = None
    prepend_copyright: bool = True
    on_click: ft.OptionalControlEventCallable = None
