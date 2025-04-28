from dataclasses import dataclass, field
from enum import Enum, IntFlag
from typing import List, Optional

import flet as ft


class MapTileLayerEvictErrorTileStrategy(Enum):
    NONE = "none"
    DISPOSE = "dispose"
    NOT_VISIBLE = "notVisible"
    NOT_VISIBLE_RESPECT_MARGIN = "notVisibleRespectMargin"


class AttributionAlignment(Enum):
    BOTTOM_LEFT = "bottomLeft"
    BOTTOM_RIGHT = "bottomRight"


class PatternFit(Enum):
    SCALE_DOWN = "scaleDown"
    SCALE_UP = "scaleUp"
    APPEND_DOT = "appendDot"
    EXTEND_FINAL_DASH = "extendFinalDash"


@dataclass
class MapCamera:
    center: "MapLatitudeLongitude"
    zoom: float
    min_zoom: float
    max_zoom: float
    rotation: float


@dataclass
class StrokePattern:
    type: str = ""


@dataclass
class SolidStrokePattern(StrokePattern):
    def __post_init__(self):
        self.type = "solid"


@dataclass
class DashedStrokePattern(StrokePattern):
    segments: List[ft.Number] = field(default_factory=list)
    pattern_fit: PatternFit = PatternFit.SCALE_UP

    def __post_init__(self):
        self.type = "dashed"


@dataclass
class DottedStrokePattern(StrokePattern):
    spacing_factor: ft.Number = 1.5
    pattern_fit: PatternFit = PatternFit.SCALE_UP

    def __post_init__(self):
        self.type = "dotted"


@dataclass
class MapLatitudeLongitude:
    latitude: ft.Number
    longitude: ft.Number


@dataclass
class MapLatitudeLongitudeBounds:
    corner_1: MapLatitudeLongitude
    corner_2: MapLatitudeLongitude


class MapInteractiveFlag(IntFlag):
    NONE = 0
    DRAG = 1 << 0
    FLING_ANIMATION = 1 << 1
    PINCH_MOVE = 1 << 2
    PINCH_ZOOM = 1 << 3
    DOUBLE_TAP_ZOOM = 1 << 4
    DOUBLE_TAP_DRAG_ZOOM = 1 << 5
    SCROLL_WHEEL_ZOOM = 1 << 6
    ROTATE = 1 << 7
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


class MapMultiFingerGesture(IntFlag):
    NONE = 0
    PINCH_MOVE = 1 << 0
    PINCH_ZOOM = 1 << 1
    ROTATE = 1 << 2
    ALL = (1 << 0) | (1 << 1) | (1 << 2)


@dataclass
class MapInteractionConfiguration:
    enable_multi_finger_gesture_race: Optional[bool] = None
    pinch_move_threshold: ft.OptionalNumber = None
    scroll_wheel_velocity: ft.OptionalNumber = None
    pinch_zoom_threshold: ft.OptionalNumber = None
    rotation_threshold: ft.OptionalNumber = None
    flags: Optional[MapInteractiveFlag] = None
    rotation_win_gestures: Optional[MapMultiFingerGesture] = None
    pinch_move_win_gestures: Optional[MapMultiFingerGesture] = None
    pinch_zoom_win_gestures: Optional[MapMultiFingerGesture] = None


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
class MapTapEvent(ft.TapEvent):
    coordinates: MapLatitudeLongitude


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


@dataclass
class MapEvent(ft.ControlEvent):
    source: MapEventSource
    camera: MapCamera
