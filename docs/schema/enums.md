# Enumeration Values

All enumeration constants used in Control Page XML.

## ControlType

Element type determining behavior and rendering.

| Value | Name | Description |
|-------|------|-------------|
| 1 | Device Control | Interactive device element (on/off, dimmer, thermostat) |
| 2 | Variable/List | Variable display or list selection |
| 100 | Button/Label | Static button or text label |
| 200 | Text Display | Text-only display element |
| 201 | Icon Indicator | Icon-based status indicator |

## CaptionPlacement

Where the caption text appears relative to the image.

| Value | Position |
|-------|----------|
| 0 | Top-left |
| 1 | Bottom-left |
| 4 | Below image (most common for icon labels) |
| 5 | Standalone / above (used for titles and text-only elements) |

## FontType

Font style for caption and state text.

| Value | Font |
|-------|------|
| 20 | System regular |
| 22 | System bold |
| 24 | System italic |
| 201 | Monospace |

## StateTextAlignment

Alignment of state text overlay.

| Value | Alignment |
|-------|-----------|
| 0 | Left |
| 1 | Center |

## Color Format

Colors are specified as space-separated hex pairs: `"RR GG BB"`

| Color | Value | Use |
|-------|-------|-----|
| Dark background | `19 19 19` | Page background |
| White | `FF FF FF` | Title text |
| Light gray | `BF BF BF` | Label/caption text |
| Medium gray | `DB DB DB` | State text |
| Dark gray | `33 33 33` | Dim/subtle text |
| Black | `00 00 00` | Light background text |

## DeviceAction

Action to perform on a device (used in Class 1 actions).

| Value | Action |
|-------|--------|
| 4 | Turn on |
| 5 | Turn off |
| 6 | Toggle |

## ClientActionType

Client-side action when element is tapped.

| Value | Action |
|-------|--------|
| 0 | None (default) |
| 1014 | Popup control dialog (brightness slider, thermostat controls, etc.) |

## TargetElemSubKey

Device state key to display. Which state property to monitor.

### Relay / Dimmer

| Key | Description |
|-----|-------------|
| `onOffState` | On/off boolean state |
| `brightnessLevel` | Dimmer level 0-100 |

### Thermostat

| Key | Description |
|-----|-------------|
| `temperatureInputsAll` | All temperature inputs combined |
| `temperatureInput1` | First temperature sensor |
| `temperatureInput2` | Second temperature sensor |
| `humidityInput1` | Humidity sensor |
| `setpointCool` | Cooling setpoint |
| `setpointHeat` | Heating setpoint |
| `hvacOperationMode` | Current HVAC mode |
| `hvacFanMode` | Fan mode |

### Sensor

| Key | Description |
|-----|-------------|
| `onOffState` | Motion/contact sensor state |
| `sensorValue` | Generic sensor reading |

### Sprinkler

| Key | Description |
|-----|-------------|
| `activeZone` | Currently active zone |

### Speed Control

| Key | Description |
|-----|-------------|
| `speedLevel` | Current speed level |
| `speedIndex` | Speed index (0-3) |

### Energy Meter

| Key | Description |
|-----|-------------|
| `curEnergyLevel` | Current energy usage |
| `accumEnergyTotal` | Total accumulated energy |

### General

| Key | Description |
|-----|-------------|
| `LastLogEntry` | Last log entry for the device |
