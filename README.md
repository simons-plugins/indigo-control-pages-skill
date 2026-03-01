# Indigo Control Page Builder Skill

Community-maintained Claude Code skill for designing and building [Indigo](https://www.indigodomo.com) Control Pages. Guides you through a 5-phase workflow with ASCII wireframe previews, generates valid Indigo XML, and exports ready-to-import `.textClipping` files.

## What is This?

This is a Claude Code skill that provides a guided builder for Indigo home automation Control Pages. It walks you through device discovery, layout planning, wireframe previewing, XML generation, and file export — all within a conversational workflow.

## Requirements

- **Indigo 2025.1+** (Control Pages feature)
- **Claude Code** with skill support
- **Optional**: Indigo MCP server for automatic device discovery

## Installation

### Option 1: Clone into your project

```bash
cd /path/to/your/indigo/project
mkdir -p .claude/skills
cd .claude/skills
git clone https://github.com/simons-plugins/indigo-control-pages-skill.git control-pages
```

### Option 2: Add as submodule

```bash
cd /path/to/your/indigo/project
mkdir -p .claude/skills
git submodule add https://github.com/simons-plugins/indigo-control-pages-skill.git .claude/skills/control-pages
```

### Option 3: Symlink (for multiple projects)

```bash
# Clone once
git clone https://github.com/simons-plugins/indigo-control-pages-skill.git ~/indigo-control-pages

# Symlink in each project
cd /path/to/your/indigo/project
mkdir -p .claude/skills
ln -s ~/indigo-control-pages .claude/skills/control-pages
```

## Usage

Once installed, invoke the skill in Claude Code:

```
/control-page "Create a living room panel"
/control-page "Build a control page for the kitchen lights"
/control-page "What images are available for thermostats?"
/control-page "Show me layout templates"
```

The skill guides you through 5 phases:

1. **DISCOVER** — Find devices via MCP or Indigo database
2. **PLAN** — Choose room, devices, screen size, and style
3. **WIREFRAME** — Preview ASCII layout, iterate on design
4. **BUILD** — Generate valid Indigo XML with real device IDs
5. **EXPORT** — Create `.textClipping` file for drag-and-drop import

## What's Included

- **Workflow guide** — 5-phase guided process with interactive prompts
- **XML schema reference** — Complete documentation of Indigo Control Page XML format
- **Image catalog** — All available device, static, and variable images
- **Layout templates** — Pre-built room templates with complete XML examples
- **Sizing guide** — Screen presets, spacing constants, positioning formulas
- **Export tools** — Python script for `.textClipping` file generation

## Documentation

All documentation is organized in the `docs/` directory:

| Directory | Contents |
|-----------|----------|
| `docs/workflow.md` | 5-phase guided builder process |
| `docs/schema/` | XML schema reference (control pages, elements, actions, enums) |
| `docs/images/` | Image catalog (devices, static, variables) |
| `docs/layouts/` | Layout templates and sizing guide |
| `docs/export/` | Export process and clipping script docs |
| `tools/` | Python helper scripts |

## Contributing

We welcome contributions from the Indigo developer community!

- Report issues: https://github.com/simons-plugins/indigo-control-pages-skill/issues
- Submit PRs: https://github.com/simons-plugins/indigo-control-pages-skill/pulls

## License

MIT License
