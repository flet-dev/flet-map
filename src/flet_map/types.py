from dataclasses import dataclass, field
from enum import Enum, IntFlag
from typing import List, Optional

import flet as ft

__all__ = [
    "MapTileLayerEvictErrorTileStrategy",
    "AttributionAlignment",
    "PatternFit",
    "MapCamera",
    "StrokePattern",
    "SolidStrokePattern",
    "DashedStrokePattern",
    "DottedStrokePattern",
    "MapLatitudeLongitude",
    "MapLatitudeLongitudeBounds",
    "MapInteractiveFlag",
    "MapMultiFingerGesture",
    "MapInteractionConfiguration",
    "MapEventSource",
    "MapCameraFit",
    "MapTapEvent",
    "MapHoverEvent",
    "MapPositionChangeEvent",
    "MapPointerEvent",
    "MapEvent",
    "TileDisplay",
    "InstantaneousTileDisplay",
    "FadeInTileDisplay",
]


class MapTileLayerEvictErrorTileStrategy(Enum):
    """Strategies on how to handle tile errors"""

    NONE = "none"
    """Never evict images for tiles which failed to load."""

    DISPOSE = "dispose"
    """Evict images for tiles which failed to load when they are pruned."""

    NOT_VISIBLE = "notVisible"
    """
    Evict images for tiles which failed to load and:
        - do not belong to the current zoom level AND/OR
        - are not visible
    """

    NOT_VISIBLE_RESPECT_MARGIN = "notVisibleRespectMargin"
    """
    Evict images for tiles which failed to load and:
        - do not belong to the current zoom level AND/OR
        - are not visible, respecting the pruning buffer (the maximum of the `keep_buffer` and `pan_buffer`).
    """


class AttributionAlignment(Enum):
    """Position to anchor `RichAttribution` control relative to the map."""

    BOTTOM_LEFT = "bottomLeft"
    """The bottom left corner."""

    BOTTOM_RIGHT = "bottomRight"
    """The bottom right corner."""


class PatternFit(Enum):
    """
    Determines how a non-solid [StrokePattern] should be fit to a line
    when their lengths are not equal or multiples
    """

    NONE = "none"
    """
    Don't apply any specific fit to the pattern - repeat exactly as specified,
    and stop when the last point is reached.
    
    Not recommended, as it may leave a gap between the final segment and the last
    point, making it unclear where the line ends.
    """

    SCALE_DOWN = "scaleDown"
    """
    Scale the pattern to ensure it fits an integer number of times into the
    polyline (smaller version regarding rounding, cf. `SCALE_UP`)
    """

    SCALE_UP = "scaleUp"
    """
    Scale the pattern to ensure it fits an integer number of times into the
    polyline (bigger version regarding rounding, cf. `SCALE_DOWN`)
    """

    APPEND_DOT = "appendDot"
    """
    Uses the pattern exactly, truncating the final dash if it does not fit, or
    adding a single dot at the last point if the final dash does not reach the
    last point (there is a gap at that location).
    """

    EXTEND_FINAL_DASH = "extendFinalDash"
    """
    Uses the pattern exactly, truncating the final dash if it does not fit, or
    extending the final dash to the last point if it would not normally reach
    that point (there is a gap at that location).
    
    Only useful when working with `DashedStrokePattern`. 
    Similar to `APPEND_DOT` for `DottedStrokePattern`.
    """


@dataclass
class MapCamera:
    center: "MapLatitudeLongitude"
    """
    The center of this camera.
    """

    zoom: ft.Number
    """
    Defines how far this camera is zoomed.
    """

    min_zoom: ft.Number
    """
    The minimum allowed zoom level.
    """

    max_zoom: ft.Number
    """
    The maximum allowed zoom level.
    """

    rotation: ft.Number
    """
    The rotation (in degrees) of the camera.
    """


@dataclass(kw_only=True)
class StrokePattern:
    """
    Determines whether a stroke should be solid, dotted, or dashed,
    and the exact characteristics of each.

    This is an abstract class and shouldn't be used directly.
    See usable derivatives: `SolidStrokePattern`, `DashedStrokePattern` and `DottedStrokePattern`.
    """

    _type: str = ""


