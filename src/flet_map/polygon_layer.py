from typing import List, Optional

import flet as ft

from .map_layer import MapLayer
from .types import MapLatitudeLongitude

__all__ = ["PolygonMarker", "PolygonLayer"]


@ft.control("PolygonMarker")
class PolygonMarker(ft.Control):
    """
    A marker for the PolygonLayer.

    -----

    Online docs: https://flet.dev/docs/controls/mappolygonmarker
    """

    coordinates: List[MapLatitudeLongitude]
    label: Optional[str] = None
    label_text_style: ft.OptionalTextStyle = None
    border_color: ft.OptionalColorValue = None
    color: ft.OptionalColorValue = None
    border_stroke_width: ft.Number = 0
    disable_holes_border: bool = False
    rotate_label: bool = False
    stroke_cap: ft.StrokeCap = ft.StrokeCap.ROUND
    stroke_join: ft.StrokeJoin = ft.StrokeJoin.ROUND

    def before_update(self):
        super().before_update()
        assert (
            self.border_stroke_width >= 0
        ), "border_stroke_width must be greater than or equal to 0"


@ft.control("PolygonLayer")
class PolygonLayer(MapLayer):
    """
    A layer to display PolygonMarkers.

    -----

    Online docs: https://flet.dev/docs/controls/mappolygonlayer
    """

    polygons: List[PolygonMarker]
    polygon_culling: bool = False
    polygon_labels: bool = True
    draw_labels_last: bool = False
    simplification_tolerance: ft.Number = 0.5
    use_alternative_rendering: bool = False
