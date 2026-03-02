# Control Page Builder Workflow

5-phase guided process for creating Indigo Control Pages.

---

## Phase 1: DISCOVER

Find devices available for the control page.

### Method A: MCP Server (Preferred)

If Indigo MCP server is available, query devices directly:

```
# Get all device types
search_entities(query="all devices")

# Or by specific type
get_devices_by_type(device_type="dimmer")    # Lights
get_devices_by_type(device_type="relay")     # Switches
get_devices_by_type(device_type="thermostat")
get_devices_by_type(device_type="sensor")    # Motion, temp, etc.
get_devices_by_type(device_type="speedcontrol")  # Fans
get_devices_by_type(device_type="sprinkler")
```

### Method B: Database Fallback

If no MCP server, read the Indigo database directly:

```bash
# Find the database file
ls "/Library/Application Support/Perceptive Automation/Indigo 2025.1/Databases/"

# The database is an XML file - extract device info
grep -A5 '<Name type="string">' "/Library/Application Support/Perceptive Automation/Indigo 2025.1/Databases/IndigoDb.indiDb"
```

Look for `<DeviceList` section and extract:
- Device `<Name>` — display name
- Device `<ID>` — numeric ID (needed for XML)
- Device type — from `<TypeId>` or `<DeviceTypeId>`

### Output

Present a device inventory table:

```
| # | Name               | ID         | Type       | Key States        |
|---|--------------------|------------|------------|-------------------|
| 1 | Living Room Light  | 123456789  | dimmer     | onOffState, brightness |
| 2 | Front Door Lock    | 234567890  | relay      | onOffState        |
| 3 | Hallway Thermostat | 345678901  | thermostat | temperatureInput1, setpointHeat |
| 4 | Kitchen Motion     | 456789012  | sensor     | onOffState        |
```

Ask: "I found these devices. Which room or area are we building a control page for?"

---

## Phase 2: PLAN

Ask the user about their control page using **AskUserQuestion** tool.

### Loading User Preferences

Before asking questions, check if `control-pages.local.md` exists in the skill directory. If it doesn't exist, create it with the default content below, then read it:

```yaml
---
# Screen presets (built-in + custom)
screen_presets:
  iPhone: "375 667"
  iPhone Plus: "414 736"
  iPad Portrait: "768 1024"
  iPad Landscape: "1024 768"
  Full HD: "1920 1080"
  # Add custom presets here:
  # Wall Tablet: "1920 1080"

default_screen: "iPhone"

# Style: minimal | dashboard | full-control
default_style: "full-control"

# Theme
theme:
  background: "19 19 19"
  title_color: "FF FF FF"
  label_color: "FF FF FF"
  state_text_color: "DB DB DB"

# Layout
layout:
  icon_size: "76 76"
  caption_placement: omit   # omit = below icon (default), 4 = left of icon
  retina: true               # always use 2x images

# Typography
fonts:
  title_size: 22
  title_font: 22             # bold
  label_size: 14
  state_text_size: 20
---

## Style Notes

Any free-form notes about your preferences go here.
For example: "Always use dark theme for room controls, light for camera pages."
```

Once the config is loaded, apply saved defaults:

1. For each question below, check if the config has a default value
2. If a default exists, use it and tell the user: "Using your default: **X**"
3. If no default exists, ask the question as normal
4. After applying defaults, offer: "Using your saved preferences. Say **'change'** to adjust any setting."

This makes repeat usage much faster — the user only answers questions that don't have saved defaults.

### Question 1: Room/Purpose

```
"What room or purpose is this control page for?"
Options: Based on device names (e.g., "Living Room", "Kitchen", "Bedroom", "Outdoor", "Security")
```

### Question 2: Devices

Present discovered devices filtered by room, ask which to include:

```
"Which devices should appear on this control page?"
multiSelect: true
Options: List devices relevant to the chosen room
```

### Question 3: Screen Size

```
"What screen size should this control page be designed for?"
Options:
- "iPhone (375x667)" — Standard phone (Recommended)
- "iPhone Plus (414x736)" — Large phone
- "iPad Portrait (768x1024)" — Tablet portrait
- "iPad Landscape (1024x768)" — Tablet landscape
- Custom — Ask for width x height
```

### Question 4: Style