@dataclass
class SolidStrokePattern(StrokePattern):
    """A solid/unbroken stroke pattern."""

    def __post_init__(self):
        self._type = "solid"


@dataclass
class DashedStrokePattern(StrokePattern):
    segments: List[ft.Number] = field(default_factory=list)
    pattern_fit: PatternFit = PatternFit.SCALE_UP
    """
    Determines how this stroke pattern should be fit to a line when their lengths are not equal or multiples.

    Defaults to `PatternFit.SCALE_UP`.
    """

    def __post_init__(self):
        assert len(self.segments) >= 2, "segments must contain at least two items"
        assert len(self.segments) % 2 == 0, "segments must have an even length"
        self._type = "dashed"


@dataclass
class DottedStrokePattern(StrokePattern):
    """A stroke pattern of circular dots, spaced with `spacing_factor`."""

    spacing_factor: ft.Number = 1.5
    """
    The multiplier used to calculate the spacing between dots in a dotted polyline, 
    with respect to `Polyline.stroke_width` / `Polygon.border_stroke_width`.
    A value of `1.0` will result in spacing equal to the `stroke_width`. 
    Increasing the value increases the spacing with the same scaling.
    
    May also be scaled by the use of `PatternFit.SCALE_UP`.
    
    Defaults to `1.5`.
    """
    pattern_fit: PatternFit = PatternFit.SCALE_UP
    """
    Determines how this stroke pattern should be fit to a line when their lengths are not equal or multiples.

    Defaults to `PatternFit.SCALE_UP`.
    """

    def __post_init__(self):
        assert (
            self.spacing_factor > 0
        ), "spacing_factor must be greater than or equal to 0.0"
        self._type = "dotted"


@dataclass
class MapLatitudeLongitude:
    """Map coordinates in degrees."""

    latitude: ft.Number
    """The latitude point of this coordinate."""

    longitude: ft.Number
    """The longitude point of this coordinate."""


@dataclass
class MapLatitudeLongitudeBounds:
    """
    Both corners have to be on opposite sites, but it doesn't matter
    which opposite corners or in what order the corners are provided.
    """

    corner_1: MapLatitudeLongitude
    """The corner 1."""

    corner_2: MapLatitudeLongitude
    """The corner 2."""


