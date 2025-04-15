from typing import List

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
    rotate: bool = False
    height: ft.Number = 30.0
    width: ft.Number = 30.0
    alignment: ft.OptionalAlignment = None

    def before_update(self):
        super().before_update()
        assert (
                self.height is None or self.height >= 0
        ), "height must be greater than or equal to 0"
        assert (
                self.width is None or self.width >= 0
        ), "width must be greater than or equal to 0"


@ft.control("MarkerLayer")
class MarkerLayer(MapLayer):
    """
    A layer to display Markers.

    -----

    Online docs: https://flet.dev/docs/controls/mapmarkerlayer
    """

    markers: List[Marker]
    alignment: ft.OptionalAlignment = None
    rotate: bool = False
