import flet as ft

from .map_layer import MapLayer

__all__ = ["SimpleAttribution"]


@ft.control("SimpleAttribution")
class SimpleAttribution(MapLayer):
    """
    A simple attribution layer displayed on the Map.

    -----

    Online docs: https://flet.dev/docs/controls/mapsimpleattribution
    """

    text: str
    alignment: ft.OptionalAlignment = None
    bgcolor: ft.OptionalColorValue = None
    on_click: ft.OptionalControlEventCallable = None
