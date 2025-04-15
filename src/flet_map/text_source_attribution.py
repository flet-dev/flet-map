import flet as ft

__all__ = ["TextSourceAttribution"]


@ft.control("TextSourceAttribution")
class TextSourceAttribution(ft.Control):
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
