# Indigo Control Page Builder

**Repository**: https://github.com/simons-plugins/indigo-control-pages
**Version**: 1.0.0
**Slash command**: `/control-page`

## Description

Guided builder for Indigo home automation Control Pages. Designs layouts
with ASCII wireframes, generates valid Indigo XML, and exports ready-to-import
.textClipping files.

## CRITICAL: Context Optimization Strategy

**DO NOT load all files.** Load docs selectively based on current workflow phase.

### Phase-Based Loading

| Current Phase | Load These Files |
|---------------|-----------------|
| Starting (any request) | `docs/workflow.md` |
| DISCOVER (finding devices) | `docs/workflow.md` (Phase 1 section) |
| PLAN (asking questions) | `docs/workflow.md` (Phase 2 section), `docs/layouts/sizing.md` |
| WIREFRAME (designing layout) | `docs/layouts/templates.md`, `docs/layouts/sizing.md` |
| BUILD (generating XML) | `docs/schema/control-page.md`, `docs/schema/page-elements.md`, `docs/schema/actions.md`, `docs/schema/enums.md` |
| BUILD (choosing images) | `docs/images/device-images.md` |
| EXPORT (creating file) | `docs/export/clipping-export.md` |

### Query Routing

| User Says | Load |
|-----------|------|
| "Create a control page" | `docs/workflow.md` → start Phase 1 |
| "What images are available?" | `docs/images/device-images.md` |
| "Show me templates" | `docs/layouts/templates.md` |
| "What screen sizes?" | `docs/layouts/sizing.md` |
| "How do I import?" | `docs/export/clipping-export.md` |
| "What XML properties?" | `docs/schema/page-elements.md` |
| "What actions can I use?" | `docs/schema/actions.md` |
| "What are the enum values?" | `docs/schema/enums.md` |
| "Show me static images" | `docs/images/static-images.md` |
| "Variable images?" | `docs/images/variable-images.md` |

## Workflow Overview

5 phases: DISCOVER → PLAN → WIREFRAME → BUILD → EXPORT

1. Query devices via MCP (`search_entities`, `get_devices_by_type`) or database fallback
2. Ask user about room, devices, screen size, style
3. Generate ASCII wireframe, iterate with user
4. Convert to Indigo XML with real device IDs
5. Create .textClipping file for drag-and-drop import

## Quick Mode

Experienced users can say "Create a control page for the living room with
the ceiling light, floor lamp, and thermostat on iPhone" — skip straight
to wireframing with sensible defaults.

## Documentation Structure

```
docs/
├── workflow.md                    # 5-phase guided process
├── schema/
│   ├── control-page.md            # ControlPage XML structure
│   ├── page-elements.md           # PageElem types & properties
│   ├── actions.md                 # ActionGroup/Action classes
│   └── enums.md                   # All enumeration values
├── images/
│   ├── device-images.md           # Device state images catalog
│   ├── static-images.md           # Buttons, tiles, arrows
│   └── variable-images.md         # Variable indicators
├── layouts/
│   ├── templates.md               # Pre-built room templates
│   └── sizing.md                  # Screen sizes, spacing, grid
└── export/
    └── clipping-export.md         # Export process + script docs

tools/
└── create_clipping.py             # .textClipping generator
```

## Best Practices

- Always use 2x (retina) images for new pages
- Use `ClientActionType` 1014 for dimmers and thermostats (popup control)
- Use empty ActionGroup for display-only elements (sensors)
- Generate unique IDs for pages and elements using random integers
- Dark theme (`19 19 19` background) is the standard Indigo look
- Test with a simple page first before building complex layouts
