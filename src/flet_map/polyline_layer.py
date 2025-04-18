from dataclasses import field
from typing import List, Optional

import flet as ft

from .map_layer import MapLayer
from .types import MapLatitudeLongitude, SolidStrokePattern, StrokePattern

__all__ = ["PolylineMarker", "PolylineLayer"]


@ft.control("PolylineMarker")
class PolylineMarker(ft.Control):
    """
    A marker for the PolylineLayer.

    -----

    Online docs: https://flet.dev/docs/controls/mappolylinemarker
    """

    coordinates: List[MapLatitudeLongitude]
    colors_stop: Optional[List[ft.Number]] = None
    gradient_colors: Optional[List[ft.ColorValue]] = None
    border_color: ft.OptionalColorValue = None
    color: ft.OptionalColorValue = None
    stroke_width: ft.Number = 1.0
    border_stroke_width: ft.Number = 0.0
    use_stroke_width_in_meter: bool = False
    stroke_pattern: StrokePattern = field(default_factory=lambda: SolidStrokePattern())
    stroke_cap: ft.StrokeCap = ft.StrokeCap.ROUND
    stroke_join: ft.StrokeJoin = ft.StrokeJoin.ROUND

    def before_update(self):
        super().before_update()
        assert (
            self.border_stroke_width >= 0
        ), "border_stroke_width must be greater than or equal to 0"
        assert self.stroke_width >= 0, "stroke_width must be greater than or equal to 0"


@ft.control("PolylineLayer")
class PolylineLayer(MapLayer):
    """
    A layer to display PolylineMarkers.

    -----

    Online docs: https://flet.dev/docs/controls/mappolylinelayer
    """

    polylines: List[PolylineMarker]
    culling_margin: ft.Number = 10.0
    min_hittable_radius: ft.Number = 10.0
    simplify_tolerance: ft.Number = 0.4
