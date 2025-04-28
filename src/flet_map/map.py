import asyncio
from dataclasses import field
from typing import List, Optional

import flet as ft

from .map_layer import MapLayer
from .types import (
    MapEvent,
    MapHoverEvent,
    MapInteractionConfiguration,
    MapLatitudeLongitude,
    MapPointerEvent,
    MapPositionChangeEvent,
    MapTapEvent,
)

__all__ = ["Map"]


@ft.control("Map")
class Map(ft.ConstrainedControl):
    """
    Map Control.

    -----

    Online docs: https://flet.dev/docs/controls/map
    """

    layers: List[MapLayer]
    initial_center: MapLatitudeLongitude = field(
        default_factory=lambda: MapLatitudeLongitude(latitude=50.5, longitude=30.51)
    )
    initial_rotation: ft.Number = 0.0
    initial_zoom: ft.Number = 13.0
    interaction_configuration: MapInteractionConfiguration = field(
        default_factory=lambda: MapInteractionConfiguration()
    )
    bgcolor: ft.ColorValue = ft.Colors.GREY_300
    keep_alive: bool = False
    max_zoom: ft.OptionalNumber = None
    min_zoom: ft.OptionalNumber = None
    animation_curve: ft.AnimationCurve = ft.AnimationCurve.FAST_OUT_SLOWIN
    animation_duration: ft.DurationValue = field(
        default_factory=lambda: ft.Duration(milliseconds=500)
    )
    on_init: ft.OptionalControlEventCallable = None
    on_tap: ft.OptionalEventCallable[MapTapEvent] = None
    on_hover: ft.OptionalEventCallable[MapHoverEvent] = None
    on_secondary_tap: ft.OptionalEventCallable[MapTapEvent] = None
    on_long_press: ft.OptionalEventCallable[MapTapEvent] = None
    on_event: ft.OptionalEventCallable[MapEvent] = None
    on_position_change: ft.OptionalEventCallable[MapPositionChangeEvent] = None
    on_pointer_down: ft.OptionalEventCallable[MapPointerEvent] = None
    on_pointer_cancel: ft.OptionalEventCallable[MapPointerEvent] = None
    on_pointer_up: ft.OptionalEventCallable[MapPointerEvent] = None

    async def rotate_from_async(
        self,
        degree: ft.Number,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ):
        await self._invoke_method_async(
            method_name="rotate_from",
            arguments={
                "degree": degree,
                "curve": animation_curve or self.animation_curve,
                "duration": animation_duration or self.animation_duration,
                "cancel_ongoing_animations": cancel_ongoing_animations,
            },
        )

    def rotate_from(
        self,
        degree: ft.Number,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ):
        asyncio.create_task(
            self.rotate_from_async(
                degree, animation_curve, animation_duration, cancel_ongoing_animations
            )
        )

    async def reset_rotation_async(
        self,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ):
        await self._invoke_method_async(
            method_name="reset_rotation",
            arguments={
                "curve": animation_curve or self.animation_curve,
                "duration": animation_duration or self.animation_duration,
                "cancel_ongoing_animations": cancel_ongoing_animations,
            },
        )

    def reset_rotation(
        self,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.DurationValue = None,
        cancel_ongoing_animations: bool = False,
    ):
        asyncio.create_task(
            self.reset_rotation_async(
                animation_curve, animation_duration, cancel_ongoing_animations
            )
        )

    async def zoom_in_async(
        self,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ):
        await self._invoke_method_async(
            method_name="zoom_in",
            arguments={
                "curve": animation_curve or self.animation_curve,
                "duration": animation_duration or self.animation_duration,
                "cancel_ongoing_animations": cancel_ongoing_animations,
            },
        )

    def zoom_in(
        self,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ):
        asyncio.create_task(
            self.zoom_in_async(
                animation_curve, animation_duration, cancel_ongoing_animations
            )
        )

    async def zoom_out_async(
        self,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ):
        await self._invoke_method_async(
            method_name="zoom_out",
            arguments={
                "curve": animation_curve or self.animation_curve,
                "duration": animation_duration or self.animation_duration,
                "cancel_ongoing_animations": cancel_ongoing_animations,
            },
        )

    def zoom_out(
        self,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ):
        asyncio.create_task(
            self.zoom_out_async(
                animation_curve, animation_duration, cancel_ongoing_animations
            )
        )

    async def zoom_to_async(
        self,
        zoom: ft.Number,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ):
        await self._invoke_method_async(
            method_name="zoom_to",
            arguments={
                "zoom": zoom,
                "curve": animation_curve or self.animation_curve,
                "duration": animation_duration or self.animation_duration,
                "cancel_ongoing_animations": cancel_ongoing_animations,
            },
        )

    def zoom_to(
        self,
        zoom: ft.Number,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ):
        asyncio.create_task(
            self.zoom_to_async(
                zoom, animation_curve, animation_duration, cancel_ongoing_animations
            )
        )

    async def move_to_async(
        self,
        destination: Optional[MapLatitudeLongitude] = None,
        zoom: ft.OptionalNumber = None,
        rotation: ft.OptionalNumber = None,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        offset: ft.OffsetValue = ft.Offset(0, 0),
        cancel_ongoing_animations: bool = False,
    ):
        await self._invoke_method_async(
            method_name="move_to",
            arguments={
                "destination": destination,
                "zoom": zoom,
                "offset": offset,
                "rotation": rotation,
                "curve": animation_curve or self.animation_curve,
                "duration": animation_duration or self.animation_duration,
                "cancel_ongoing_animations": cancel_ongoing_animations,
            },
        )

    def move_to(
        self,
        destination: Optional[MapLatitudeLongitude] = None,
        zoom: ft.OptionalNumber = None,
        rotation: ft.OptionalNumber = None,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        offset: ft.OffsetValue = ft.Offset(0, 0),
        cancel_ongoing_animations: bool = False,
    ):
        asyncio.create_task(
            self.move_to_async(
                destination,
                zoom,
                rotation,
                animation_curve,
                animation_duration,
                offset,
                cancel_ongoing_animations,
            )
        )

    async def center_on_async(
        self,
        point: MapLatitudeLongitude,
        zoom: ft.OptionalNumber,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
    ):
        await self._invoke_method_async(
            method_name="center_on",
            arguments={
                "point": point,
                "zoom": zoom,
                "curve": animation_curve or self.animation_curve,
                "duration": animation_duration or self.animation_duration,
            },
        )

    def center_on(
        self,
        point: Optional[MapLatitudeLongitude],
        zoom: ft.OptionalNumber,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
    ):
        asyncio.create_task(
            self.center_on_async(point, zoom, animation_curve, animation_duration)
        )
