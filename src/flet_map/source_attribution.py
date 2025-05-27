from dataclasses import dataclass

import flet as ft

__all__ = ["ImageSourceAttribution", "SourceAttribution", "TextSourceAttribution"]


@dataclass(kw_only=True)
class SourceAttribution(ft.BaseControl):
    """
    Abstract class for source attribution controls: `ImageSourceAttribution` and `TextSourceAttribution`
    """


@ft.control("ImageSourceAttribution")
class ImageSourceAttribution(SourceAttribution):
    """
    An image attribution permanently displayed adjacent to the open/close icon of a `RichAttribution` control.
    For it to be displayed, it should be part of a `RichAttribution.attributions` list.
    """

    image: ft.Image
    """
    The `Image` to be displayed.
    """

    height: ft.OptionalNumber = 24.0
    """
    The height of the image.
    Should be the same as `RichAttribution.permanent_height`, otherwise layout issues may occur.
    
    Defaults to `24.0`.
    """

    tooltip: ft.OptionalString = None
    """Tooltip text to be displayed when the image is hovered over."""

    on_click: ft.OptionalControlEventCallable = None
    """Fired when this attribution is clicked/pressed."""

    def before_update(self):
        super().before_update()
        assert self.image.visible, "image must be visible"


@ft.control("TextSourceAttribution")
class TextSourceAttribution(SourceAttribution):
    """
    A text source attribution displayed on the Map.
    For it to be displayed, it should be part of a RichAttribution.attributions list.
    """

    text: str
    """The text to display as attribution, styled with `text_style`."""

    text_style: ft.OptionalTextStyle = None
    """Style used to display the `text`."""

    prepend_copyright: bool = True
    """
    Whether to add the '©' character to the start of `text` automatically.
    
    Defaults to `True`.
    """

    on_click: ft.OptionalControlEventCallable = None
    """Fired when this attribution is clicked/pressed."""
