import asyncio
from dataclasses import field
from typing import List, Optional

import flet as ft

from .map_layer import MapLayer
from .types import (
    CameraFit,
    InteractionConfiguration,
    MapEvent,
    MapHoverEvent,
    MapLatitudeLongitude,
    MapPointerEvent,
    MapPositionChangeEvent,
    MapTapEvent,
)

__all__ = ["Map"]


@ft.control("Map")
class Map(ft.ConstrainedControl):
    """
    An interactive map control that allows displaying various layers.
    """

    layers: List[MapLayer]
    """
    A list of layers to be displayed (stack-like) on the map.

    Value is of type `MapLayer`.
    """

    initial_center: MapLatitudeLongitude = field(
        default_factory=lambda: MapLatitudeLongitude(latitude=50.5, longitude=30.51)
    )
    """
    The initial center of the map.

    Value is of type `MapLatitudeLongitude`.
    Defaults to `MapLatitudeLongitude(latitude=50.5, longitude=30.51)`.
    """

    initial_rotation: ft.Number = 0.0
    """
    The rotation (in degrees) when the map is first loaded.
    
    Defaults to `0.0`.
    """

    initial_zoom: ft.Number = 13.0
    """
    The zoom when the map is first loaded. 
    If initial_camera_fit is defined this has no effect.
    
    Defaults to `13.0`.
    """

    interaction_configuration: InteractionConfiguration = field(
        default_factory=lambda: InteractionConfiguration()
    )
    """
    The interaction configuration.
    
    Defaults to `InteractionConfiguration()`.
    """

    bgcolor: ft.ColorValue = ft.Colors.GREY_300
    """
    The background color of this control.
    
    Defaults to `ft.Colors.GREY_300`.
    """

    keep_alive: bool = False
    """
    Whether to enable the built in keep-alive functionality.
    
    If the map is within a complex layout, such as a `ListView`,
    the map will reset to it's inital position after it appears back into view.
    To ensure this doesn't happen, enable this flag to prevent it from rebuilding.
    
    Defaults to `False`.
    """

    max_zoom: ft.OptionalNumber = None
    """
    The maximum (highest) zoom level of every layer. 
    Each layer can specify additional zoom level restrictions.
    """

    min_zoom: ft.OptionalNumber = None
    """
    The minimum (smallest) zoom level of every layer. 
    Each layer can specify additional zoom level restrictions.
    """

    animation_curve: ft.AnimationCurve = ft.AnimationCurve.FAST_OUT_SLOWIN
    """
    The default animation curve to be used for map-animations 
    when calling instance methods like `zoom_in()`, `rotate_from()`, `move_to()` etc.
    
    Defaults to `AnimationCurve.FAST_OUT_SLOWIN`.
    """

    animation_duration: ft.DurationValue = field(
        default_factory=lambda: ft.Duration(milliseconds=500)
    )
    """
    The default animation duration to be used for map-animations 
    when calling instance methods like `zoom_in()`, `rotate_from()`, `move_to()` etc.
    
    Defaults to `Duration(milliseconds=500)`.
    """

    initial_camera_fit: Optional[CameraFit] = None
    """
    Defines the visible bounds when the map is first loaded. 
    Takes precedence over `initial_center`/`initial_zoom`.
    """

    on_init: ft.OptionalControlEventCallable = None
    """
    Fires when the map is initialized.
    """

    on_tap: ft.OptionalEventCallable[MapTapEvent] = None
    """
    Fires when a tap event occurs.

    Event handler argument is of type [`MapTapEvent`][(p).types.].
    """

    on_hover: ft.OptionalEventCallable[MapHoverEvent] = None
    """
    Fires when a hover event occurs.

    Event handler argument is of type [`MapHoverEvent`][(p).types.].
    """

    on_secondary_tap: ft.OptionalEventCallable[MapTapEvent] = None
    """
    Fires when a secondary tap event occurs.

    Event handler argument is of type [`MapTapEvent`][(p).types.].
    """

    on_long_press: ft.OptionalEventCallable[MapTapEvent] = None
    """
    Fires when a long press event occurs.

    Event handler argument is of type [`MapTapEvent`][(p).types.].
    """

    on_event: ft.OptionalEventCallable[MapEvent] = None
    """
    Fires when any map events occurs.

    Event handler argument is of type [`MapEvent`][(p).types.].
    """

    on_position_change: ft.OptionalEventCallable[MapPositionChangeEvent] = None
    """
    Fires when the map position changes.

    Event handler argument is of type [`MapPositionChangeEvent`][(p).types.].
    """

    on_pointer_down: ft.OptionalEventCallable[MapPointerEvent] = None
    """
    Fires when a pointer down event occurs.

    Event handler argument is of type [`MapPointerEvent`][(p).types.].
    """

    on_pointer_cancel: ft.OptionalEventCallable[MapPointerEvent] = None
    """
    Fires when a pointer cancel event occurs.
    
    Event handler argument is of type [`MapPointerEvent`][(p).types.].
    """

    on_pointer_up: ft.OptionalEventCallable[MapPointerEvent] = None
    """
    Fires when a pointer up event occurs.

    Event handler argument is of type [`MapPointerEvent`][(p).types.].
    """

    async def rotate_from_async(
        self,
        degree: ft.Number,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ) -> None:
        """
        Applies a rotation of `degree` to the current rotation.

        Args:
            degree: The number of degrees to increment to the current rotation.
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
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
    ) -> None:
        """
        Applies a rotation of `degree` to the current rotation.

        Args:
            degree: The number of degrees to increment to the current rotation.
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
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
    ) -> None:
        """
        Resets the map's rotation to 0 degrees.

        Args:
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
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
    ) -> None:
        """
        Resets the map's rotation to 0 degrees.

        Args:
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
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
    ) -> None:
        """
        Zooms in by one zoom-level from the current one.

        Args:
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
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
    ) -> None:
        """
        Zooms in by one zoom-level from the current one.

        Args:
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
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
    ) -> None:
        """
        Zooms out by one zoom-level from the current one.

        Args:
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
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
    ) -> None:
        """
        Zooms out by one zoom-level from the current one.

        Args:
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
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
    ) -> None:
        """
        Zoom the map to a specific zoom level.

        Args:
            zoom: The zoom level to zoom to.
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
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
    ) -> None:
        """
        Zoom the map to a specific zoom level.

        Args:
            zoom: The zoom level to zoom to.
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
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
    ) -> None:
        """
        Moves to a specific location.

        Args:
            destination: The destination point to move to.
            zoom: The zoom level to be applied. If provided, must be greater than or equal to `0.0`.
            rotation: Rotation (in degrees) to be applied.
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            offset: The offset to be used. Only works when `rotation` is `None`.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.

        Raises:
            AssertionError: If `zoom` is not `None` and is negative.
        """
        assert zoom is None or zoom >= 0, "zoom must be greater than or equal to zero"
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
    ) -> None:
        """
        Moves to a specific location.

        Args:
            destination: The destination point to move to.
            zoom: The zoom level to be applied. If provided, must be greater than or equal to `0.0`.
            rotation: Rotation (in degrees) to be applied.
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            offset: The offset to be used. Only works when `rotation` is `None`.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.

        Raises:
            AssertionError: If `zoom` is not `None` and is negative.
        """
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
        cancel_ongoing_animations: bool = False,
    ) -> None:
        """
        Centers the map on the given point.

        Args:
            point: The point on which to center the map.
            zoom: The zoom level to be applied.
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
        await self._invoke_method_async(
            method_name="center_on",
            arguments={
                "point": point,
                "zoom": zoom,
                "curve": animation_curve or self.animation_curve,
                "duration": animation_duration or self.animation_duration,
                "cancel_ongoing_animations": cancel_ongoing_animations,
            },
        )

    def center_on(
        self,
        point: Optional[MapLatitudeLongitude],
        zoom: ft.OptionalNumber,
        animation_curve: ft.OptionalAnimationCurve = None,
        animation_duration: ft.OptionalDurationValue = None,
        cancel_ongoing_animations: bool = False,
    ) -> None:
        """
        Centers the map on the given point.

        Args:
            point: The point on which to center the map.
            zoom: The zoom level to be applied.
            animation_curve: The curve of the animation. If None (the default), `Map.animation_curve` will be used.
            animation_duration: The duration of the animation. If None (the default), `Map.animation_duration` will be used.
            cancel_ongoing_animations: Whether to cancel/stop all ongoing map-animations before starting this new one.
        """
        asyncio.create_task(
            self.center_on_async(
                point,
                zoom,
                animation_curve,
                animation_duration,
                cancel_ongoing_animations,
            )
        )
