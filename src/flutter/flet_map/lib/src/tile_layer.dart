import 'dart:convert';

import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:flutter_map_cancellable_tile_provider/flutter_map_cancellable_tile_provider.dart';

import './utils/map.dart';

class TileLayerControl extends StatelessWidget {
  final Control control;

  const TileLayerControl({super.key, required this.control});

  @override
  Widget build(BuildContext context) {
    debugPrint("TileLayerControl build: ${control.id}");

    var errorImageSrc = control.getString("errorImageSrc");
    ImageProvider<Object>? errorImage;

    if (errorImageSrc != null) {
      var assetSrc = control.backend.getAssetSource(errorImageSrc);
      if (assetSrc.isFile) {
        // from File
        errorImage = AssetImage(assetSrc.path);
      } else {
        // URL
        errorImage = NetworkImage(assetSrc.path);
      }
    }
    Widget tileLayer = TileLayer(
        urlTemplate: control.getString("url_template", "")!,
        fallbackUrl: control.getString("fallback_url"),
        subdomains: control.get("subdomains", ['a', 'b', 'c'])!,
        tileProvider: CancellableNetworkTileProvider(),
        tileDisplay: const TileDisplay.fadeIn(),
        tileSize: control.getDouble("tile_size", 256)!,
        minNativeZoom: control.getInt("min_native_zoom", 0)!,
        maxNativeZoom: control.getInt("max_native_zoom", 19)!,
        zoomReverse: control.getBool("zoom_reverse", false)!,
        zoomOffset: control.getDouble("zoom_offset", 0)!,
        keepBuffer: control.getInt("keep_buffer", 2)!,
        panBuffer: control.getInt("pan_buffer", 1)!,
        tms: control.getBool("enable_tms", false)!,
        tileBounds: parseLatLngBounds(control.get("tile_bounds")),
        retinaMode: control.getBool("enable_retina_mode"),
        maxZoom: control.getDouble("max_zoom", double.infinity)!,
        minZoom: control.getDouble("min_zoom", 0)!,
        evictErrorTileStrategy: parseEvictErrorTileStrategy(
            control.getString("evict_error_tile_strategy"),
            EvictErrorTileStrategy.none)!,
        errorImage: errorImage,
        errorTileCallback: (TileImage t, Object o, StackTrace? s) {
          control.triggerEvent("image_error");
        },
        additionalOptions: control.get("additional_options", {})!);

    return ConstrainedControl(control: control, child: tileLayer);
  }
}
