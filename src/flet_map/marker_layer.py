from dataclasses import field
from typing import List, Optional

import flet as ft

from .map_layer import MapLayer
from .types import MapLatitudeLongitude

__all__ = ["Marker", "MarkerLayer"]


@ft.control("Marker")
class Marker(ft.Control):
    """
    A marker displayed on the Map at the specified location through the MarkerLayer.

    -----

    Online docs: https://flet.dev/docs/controls/mapmarker
    """

    content: ft.Control
    coordinates: MapLatitudeLongitude
    rotate: Optional[bool] = None
    height: ft.Number = 30.0
    width: ft.Number = 30.0
    alignment: ft.OptionalAlignment = None

    def before_update(self):
        super().before_update()
        assert self.content.visible, "content must be visible"
        assert self.height >= 0, "height must be greater than or equal to 0"
        assert self.width >= 0, "width must be greater than or equal to 0"


@ft.control("MarkerLayer")
class MarkerLayer(MapLayer):
    """
    A layer to display Markers.

    -----

    Online docs: https://flet.dev/docs/controls/mapmarkerlayer
    """

    markers: List[Marker]
    alignment: ft.OptionalAlignment = field(
        default_factory=lambda: ft.Alignment.center()
    )
    rotate: bool = False
