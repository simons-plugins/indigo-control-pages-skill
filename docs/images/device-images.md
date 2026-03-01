# Device Images Catalog

All device images available in `Web Assets/images/controls/devices/`.

## Naming Conventions

- **State suffix**: `+on.png` = on state, `+off.png` = off state
- **Multi-state**: `+0.png`, `+1.png`, `+2.png`, `+3.png` (e.g., fan speeds)
- **Resolution**: `2x` = retina (recommended for all new pages)
- **Size variants**: `_large`, `_med`, `_small`, `_tiny`
- **Default state**: Base filename (no suffix) = off/default state

When `ShowStateImage` is true, Indigo automatically appends the device state to the base image name.

**Important**: In the XML `ImageFileName` field, use the base name **without** `.png` extension and without state suffixes. Example: `Dimmable Light 2x` (not `Dimmable Light 2x.png` or `Dimmable Light 2x+on.png`).

---

## Lights

### Standard Light Icons (Retina)

| ImageFileName | States | Best For |
|---------------|--------|----------|
| `Dimmable Light 2x` | off, +on | Dimmers, general lights |
| `Dimmable Light` | off, +on | 1x version |

### Decorative Light Icons

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `lightbulb_large` | off, +on | Large light bulb |
| `lightbulb_small` | off, +on | Small light bulb |
| `lightfixture_large` | off, +on | Ceiling fixture |
| `lightfixture_small` | off, +on | Ceiling fixture (small) |
| `lightfixture2_large` | off, +on | Alternate ceiling fixture |
| `lightfixture2_small` | off, +on | Alternate ceiling fixture (small) |
| `floorlamp_large` | off, +on | Floor lamp |
| `floorlamp_small` | off, +on | Floor lamp (small) |
| `recessedcan_large` | off, +on | Recessed light |
| `recessedcan_med` | off, +on | Recessed light (medium) |
| `recessedcan_small` | off, +on | Recessed light (small) |
| `tracklight_large` | off, +on | Track light |
| `tracklight_med` | off, +on | Track light (medium) |
| `tracklight_small` | off, +on | Track light (small) |
| `lantern_large` | off, +on | Lantern |
| `lantern_med` | off, +on | Lantern (medium) |
| `lantern_small` | off, +on | Lantern (small) |
| `floodlight_large` | off, +on | Outdoor flood light |
| `floodlight_med` | off, +on | Outdoor flood light (medium) |
| `floodlight_small` | off, +on | Outdoor flood light (small) |
| `pathwaylight_large` | off, +on | Pathway light |
| `pathwaylight_med` | off, +on | Pathway light (medium) |
| `pathwaylight_small` | off, +on | Pathway light (small) |
| `xmastree_large` | off, +on | Christmas tree |
| `xmastree_med` | off, +on | Christmas tree (medium) |
| `xmastree_small` | off, +on | Christmas tree (small) |
| `xmastree_tiny` | off, +on | Christmas tree (tiny) |

---

## Fans

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Fan 2x` | off, +on | Standard fan (retina) |
| `Fan` | off, +on | Standard fan (1x) |
| `ceilingfan_large` | off, +on | Ceiling fan |
| `ceilingfan_med` | off, +on | Ceiling fan (medium) |
| `ceilingfan_small` | off, +on | Ceiling fan (small) |
| `ceilingfanlight_large` | off, +on | Ceiling fan with light |
| `ceilingfanlight_med` | off, +on | Ceiling fan with light (medium) |
| `ceilingfanlight_small` | off, +on | Ceiling fan with light (small) |
| `deskfan_large` | off, +on | Desk fan |
| `deskfan_med` | off, +on | Desk fan (medium) |
| `deskfan_small` | off, +on | Desk fan (small) |

### Multi-Speed Fan Controls

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `FanLinc Fan` | +0, +1, +2, +3 | FanLinc 4-speed |
| `Light Fan Control 2x` | +0, +1, +2, +3 | Light fan control (retina) |
| `Light Fan Control` | +0, +1, +2, +3 | Light fan control (1x) |

---

## Switches / Relays

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Switch 2x` | off, +on | Standard switch (retina) |
| `Switch` | off, +on | Standard switch (1x) |

### Buttons (On/Off)

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `PlainButton_large` | off, +on | Plain button (large) |
| `PlainButton_med` | off, +on | Plain button (medium) |
| `PlainButton_small` | off, +on | Plain button (small) |
| `PowerButton_large` | off, +on | Power button (large) |
| `PowerButton_med` | off, +on | Power button (medium) |
| `PowerButton_small` | off, +on | Power button (small) |

### Legacy iPhone Buttons

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `iPhone_button_small_green` | off, +on | Small green button |
| `iPhone_button_small_red` | off, +on | Small red button |
| `iPhone_button_wide_green` | off, +on | Wide green button |

---

## Thermostats

