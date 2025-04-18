from typing import List

import flet as ft

from .map_layer import MapLayer
from .types import MapLatitudeLongitude

__all__ = ["CircleMarker", "CircleLayer"]


@ft.control("CircleMarker")
class CircleMarker(ft.Control):
    """
    A circular marker displayed on the Map at the specified location through the CircleLayer.

    -----

    Online docs: https://flet.dev/docs/controls/mapcirclemarker
    """

    radius: ft.Number
    coordinates: MapLatitudeLongitude
    color: ft.OptionalColorValue = None
    border_color: ft.OptionalColorValue = None
    border_stroke_width: ft.Number = 0.0
    use_radius_in_meter: bool = False

    def before_update(self):
        super().before_update()
        assert (
            self.border_stroke_width >= 0
        ), "border_stroke_width must be greater than or equal to 0"


@ft.control("CircleLayer")
class CircleLayer(MapLayer):
    """
    A layer to display CircleMarkers.

    -----

    Online docs: https://flet.dev/docs/controls/mapcirclelayer
    """

    circles: List[CircleMarker]
