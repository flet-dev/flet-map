import 'dart:convert';

import 'package:collection/collection.dart';
import 'package:flet/flet.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart';

LatLng? parseLatLng(dynamic value, [LatLng? defaultValue]) {
  if (value == null) return defaultValue;

  return LatLng(
      parseDouble(value['latitude'], 0)!, parseDouble(value['longitude'], 0)!);
}

LatLngBounds? parseLatLngBounds(dynamic value, [LatLngBounds? defaultValue]) {
  if (value == null ||
      value['corner_1'] == null ||
      value['corner_2'] == null ||
      parseLatLng(value['corner_1']) == null ||
      parseLatLng(value['corner_2']) == null) {
    return defaultValue;
  }
  return LatLngBounds(
      parseLatLng(value['corner_1'])!, parseLatLng(value['corner_2'])!);
}

PatternFit? parsePatternFit(String? value, [PatternFit? defaultValue]) {
  if (value == null) return defaultValue;
  return PatternFit.values.firstWhereOrNull(
          (e) => e.name.toLowerCase() == value.toLowerCase()) ??
      defaultValue;
}

StrokePattern? parseStrokePattern(dynamic value,
    [StrokePattern? defaultValue]) {
  if (value == null) return defaultValue;

  if (value['type'] == 'dotted') {
    return StrokePattern.dotted(
      spacingFactor: parseDouble(value['spacing_factor'], 1.5)!,
      patternFit: parsePatternFit(value['pattern_fit'], PatternFit.scaleUp)!,
    );
  } else if (value['type'] == 'solid') {
    return const StrokePattern.solid();
  } else if (value['type'] == 'dashed') {
    var segments = value['segments'] ?? [];
    return StrokePattern.dashed(
      patternFit: parsePatternFit(value['pattern_fit'], PatternFit.scaleUp)!,
      segments: segments.map((e) => parseDouble(e)).nonNulls.toList(),
    );
  }
  return defaultValue;
}

InteractionOptions? parseInteractionOptions(dynamic value,
    [InteractionOptions? defaultValue]) {
  if (value == null) return defaultValue;
  return InteractionOptions(
      enableMultiFingerGestureRace:
          parseBool(value["enable_multi_finger_gesture_race"], false)!,
      pinchMoveThreshold: parseDouble(value["pinch_move_threshold"], 40.0)!,
      scrollWheelVelocity: parseDouble(value["scroll_wheel_velocity"], 0.005)!,
      pinchZoomThreshold: parseDouble(value["pinch_zoom_threshold"], 0.5)!,
      rotationThreshold: parseDouble(value["rotation_threshold"], 20.0)!,
      flags: parseInt(value["flags"], InteractiveFlag.all)!,
      rotationWinGestures:
          parseInt(value["rotation_win_gestures"], MultiFingerGesture.rotate)!,
      pinchMoveWinGestures: parseInt(value["pinch_move_win_gestures"],
          MultiFingerGesture.pinchZoom | MultiFingerGesture.pinchMove)!,
      pinchZoomWinGestures: parseInt(value["pinch_zoom_win_gestures"],
          MultiFingerGesture.pinchZoom | MultiFingerGesture.pinchMove)!);
}

EvictErrorTileStrategy? parseEvictErrorTileStrategy(String? value,
    [EvictErrorTileStrategy? defaultValue]) {
  if (value == null) return defaultValue;
  return EvictErrorTileStrategy.values.firstWhereOrNull(
          (e) => e.name.toLowerCase() == value.toLowerCase()) ??
      defaultValue;
}

