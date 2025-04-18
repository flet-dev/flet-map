import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';

class TextSourceAttributionControl extends StatelessWidget {
  final Control control;

  const TextSourceAttributionControl({super.key, required this.control});

  @override
  Widget build(BuildContext context) {
    debugPrint("TextSourceAttributionControl build: ${control.id}");

    return TextSourceAttribution(
      control.getString("text", "Placeholder Text")!,
      textStyle: control.getTextStyle("text_style", Theme.of(context)),
      onTap: () => control.triggerEvent("click"),
      prependCopyright: control.getBool("prepend_copyright", true)!,
    );
  }
}
