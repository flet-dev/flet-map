import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';

class ImageSourceAttributionControl extends StatelessWidget {
  final Control control;

  const ImageSourceAttributionControl({super.key, required this.control});

  @override
  Widget build(BuildContext context) {
    debugPrint("ImageSourceAttributionControl build: ${control.id}");
    var content = control.buildWidget("content");
    if (content is! Image) {
      return const ErrorControl("content must be an Image control");
    }
    return LogoSourceAttribution(
      content,
      height: control.getDouble("height", 24)!,
      tooltip: control.getString("tooltip"),
      onTap: () => control.triggerEvent("click"),
    );
  }
}