class MapInteractiveFlag(IntFlag):
    """
    Flags to enable/disable certain interaction events on the map.

    Example:
        - `MapInteractiveFlag.ALL` enables all events
        - `MapInteractiveFlag.NONE` disables all events
    """

    NONE = 0
    """No interaction."""

    DRAG = 1 << 0
    """Panning with a single finger or cursor."""

    FLING_ANIMATION = 1 << 1
    """Fling animation after panning if velocity is great enough."""

    PINCH_MOVE = 1 << 2
    """Panning with multiple fingers."""

    PINCH_ZOOM = 1 << 3
    """Zooming with a multi-finger pinch gesture."""

    DOUBLE_TAP_ZOOM = 1 << 4
    """Zooming with a single-finger double tap gesture."""

    DOUBLE_TAP_DRAG_ZOOM = 1 << 5
    """Zooming with a single-finger double-tap-drag gesture."""

    SCROLL_WHEEL_ZOOM = 1 << 6
    """Zooming with a mouse scroll wheel."""

    ROTATE = 1 << 7
    """Rotation with two-finger twist gesture."""

    ALL = (
        (1 << 0)
        | (1 << 1)
        | (1 << 2)
        | (1 << 3)
        | (1 << 4)
        | (1 << 5)
        | (1 << 6)
        | (1 << 7)
    )
    """All available interactive flags."""

    @staticmethod
    def has_flag(left_flags: int, right_flags: int) -> bool:
        """
        Returns `True` if `left_flags` has at least one member in `right_flags` (intersection).
        """
        return left_flags & right_flags != 0

    @staticmethod
    def has_multi_finger(flags: int) -> bool:
        """
        return Returns `True` if any multi-finger gesture flags
        (`MapMultiFingerGesture.PINCH_MOVE`, `MapMultiFingerGesture.PINCH_ZOOM`, `MapMultiFingerGesture.ROTATE`) are enabled.
        """
        return MapInteractiveFlag.has_flag(
            flags,
            (
                MapMultiFingerGesture.PINCH_MOVE
                | MapMultiFingerGesture.PINCH_ZOOM
                | MapMultiFingerGesture.ROTATE
            ),
        )

    @staticmethod
    def has_drag(flags: int) -> bool:
        """Returns `True` if the `DRAG` interactive flag is enabled."""
        return MapInteractiveFlag.has_flag(flags, MapInteractiveFlag.DRAG)

    @staticmethod
    def has_fling_animation(flags: int) -> bool:
        """Returns `True` if the `FLING_ANIMATION` interactive flag is enabled."""
        return MapInteractiveFlag.has_flag(flags, MapInteractiveFlag.FLING_ANIMATION)

    @staticmethod
    def has_pinch_move(flags: int) -> bool:
        """Returns `True` if the `PINCH_MOVE` interactive flag is enabled."""
        return MapInteractiveFlag.has_flag(flags, MapInteractiveFlag.PINCH_MOVE)

    @staticmethod
    def has_fling_pinch_zoom(flags: int) -> bool:
        """Returns `True` if the `PINCH_ZOOM` interactive flag is enabled."""
        return MapInteractiveFlag.has_flag(flags, MapInteractiveFlag.PINCH_ZOOM)

    @staticmethod
    def has_double_tap_drag_zoom(flags: int) -> bool:
        """Returns `True` if the `DOUBLE_TAP_DRAG_ZOOM` interactive flag is enabled."""
        return MapInteractiveFlag.has_flag(
            flags, MapInteractiveFlag.DOUBLE_TAP_DRAG_ZOOM
        )

    @staticmethod
    def has_double_tap_zoom(flags: int) -> bool:
        """Returns `True` if the `DOUBLE_TAP_ZOOM` interactive flag is enabled."""
        return MapInteractiveFlag.has_flag(flags, MapInteractiveFlag.DOUBLE_TAP_ZOOM)

    @staticmethod
    def has_rotate(flags: int) -> bool:
        """Returns `True` if the `ROTATE` interactive flag is enabled."""
        return MapInteractiveFlag.has_flag(flags, MapInteractiveFlag.ROTATE)

    @staticmethod
    def has_scroll_wheel_zoom(flags: int) -> bool:
        """Returns `True` if the `SCROLL_WHEEL_ZOOM` interactive flag is enabled."""
        return MapInteractiveFlag.has_flag(flags, MapInteractiveFlag.SCROLL_WHEEL_ZOOM)


class MapMultiFingerGesture(IntFlag):
    NONE = 0
    PINCH_MOVE = 1 << 0
    PINCH_ZOOM = 1 << 1
    ROTATE = 1 << 2
    ALL = (1 << 0) | (1 << 1) | (1 << 2)


