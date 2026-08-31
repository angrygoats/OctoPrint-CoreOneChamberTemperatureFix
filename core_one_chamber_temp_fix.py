def fix_chamber_temp_report(comm, line, *args, **kwargs):
    return line.replace("C@:", "C:")

__plugin_name__ = "OctoPrint Core One Chamber Temperature Fix"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Fixes the reported chamber temperature to be compatible with OctoPrint."
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_hooks__ = {
    "octoprint.comm.protocol.gcode.received": fix_chamber_temp_report
}
