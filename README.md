# Core One Chamber Temperature Reporting Fix

This small plugin patches Octoprint so that chamber temperature is reported correctly for logging.

## Details

[PR #4671](https://github.com/prusa3d/Prusa-Firmware-Buddy/pull/4671) Stated in the comments that as of Firmware 6.1.1 chamber temperature is reported correctly. However,
Octoprint expects the form to be `C:` and not `@C:`. Below is the way Buddy Firmware 6.8.1 reports temperature:

`T:23.50/0.00 B:21.13/0.00 X:20.87/36.00 A:32.25/0.00 @:0 B@:0 C@:20.70 HBR@:0`.

This PR aims to be a simple fix to this problem by rewriting the chamber temperature report command to `C` via `octoprint.comm.protocol.gcode.received`.

## Usage 

Clone this repository somewhere on your server and copy or simlink `core_one_chamber_temp_fix.py` into your `~/.octoprint/plugins`.
