from typing import Dict, List, Optional

import flet as ft

from .map_layer import MapLayer
from .types import MapLatitudeLongitudeBounds, MapTileLayerEvictErrorTileStrategy

__all__ = ["TileLayer"]


@ft.control("TileLayer")
class TileLayer(MapLayer):
    """
    The Map's main layer.
    Displays square raster images in a continuous grid, sourced from the provided utl_template.

    -----

    Online docs: https://flet.dev/docs/controls/maptilelayer
    """

    url_template: str
    fallback_url: Optional[str] = None
    subdomains: Optional[List[str]] = None
    tile_bounds: Optional[MapLatitudeLongitudeBounds] = None
    tile_size: ft.Number = 256.0
    min_native_zoom: int = 0
    max_native_zoom: int = 19
    zoom_reverse: bool = False
    zoom_offset: ft.Number = 0.0
    keep_buffer: int = 2
    pan_buffer: int = 2
    enable_tms: bool = False
    keep_alive: Optional[bool] = None
    enable_retina_mode: bool = False
    additional_options: Optional[Dict[str, str]] = None
    max_zoom: ft.Number = float("inf")
    min_zoom: ft.Number = 0.0
    error_image_src: Optional[str] = None
    evict_error_tile_strategy: Optional[MapTileLayerEvictErrorTileStrategy] = None
    on_image_error: ft.OptionalControlEventCallable = None

    def before_update(self):
        super().before_update()
        assert self.tile_size >= 0, "tile_size cannot be negative"
        assert (
                self.min_native_zoom >= 0
        ), "min_native_zoom must be greater than or equal to 0"
        assert (
                self.max_native_zoom >= 0
        ), "max_native_zoom must be greater than or equal to 0"
        assert self.zoom_offset >= 0, "zoom_offset must be greater than or equal to 0"
        assert self.max_zoom >= 0, "max_zoom must be greater than or equal to 0"
        assert self.min_zoom >= 0, "min_zoom must be greater than or equal to 0"
