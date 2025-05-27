from dataclasses import field
from typing import List, Optional

import flet as ft

from .map_layer import MapLayer
from .types import MapLatitudeLongitude, SolidStrokePattern, StrokePattern

__all__ = ["PolylineMarker", "PolylineLayer"]


@ft.control("PolylineMarker")
class PolylineMarker(ft.Control):
    """
    A marker for the `PolylineLayer`.
    """

    coordinates: List[MapLatitudeLongitude]
    """
    The list of coordinates for the Polyline.
    """

    colors_stop: Optional[List[ft.Number]] = None
    """
    The stops for the `gradient_colors`.
    """

    gradient_colors: Optional[List[ft.ColorValue]] = None
    """
    The List of colors in case a gradient should get used.
    """

    border_color: ft.ColorValue = ft.Colors.YELLOW
    """
    The border's color.
    
    Defaults to `ft.Colors.YELLOW`.
    """

    color: ft.ColorValue = ft.Colors.YELLOW
    """
    The color of the line stroke.
    
    Defaults to `ft.Colors.YELLOW`.
    """

    stroke_width: ft.Number = 1.0
    """
    The width of the stroke.
    
    Defaults to `1.0`.
    """

    border_stroke_width: ft.Number = 0.0
    """
    The width of the stroke with of the line border.
    
    Defaults to `0.0` (disabled).
    """

    use_stroke_width_in_meter: bool = False
    """
    Whether the stroke's width should have meters as unit.
    
    Defaults to `False`.
    """

    stroke_pattern: StrokePattern = field(default_factory=lambda: SolidStrokePattern())
    """
    Determines whether the line should be solid, dotted, or dashed, and the
    exact characteristics of each.
    
    Defaults to `SolidStrokePattern()`.
    """

    stroke_cap: ft.StrokeCap = ft.StrokeCap.ROUND
    """
    Style to use for line endings.
    
    Defaults to `ft.StrokeCap.ROUND`.
    """

    stroke_join: ft.StrokeJoin = ft.StrokeJoin.ROUND
    """
    Style to use for line segment joins.
    
    Defaults to `ft.StrokeJoin.ROUND`.
    """

    def before_update(self):
        super().before_update()
        assert (
            self.border_stroke_width >= 0
        ), "border_stroke_width must be greater than or equal to 0"
        assert self.stroke_width >= 0, "stroke_width must be greater than or equal to 0"


@ft.control("PolylineLayer")
class PolylineLayer(MapLayer):
    """
    A layer to display `PolylineMarker`s.
    """

    polylines: List[PolylineMarker]
    """
    List polylines to be drawn. 
    """

    culling_margin: ft.Number = 10.0
    """
    Acceptable extent outside of viewport before culling polyline segments.
    
    Defaults to `10.0`.
    """

    min_hittable_radius: ft.Number = 10.0
    """
    The minimum radius of the hittable area around each `Polyline` in logical pixels.
    
    The entire visible area is always hittable, but if the visible area is
    smaller than this, then this will be the hittable area.
    
    Defaults to `10.0`.
    """

    simplify_tolerance: ft.Number = 0.3
    """
    Defaults to `0.3`.
    """
