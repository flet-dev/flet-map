from typing import List, Optional

import flet as ft

from .map_layer import MapLayer
from .source_attribution import SourceAttribution
from .types import AttributionAlignment

__all__ = ["RichAttribution"]


@ft.control("RichAttribution")
class RichAttribution(MapLayer):
    """
    An animated and interactive attribution layer that supports both logos/images and text
    (displayed in a popup controlled by an icon button adjacent to the logos).

    -----

    Online docs: https://flet.dev/docs/controls/maprichattribution
    """

    attributions: List[SourceAttribution]
    alignment: Optional[AttributionAlignment] = None
    popup_bgcolor: ft.OptionalColorValue = None
    popup_border_radius: ft.OptionalBorderRadiusValue = None
    popup_initial_display_duration: ft.OptionalDurationValue = None
    permanent_height: ft.Number = 24.0
    show_flutter_map_attribution: bool = True
