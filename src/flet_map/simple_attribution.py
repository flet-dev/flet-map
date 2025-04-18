from dataclasses import field
from typing import Union

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

    text: Union[str, ft.Text]
    alignment: ft.Alignment = field(default=ft.alignment.bottom_right)
    bgcolor: ft.OptionalColorValue = None
    on_click: ft.OptionalControlEventCallable = None
