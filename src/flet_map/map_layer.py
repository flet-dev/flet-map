import flet as ft

__all__ = ["MapLayer"]


@ft.control("MapLayer")
class MapLayer(ft.Control):
    """
    Abstract class for all map layers.

    The following layers are available:

    - [`CircleLayer`][(p).circle_layer.]
    - [`MarkerLayer`][(p).marker_layer.]
    - [`PolygonLayer`][(p).polygon_layer.]
    - [`PolylineLayer`][(p).polyline_layer.]
    - [`RichAttribution`][(p).rich_attribution.]
    - [`SimpleAttribution`][(p).simple_attribution.]
    - [`TileLayer`][(p).tile_layer.]
    """
