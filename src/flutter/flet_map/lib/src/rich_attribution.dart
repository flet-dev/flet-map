import 'package:flet/flet.dart';
import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';

import 'utils/attribution_alignment.dart';

class RichAttributionControl extends StatefulWidget {
  final Control control;

  const RichAttributionControl({super.key, required this.control});

  @override
  State<RichAttributionControl> createState() => _RichAttributionControlState();
}

class _RichAttributionControlState extends State<RichAttributionControl>
    with FletStoreMixin {
  @override
  Widget build(BuildContext context) {
    debugPrint("RichAttributionControl build: ${widget.control.id}");

    var attributions = widget.control
        .buildWidgets("attributions")
        .whereType<SourceAttribution>()
        .toList();

    return RichAttributionWidget(
        attributions: attributions,
        permanentHeight: widget.control.getDouble("permanent_height", 24)!,
        popupBackgroundColor: widget.control.getColor("popup_bgcolor", context),
        showFlutterMapAttribution:
            widget.control.getBool("show_flutter_map_attribution", true)!,
        alignment: parseAttributionAlignment(
            widget.control.getString("alignment"),
            AttributionAlignment.bottomRight)!,
        popupBorderRadius:
            widget.control.getBorderRadius("popup_border_radius"),
        popupInitialDisplayDuration: widget.control
            .getDuration("popup_initial_display_duration", Duration.zero)!);
  }
}