```
"What style of control page?"
Options:
- "Minimal" — Icons with labels only
- "Dashboard" — Icons with state text and labels (Recommended)
- "Full Control" — Icons with state text, labels, and popup controls
```

### Quick Mode

If user provides enough context upfront (e.g., "Create a control page for the living room with the ceiling light, floor lamp, and thermostat on iPhone"), skip questions and use:
- Room: from user input
- Devices: from user input (match names to discovered devices)
- Screen: from config `default_screen` if set, otherwise iPhone 375x667
- Style: from config `default_style` if set, otherwise Dashboard

With a config file, Quick Mode becomes even faster — the user can just say "build bedroom page" and everything else comes from saved preferences.

### Defaults for Beginners

If user says "I'm not sure" or similar:
- Screen: iPhone (most common)
- Style: Dashboard (good balance of info and simplicity)
- Devices: All devices in the selected room
- Layout: 2-column grid

---

## Phase 3: WIREFRAME

Generate an ASCII wireframe based on the plan.

### Layout Rules

1. **Title**: Centered at top, 20px from top edge
2. **Grid**: 2 columns for iPhone, 3 for iPad portrait, 4 for iPad landscape
3. **Spacing**: 90px vertical between element rows, 20px horizontal gap
4. **Padding**: 30px from left/right edges
5. **Icons**: 76x76 (2x images)
6. **Labels**: Below icon at +80px Y offset (CaptionPlacement 4)
7. **Grouping**: Related devices together (lights, climate, sensors)

### Wireframe Symbols

Use these symbols in the ASCII wireframe:

| Symbol | Device Type |
|--------|-------------|
| `[light-bulb]` | Dimmer / Light |
| `[thermometer]` | Thermostat |
| `[switch]` | Relay / Switch |
| `[fan]` | Speed control / Fan |
| `[motion]` | Motion sensor |
| `[temp]` | Temperature sensor |
| `[humidity]` | Humidity sensor |
| `[sprinkler]` | Sprinkler |
| `[label]` | Text label |
| `[button]` | Action button |
| `[dot]` | Status indicator |
| `[power-meter]` | Energy meter |
| `[garage]` | Garage door |

### Example Wireframe (iPhone, 2-column, Dashboard)

```
+------ Living Room (375x667) ------+
|                                    |
|          "Living Room"             |
|                                    |
|   [light-bulb]    [light-bulb]    |
|   Ceiling Light    Floor Lamp      |
|   "On - 80%"      "Off"           |
|                                    |
|   [fan]           [thermometer]   |
|   Ceiling Fan      Thermostat     |
|   "Speed 2"       "72°F"          |
|                                    |
|   [motion]                        |
|   Hall Motion                      |
|   "No motion"                      |
|                                    |
+------------------------------------+
```

### Iteration

Present wireframe to user and ask: "Does this layout work? Any changes?"

Support modifications:
- "Move X up" / "Move X down"
- "Swap X and Y"
- "Add Z"
- "Remove W"
- "Make it 3 columns"
- "Group the lights together"

When layout is ambiguous, offer: "Option A or Option B?"

---

## Phase 4: BUILD

Convert the wireframe to valid Indigo XML.

### Steps

1. **Generate unique page ID**:
   ```bash
   python3 -c "import random; print(random.randint(100000000, 2147483647))"
   ```

2. **Generate unique element IDs** for each PageElem (same method)

3. **Map wireframe to XML**:
   - Each wireframe element becomes a `<PageElem>` with calculated Position
   - Use real device IDs from Phase 1
   - Set correct ControlType, ImageFileName, ActionGroup per device type
   - Calculate positions from the wireframe grid layout

4. **Validate XML**:
   - All device IDs are real (from Phase 1)
   - All image filenames exist (from image catalog)
   - Positions are within page bounds
   - No duplicate element IDs

### Device Type to XML Mapping

**Light / Dimmer:**
- ControlType: 1
- ImageFileName: `Dimmable Light 2x` (or other light image)
- ShowStateImage: true, ShowStateText: true
- TargetElemSubKey: `brightnessLevel`
- ActionGroup: toggle (DeviceAction 6)
- ClientActionType: 1014 (popup for brightness control)