MapOptions? parseConfiguration(Control control, BuildContext context,
    [MapOptions? defaultValue]) {
  return MapOptions(
    initialCenter:
        parseLatLng(control.get("initial_center", const LatLng(50.5, 30.51)))!,
    interactionOptions: parseInteractionOptions(
        control.get("interaction_configuration", const InteractionOptions()))!,
    backgroundColor:
        control.getColor("bgcolor", context, const Color(0x00000000))!,
    initialRotation: control.getDouble("initial_rotation", 0.0)!,
    initialZoom: control.getDouble("initial_zoom", 13.0)!,
    keepAlive: control.getBool("keep_alive", false)!,
    maxZoom: control.getDouble("max_zoom"),
    minZoom: control.getDouble("min_zoom"),
    onPointerHover: control.getBool("on_hover", false)!
        ? (PointerHoverEvent e, LatLng latlng) {
            control.triggerEvent("hover", {
              "coordinates": {
                "latitude": latlng.latitude,
                "longitude": latlng.longitude,
              },
              "global_x": e.position.dx,
              "global_y": e.position.dy,
              "local_x": e.localPosition.dx,
              "local_y": e.localPosition.dy,
              "device_type": e.kind.name,
            });
          }
        : null,
    onTap: control.getBool("on_tap", false)!
        ? (TapPosition pos, LatLng latlng) {
            control.triggerEvent("tap", {
              "coordinates": {
                "latitude": latlng.latitude,
                "longitude": latlng.longitude,
              },
              "global_x": pos.global.dx,
              "global_y": pos.global.dy,
              "local_x": pos.relative?.dx,
              "local_y": pos.relative?.dy,
            });
          }
        : null,
    onLongPress: control.getBool("on_long_press", false)!
        ? (TapPosition pos, LatLng latlng) {
            control.triggerEvent("long_press", {
              "coordinates": {
                "latitude": latlng.latitude,
                "longitude": latlng.longitude,
              },
              "global_x": pos.global.dx,
              "global_y": pos.global.dy,
              "local_x": pos.relative?.dx,
              "local_y": pos.relative?.dy,
            });
          }
        : null,
    onPositionChanged: control.getBool("on_position_change", false)!
        ? (MapCamera camera, bool hasGesture) {
            control.triggerEvent("position_change", {
              "coordinates": {
                "latitude": camera.center.latitude,
                "longitude": camera.center.longitude,
              },
              "min_zoom": camera.minZoom,
              "max_zoom": camera.maxZoom,
              "rotation": camera.rotation,
            });
          }
        : null,
    onPointerDown: control.getBool("on_pointerDown", false)!
        ? (PointerDownEvent e, LatLng latlng) {
            control.triggerEvent("pointer_down", {
              "coordinates": {
                "latitude": latlng.latitude,
                "longitude": latlng.longitude,
              },
              "global_x": e.position.dx,
              "global_y": e.position.dy,
              "device_type": e.kind.name,
            });
          }
        : null,
    onPointerCancel: control.getBool("on_pointer_cancel", false)!
        ? (PointerCancelEvent e, LatLng latlng) {
            control.triggerEvent("pointer_cancel", {
              "coordinates": {
                "latitude": latlng.latitude,
                "longitude": latlng.longitude,
              },
              "global_x": e.position.dx,
              "global_y": e.position.dy,
              "device_type": e.kind.name,
            });
          }
        : null,
    onPointerUp: control.getBool("on_pointer_up", false)!
        ? (PointerUpEvent e, LatLng latlng) {
            control.triggerEvent("pointer_up", {
              "coordinates": {
                "latitude": latlng.latitude,
                "longitude": latlng.longitude,
              },
              "global_x": e.position.dx,
              "global_y": e.position.dy,
              "device_type": e.kind.name,
            });
          }
        : null,
    onSecondaryTap: control.getBool("onSecondary_tap", false)!
        ? (TapPosition pos, LatLng latlng) {
            control.triggerEvent("secondary_tap", {
              "coordinates": {
                "latitude": latlng.latitude,
                "longitude": latlng.longitude,
              },
              "global_x": pos.global.dx,
              "global_y": pos.global.dy,
              "local_x": pos.relative?.dx,
              "local_y": pos.relative?.dy,
            });
          }
        : null,
    onMapEvent: control.getBool("on_event", false)!
        ? (MapEvent e) {
            control.triggerEvent("event", {
              "source": e.source.name,
              "center": {
                "latitude": e.camera.center.latitude,
                "longitude": e.camera.center.longitude,
              },
              "zoom": e.camera.zoom,
              "min_zoom": e.camera.minZoom,
              "max_zoom": e.camera.maxZoom,
              "rotation": e.camera.rotation,
            });
          }
        : null,
    onMapReady: control.getBool("on_init", false)!
        ? () => control.triggerEvent("init")
        : null,
  );
}