### Temperature Sensors

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Temperature Sensor 2x` | off, +on | Temperature display (retina) |
| `Temperature Sensor` | off, +on | Temperature display (1x) |

### Thermostat Status Indicators

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Thermostat Heat Status 2x` | off, +on | Heat active indicator (retina) |
| `Thermostat Heat Status` | off, +on | Heat active indicator (1x) |
| `Thermostat Cool Status 2x` | off, +on | Cool active indicator (retina) |
| `Thermostat Cool Status` | off, +on | Cool active indicator (1x) |
| `Thermostat Fan Status 2x` | off, +on | Fan running indicator (retina) |
| `Thermostat Fan Status` | off, +on | Fan running indicator (1x) |

### Thermostat Mode Controls

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Thermostat Mode` | +heat on, +cool on, +auto on, +all off | HVAC mode selector |
| `Light Thermostat Mode Control 2x` | +heat on, +cool on, +auto on, +all off | Light theme (retina) |
| `Light Thermostat Mode Control` | +heat on, +cool on, +auto on, +all off | Light theme (1x) |
| `Thermostat Fan Mode` | +always on, +auto on | Fan mode selector |
| `Light Thermostat Fan Control 2x` | +always on, +auto on | Light theme (retina) |
| `Light Thermostat Fan Control` | +always on, +auto on | Light theme (1x) |

---

## Sensors

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Motion Sensor 2x` | off, +on | Motion sensor (retina) |
| `Motion Sensor` | off, +on | Motion sensor (1x) |
| `Humidity Sensor 2x` | off, +on | Humidity sensor (retina) |
| `Humidity Sensor` | off, +on | Humidity sensor (1x) |
| `Ambient Light Sensor 2x` | off, +on | Light level sensor (retina) |
| `Ambient Light Sensor` | off, +on | Light level sensor (1x) |

---

## Status Indicators

### Dots

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Green Dot 2x` | off, +on | Green status dot (retina) |
| `Green Dot` | off, +on | Green status dot (1x) |
| `Red Dot 2x` | off, +on | Red status dot (retina) |
| `Red Dot` | off, +on | Red status dot (1x) |
| `dot_large` | off, +on | Generic dot (large) |
| `dot_small` | off, +on | Generic dot (small) |

---

## Energy / Power

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Power Meter 2x` | off, +on | Power meter (retina) |
| `Power Meter` | off, +on | Power meter (1x) |

---

## Sprinklers

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Sprinkler 2x` | off, +on | Sprinkler (retina) |
| `Sprinkler` | off, +on | Sprinkler (1x) |

---

## Garage Doors

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Garage Door` | +on, +off | Garage door |
| `Light Garage Door Control 2x` | off, +on | Light theme (retina) |
| `Light Garage Door Control` | off, +on | Light theme (1x) |
| `Light Garage Door Control Reversed 2x` | off, +on | Reversed logic (retina) |
| `Light Garage Door Control Reversed` | off, +on | Reversed logic (1x) |

---

## Media Controls

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Media Play Pause Control 2x` | +stopped, +playing, +paused | Play/pause toggle (retina) |
| `Media Play Pause Control` | +stopped, +playing, +paused | Play/pause toggle (1x) |
| `Media Play State 2x` | +stopped, +playing, +paused | Play state display (retina) |
| `Media Play State` | +stopped, +playing, +paused | Play state display (1x) |

---

## Timers

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Timer 2x` | default, +active, +paused | Timer indicator (retina) |
| `Timer` | default, +active, +paused | Timer indicator (1x) |

---

## Weather (NOAA)

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `NOAA Condition` | 100+ weather states | NOAA weather condition icons |

States include: `skc` (clear), `few` (few clouds), `sct` (scattered), `bkn` (broken), `ovc` (overcast), `ra` (rain), `sn` (snow), `tsra` (thunderstorms), `fg` (fog), and many more with night (`n` prefix) and probability (10-90 suffix) variants.

---

## iTunes / Airfoil (Legacy)

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `iTunesStatus_large` | +playing, +paused, +stopped, +error, +unavailable | iTunes status |
| `iTunesStatus_med` | same | iTunes status (medium) |
| `iTunesStatus_small` | same | iTunes status (small) |

---

## Recommended Images by Device Type

Quick reference for the most common choices:

| Device Type | Recommended ImageFileName |
|-------------|--------------------------|
| Dimmer / Light | `Dimmable Light 2x` |
| Relay / Switch | `Switch 2x` |
| Thermostat (temp display) | `Temperature Sensor 2x` |
| Thermostat (mode) | `Light Thermostat Mode Control 2x` |
| Motion Sensor | `Motion Sensor 2x` |
| Humidity Sensor | `Humidity Sensor 2x` |
| Fan | `Fan 2x` |
| Sprinkler | `Sprinkler 2x` |
| Power Meter | `Power Meter 2x` |
| Status Indicator | `Green Dot 2x` |
| Garage Door | `Light Garage Door Control 2x` |
