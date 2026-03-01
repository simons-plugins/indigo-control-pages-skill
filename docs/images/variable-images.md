# Variable Images Catalog

Images for variable indicators and boolean state displays. Located in `Web Assets/images/controls/variables/`.

These images use `+true.png` state suffix (not `+on.png` like device images) for boolean variable states.

---

## Status Dots

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Green Dot 2x` | default, +true | Green indicator (retina) |
| `Green Dot` | default, +true | Green indicator (1x) |
| `Red Dot 2x` | default, +true | Red indicator (retina) |
| `Red Dot` | default, +true | Red indicator (1x) |
| `Red Green Dot 2x` | default (red), +true (green) | Red/green toggle (retina) |
| `Red Green Dot` | default (red), +true (green) | Red/green toggle (1x) |
| `dot_large` | default, +true | Generic dot (large) |
| `dot_small` | default, +true | Generic dot (small) |

---

## Switches

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Switch 2x` | default, +true | Toggle switch (retina) |
| `Switch` | default, +true | Toggle switch (1x) |

---

## Buttons

### Plain Buttons

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `PlainButton_large` | default, +true | Plain button (large) |
| `PlainButton_med` | default, +true | Plain button (medium) |
| `PlainButton_small` | default, +true | Plain button (small) |

### Power Buttons

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `PowerButton_large` | default, +true | Power button (large) |
| `PowerButton_med` | default, +true | Power button (medium) |
| `PowerButton_small` | default, +true | Power button (small) |

---

## Legacy

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `iPhone_button_small_green` | default, +true | Small green button |

---

## Airfoil Speaker

| ImageFileName | States | Description |
|---------------|--------|-------------|
| `Airfoil Speaker 2x` | default, +connected, +disconnected | Airfoil speaker (retina) |
| `Airfoil Speaker` | default, +connected, +disconnected | Airfoil speaker (1x) |

---

## Usage Notes

Variable images are used with `ControlType` 2 (variable/list) elements. The `TargetElemID` should reference a variable ID, and the image state changes based on the variable's boolean value.

For boolean variables:
- Variable value is falsy (empty, "false", "0") → default image
- Variable value is truthy → `+true` image variant