@dataclass
class MapInteractionConfiguration:
    enable_multi_finger_gesture_race: bool = False
    """
    If `True` then `rotation_threshold` and `pinch_zoom_threshold` and `pinch_move_threshold` will race.
    If multiple gestures win at the same time, then precedence: `pinch_zoom_win_gestures` > `rotation_win_gestures` > `pinch_move_win_gestures`
    
    Defaults to `False`.
    """

    pinch_move_threshold: ft.Number = 40.0
    """
    Map starts to move when `pinch_move_threshold` has been achieved or another multi finger gesture wins which allows MultiFingerGesture.pinchMove.
    
    Note: if `interactive_flags` doesn't contain InteractiveFlag.pinchMove or enableMultiFingerGestureRace is false then pinch move cannot win
    
    Defaults to `False`.
    """

    scroll_wheel_velocity: ft.Number = 0.005
    """
    The used velocity how fast the map should zoom in or out by scrolling with the scroll wheel of a mouse.
    
    Defaults to `0.005`.
    """

    pinch_zoom_threshold: ft.Number = 0.5
    """
    Map starts to zoom when pinchZoomThreshold has been achieved or another multi finger gesture wins which allows MultiFingerGesture.pinchZoom 
    
    Note: if MapOptions.interactiveFlags.flags doesn't contain InteractiveFlag.pinchZoom or enableMultiFingerGestureRace is false then zoom cannot win.
    
    Defaults to `0.5`.
    """

    rotation_threshold: ft.Number = 20.0
    """
    Map starts to rotate when `rotation_threshold` has been achieved or another multi finger gesture wins which allows MultiFingerGesture.rotate.
    
    Note: if MapOptions.interactiveFlags.flags doesn't contain InteractiveFlag.rotate or enableMultiFingerGestureRace is false then rotate cannot win.
    
    Defaults to `20.0`.
    """

    flags: MapInteractiveFlag = MapInteractiveFlag.ALL
    """
    Defines the map events to be enabled/disabled.
    
    Defaults to `MapInteractiveFlag.ALL`.
    """

    rotation_win_gestures: MapMultiFingerGesture = MapMultiFingerGesture.ROTATE
    """
    When `rotation_threshold` wins over pinchZoomThreshold and `pinch_move_threshold` then rotationWinGestures gestures will be used. 
    By default only MultiFingerGesture.rotate gesture will take effect see MultiFingerGesture for custom settings
    
    Defaults to `MapMultiFingerGesture.ROTATE`.
    """

    pinch_move_win_gestures: MapMultiFingerGesture = (
        MapMultiFingerGesture.PINCH_ZOOM | MapMultiFingerGesture.PINCH_MOVE
    )
    """
    When `pinch_move_threshold` wins over `rotation_threshold` and pinchZoomThreshold then pinchMoveWinGestures gestures will be used. 
    By default MultiFingerGesture.pinchMove and MultiFingerGesture.pinchZoom gestures will take effect see MultiFingerGesture for custom settings
    
    Defaults to `MapMultiFingerGesture.PINCH_ZOOM | MapMultiFingerGesture.PINCH_MOVE`.
    """

    pinch_zoom_win_gestures: MapMultiFingerGesture = (
        MapMultiFingerGesture.PINCH_ZOOM | MapMultiFingerGesture.PINCH_MOVE
    )
    """
    When pinchZoomThreshold wins over `rotation_threshold` and `pinch_move_threshold` then pinchZoomWinGestures gestures will be used. 
    By default MultiFingerGesture.pinchZoom and MultiFingerGesture.pinchMove gestures will take effect see MultiFingerGesture for custom settings
    
    Defaults to `MapMultiFingerGesture.PINCH_ZOOM | MapMultiFingerGesture.PINCH_MOVE`.
    """


class MapEventSource(Enum):
    MAP_CONTROLLER = "mapController"
    TAP = "tap"
    SECONDARY_TAP = "secondaryTap"
    LONG_PRESS = "longPress"
    DOUBLE_TAP = "doubleTap"
    DOUBLE_TAP_HOLD = "doubleTapHold"
    DRAG_START = "dragStart"
    ON_DRAG = "onDrag"
    DRAG_END = "dragEnd"
    MULTI_FINGER_GESTURE_START = "multiFingerGestureStart"
    ON_MULTI_FINGER = "onMultiFinger"
    MULTI_FINGER_GESTURE_END = "multiFingerEnd"
    FLING_ANIMATION_CONTROLLER = "flingAnimationController"
    DOUBLE_TAP_ZOOM_ANIMATION_CONTROLLER = "doubleTapZoomAnimationController"
    INTERACTIVE_FLAGS_CHANGED = "interactiveFlagsChanged"
    FIT_CAMERA = "fitCamera"
    CUSTOM = "custom"
    SCROLL_WHEEL = "scrollWheel"
    NON_ROTATED_SIZE_CHANGE = "nonRotatedSizeChange"
    CURSOR_KEYBOARD_ROTATION = "cursorKeyboardRotation"


