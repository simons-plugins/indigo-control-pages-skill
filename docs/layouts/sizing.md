# Sizing and Layout Guide

Screen presets, spacing constants, and positioning formulas for Control Page layouts.

---

## Screen Presets

| Preset | Size (W x H) | Columns | Column Width |
|--------|--------------|---------|-------------|
| iPhone | 375 x 667 | 2 | ~170px |
| iPhone Plus | 414 x 736 | 2 | ~190px |
| iPad Portrait | 768 x 1024 | 3 | ~230px |
| iPad Landscape | 1024 x 768 | 4 | ~230px |
| Full HD | 1920 x 1080 | 6 | ~290px |

---

## Spacing Constants

```
Page padding:       30px (left/right), 20px (top)
Element spacing:    90px vertical between rows, 20px horizontal gap
Icon size:          76x76 (2x retina images)
                    38x38 (1x standard images)
Label offset:       CaptionPlacement omit (below image, default) or 4 (left of icon)
Title height:       30px
Title margin:       20px below title before first element row
```

---

## Font Sizes

| Use | Size | FontType | Color |
|-----|------|----------|-------|
| Page title | 22pt | 22 (bold) | `FF FF FF` (white) |
| Section header | 20pt | 22 (bold) | `FF FF FF` (white) |
| Device label | 20pt | 22 (bold) | `BF BF BF` (light gray) |
| State text | 20pt | 201 (mono) | `DB DB DB` (medium gray) |
| Small text | 16pt | 20 (regular) | `BF BF BF` (light gray) |

---

## Color Palette (Dark Theme)

| Use | Color Value | Appearance |
|-----|-------------|------------|
| Background | `19 19 19` | Near black |
| Title text | `FF FF FF` | White |
| Label text | `BF BF BF` | Light gray |
| State text | `DB DB DB` | Medium gray |
| Dim text | `33 33 33` | Dark gray |

---

## Positioning Formulas

### 2-Column Layout (iPhone 375px)

```
Available width = 375 - (2 × 30) = 315px
Column width = (315 - 20) / 2 = ~147px
Icon width = 76px

Col 1 center X = 30 + (147/2) = 103
Col 1 icon X = 103 - (76/2) = 65

Col 2 center X = 30 + 147 + 20 + (147/2) = 270
Col 2 icon X = 270 - (76/2) = 232

Title Y = 20
Row 1 Y = 70  (title + spacing)
Row 2 Y = 160 (row 1 + 90)
Row 3 Y = 250 (row 2 + 90)
Row N Y = 70 + ((N-1) × 90)
```

### 2-Column Layout (iPhone Plus 414px)

```
Available width = 414 - (2 × 30) = 354px
Column width = (354 - 20) / 2 = 167px

Col 1 icon X = 30 + (167/2) - 38 = 75
Col 2 icon X = 30 + 167 + 20 + (167/2) - 38 = 262
```

### 3-Column Layout (iPad Portrait 768px)

```
Available width = 768 - (2 × 30) = 708px
Column width = (708 - 2×20) / 3 = ~222px

Col 1 icon X = 30 + (222/2) - 38 = 103
Col 2 icon X = 30 + 222 + 20 + (222/2) - 38 = 345
Col 3 icon X = 30 + 2×(222+20) + (222/2) - 38 = 587
```

### 4-Column Layout (iPad Landscape 1024px)

```
Available width = 1024 - (2 × 30) = 964px
Column width = (964 - 3×20) / 4 = ~226px

Col 1 icon X = 30 + (226/2) - 38 = 105
Col 2 icon X = 30 + 226 + 20 + (226/2) - 38 = 351
Col 3 icon X = 30 + 2×(226+20) + (226/2) - 38 = 597
Col 4 icon X = 30 + 3×(226+20) + (226/2) - 38 = 843
```

---

## Element Sizing Reference

| Element Type | Typical Size | Notes |
|--------------|-------------|-------|
| Device icon (2x) | 76 x 76 | Standard retina icon |
| Device icon (1x) | 38 x 38 | Standard icon |
| Title text | 300 x 30 | Full-width text |
| Caption text | 150 x 25 | Below-icon label |
| Solid button (medium) | 100 x 38 | Action button |
| Solid button (large) | 150 x 38 | Wide action button |
| Tile header/footer | varies | Match tile size |
| Tile body | varies | Stretchable middle |

---

## General Layout Tips

1. **Center the title**: Position X = (page_width / 2) - (title_width / 2)
2. **Group by function**: Put all lights together, thermostats together, etc.
3. **Leave breathing room**: Don't fill every pixel — whitespace improves readability
4. **Consistent spacing**: Use the same vertical gap (90px) between all rows
5. **Align columns**: Icons in the same column should share the same X position
6. **State text below icon**: For Dashboard style, state text appears centered below the icon when ShowStateText is true
7. **Caption below state text**: With CaptionPlacement omit (default), the label appears below the icon/state text area. CaptionPlacement 4 places the label to the left of the icon.
8. **Custom presets**: Users can add custom screen presets in `control-pages.local.md` (see User Preferences in workflow.md)