**Relay / Switch:**
- ControlType: 1
- ImageFileName: `Switch 2x` (or button image)
- ShowStateImage: true
- TargetElemSubKey: `onOffState`
- ActionGroup: toggle (DeviceAction 6)

**Thermostat:**
- ControlType: 1
- ImageFileName: `Temperature Sensor 2x`
- ShowStateImage: true, ShowStateText: true
- TargetElemSubKey: `temperatureInputsAll`
- ActionGroup: empty (display-only) or ClientActionType 1014 for popup
- For mode control: separate element with `Thermostat Mode` image

**Motion Sensor:**
- ControlType: 1
- ImageFileName: `Motion Sensor 2x`
- ShowStateImage: true, ShowStateText: true
- TargetElemSubKey: `onOffState`
- ActionGroup: empty (display-only, no user action)

**Fan / Speed Control:**
- ControlType: 1
- ImageFileName: `Fan 2x` or `ceilingfan_large`
- ShowStateImage: true
- TargetElemSubKey: `speedLevel`
- ActionGroup: toggle or ClientActionType 1014

**Sprinkler:**
- ControlType: 1
- ImageFileName: `Sprinkler 2x`
- ShowStateImage: true, ShowStateText: true
- TargetElemSubKey: `activeZone`
- ActionGroup: sprinkler action (Class 2)

**Text Label (title, section header):**
- ControlType: 100
- No image, just CaptionName
- CaptionFontType: 22 (bold), CaptionPointSize: 22
- ActionGroup: empty

### Reference Docs

Load these files during BUILD phase:
- `docs/schema/control-page.md` — Page wrapper XML
- `docs/schema/page-elements.md` — Element properties
- `docs/schema/actions.md` — Action classes
- `docs/schema/enums.md` — Enumeration values
- `docs/images/device-images.md` — Image filenames

---

## Phase 5: EXPORT

Create a `.textClipping` file for drag-and-drop import into Indigo.

### Steps

1. **Save XML** to a temporary file:
   ```bash
   cat > /tmp/control_page.xml << 'XMLEOF'
   <ControlPageList type="vector">
     <!-- generated XML here -->
   </ControlPageList>
   XMLEOF
   ```

2. **Run the clipping script**:
   ```bash
   cat /tmp/control_page.xml | python3 /path/to/indigo-control-pages/tools/create_clipping.py ~/Desktop/PageName.textClipping
   ```

3. **Verify**:
   ```bash
   file ~/Desktop/PageName.textClipping
   # Should show: "Apple binary property list"
   ```

4. **Present to user**:
   ```
   Your control page is ready!

   File: ~/Desktop/PageName.textClipping

   To import:
   1. Open the Indigo Mac client
   2. Go to Control Pages (Window > Control Pages)
   3. Drag the .textClipping file onto the Control Pages list
   4. The page will appear in your list — double-click to preview

   To edit later: right-click the page in Indigo and choose "Edit Control Page"
   ```

### Reference Docs

Load `docs/export/clipping-export.md` during EXPORT phase.

---

## User Preferences

Preferences are stored in `control-pages.local.md` at the skill root. This file is gitignored (user-specific).

### Format

YAML frontmatter for structured settings, plus optional markdown prose for free-form style notes:

```yaml
---
default_screen: "iPhone"
default_style: "full-control"
theme:
  background: "19 19 19"
  title_color: "FF FF FF"
# ... more settings
---

## Style Notes
Free-form notes here.
```

### Available Settings

| Key | Values | Effect |
|-----|--------|--------|
| `default_screen` | Name from `screen_presets` | Skips screen size question |
| `default_style` | `minimal`, `dashboard`, `full-control` | Skips style question |
| `screen_presets` | Map of name → "W H" | Custom screen sizes |
| `theme.*` | Color values | Page colors |
| `layout.icon_size` | "W H" | Icon dimensions |
| `layout.caption_placement` | `omit` or `4` | Label position |
| `layout.retina` | `true`/`false` | 2x image selection |
| `fonts.*` | Size/font values | Typography |

### How Preferences Apply

- **Phase 2**: Config defaults skip questions (user notified, can override)
- **Phase 3**: Layout uses config icon size, spacing, retina setting
- **Phase 4**: BUILD uses config theme colors, fonts, caption placement
- **Quick Mode**: Merges config defaults with user-provided context