@dataclass
class MapCameraFit:
    """
    Defines how the camera should fit the bounds or coordinates, depending on which one was provided.

    One of `bounds` or `coordinates` must be specified, but not both.
    """

    bounds: Optional[MapLatitudeLongitudeBounds] = None
    """
    The bounds which the camera should contain once it is fitted.
    """

    coordinates: Optional[List[MapLatitudeLongitude]] = None
    """
    The coordinates which the camera should contain once it is fitted.
    """

    max_zoom: ft.OptionalNumber = None
    """
    The inclusive upper zoom limit used for the resulting fit.
    If the zoom level calculated for the fit exceeds the `max_zoom` value, `max_zoom` will be used instead.
    """

    min_zoom: ft.Number = 0.0
    """
    
    Defaults to `0.0`.
    """

    padding: ft.PaddingValue = field(default_factory=lambda: ft.Padding.zero())
    """
    Adds a constant/pixel-based padding to the normal fit.
    
    Defaults to `Padding.zero()`.
    """

    force_integer_zoom_level: bool = False
    """
    Whether the zoom level of the resulting fit should be rounded to the nearest integer level.
    
    Defaults to `False`.
    """

    def __post_init__(self):
        assert (self.bounds and not self.coordinates) or (
            self.coordinates and not self.bounds
        ), "only one of bounds or coordinates must be provided, not both"


@dataclass
class MapTapEvent(ft.TapEvent):
    coordinates: MapLatitudeLongitude
    """Coordinates of the point at which the tap occured."""


@dataclass
class MapHoverEvent(ft.HoverEvent):
    coordinates: MapLatitudeLongitude


@dataclass
class MapPositionChangeEvent(ft.ControlEvent):
    coordinates: MapLatitudeLongitude
    camera: MapCamera
    has_gesture: bool


@dataclass
class MapPointerEvent(ft.PointerEvent):
    coordinates: MapLatitudeLongitude
    """Coordinates of the point at which the tap occured."""


@dataclass
class MapEvent(ft.ControlEvent):
    source: MapEventSource
    """Who/what issued the event."""

    camera: MapCamera
    """The map camera after the event."""


@dataclass(kw_only=True)
class TileDisplay:
    """
    Defines how the tile should get displayed on the map.

    This is an abstract class and shouldn't be used directly.
    See usable derivatives: `InstantaneousTileDisplay`, and `FadeInTileDisplay`.
    """

    _type: str = ""


@dataclass
class InstantaneousTileDisplay(TileDisplay):
    """A `TileDisplay` that should get instantaneously displayed."""

    opacity: ft.Number = 1.0
    """
    The optional opacity of the tile.
    
    Defaults to `1.0`.
    """

    def __post_init__(self):
        assert (
            0.0 <= self.opacity <= 1.0
        ), "start_opacity must be between 0.0 and 1.0 (inclusive)"
        self._type = "instantaneous"


@dataclass
class FadeInTileDisplay(TileDisplay):
    """A `TileDisplay` that should get faded in."""

    duration: ft.DurationValue = field(
        default_factory=lambda: ft.Duration(milliseconds=100)
    )
    """
    The duration of the fade in animation.
    
    Defaults to `ft.Duration(milliseconds=100)`.
    """

    start_opacity: ft.Number = 1.0
    """
    Opacity start value when a tile is faded in.
    
    Defaults to `1.0`.
    """

    reload_start_opacity: ft.Number = 1.0
    """
    Opacity start value when a tile is reloaded.

    Defaults to `1.0`.
    """

    def __post_init__(self):
        assert (
            0.0 <= self.start_opacity <= 1.0
        ), "start_opacity must be between 0.0 and 1.0 (inclusive)"
        assert (
            0.0 <= self.reload_start_opacity <= 1.0
        ), "reload_start_opacity must be between 0.0 and 1.0 (inclusive)"
        self._type = "fadein"
