# Export: .textClipping Files

How to create and import `.textClipping` files for Indigo Control Pages.

---

## What is a .textClipping File?

A `.textClipping` is a macOS file format (binary plist) that stores text content in multiple encodings. When you drag text from an application and drop it on the Desktop, macOS creates a `.textClipping` file.

Indigo uses this format for importing Control Pages — you can drag a `.textClipping` file containing Control Page XML onto the Control Pages list in the Indigo Mac client.

## File Structure

The `.textClipping` binary plist contains two top-level keys:

### UTI-Data

Contains the XML text in three encodings:

| Key | Type | Description |
|-----|------|-------------|
| `public.utf8-plain-text` | string | XML as UTF-8 string |
| `public.utf16-plain-text` | bytes | XML as UTF-16LE (no BOM), CR line endings |
| `com.apple.traditional-mac-plain-text` | bytes | XML as Mac Roman, CR line endings |

### OSType-Data

Contains NSKeyedArchiver metadata with an `ItemArray` listing the names of items in the clipping (typically the page name).

---

## Using the Helper Script

The `create_clipping.py` script in `tools/` generates valid `.textClipping` files.

### Usage

```bash
# From stdin (pipe XML)
cat page.xml | python3 tools/create_clipping.py output.textClipping

# From --xml argument
python3 tools/create_clipping.py output.textClipping --xml '<ControlPageList>...</ControlPageList>'

# With explicit item names
python3 tools/create_clipping.py output.textClipping --name "Living Room" --name "Kitchen"
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `output` | Yes | Output file path (should end in `.textClipping`) |
| `--xml` | No | XML string. If omitted, reads from stdin |
| `--name` | No | Item name(s) for metadata. Auto-detected from `<Name>` elements if omitted |

### Output

```
Created: /Users/you/Desktop/Living Room.textClipping
  XML length: 4523 chars
  Item names: ['Living Room']
  File size: 6789 bytes
```

### Verification

```bash
# Check file type
file output.textClipping
# Expected: "Apple binary property list"

# Inspect contents (optional)
plutil -p output.textClipping
```

---

## Import into Indigo

1. Open the **Indigo Mac client**
2. Go to **Window > Control Pages** (or click "Control Pages" in the sidebar)
3. **Drag** the `.textClipping` file onto the Control Pages list
4. The page appears in your list
5. **Double-click** the page name to preview it
6. **Right-click > Edit Control Page** to modify in Indigo's visual editor

---

## Troubleshooting

### Import fails silently

- Verify the file is a valid binary plist: `file output.textClipping` should show "Apple binary property list"
- Check the XML wrapping: must start with `<ControlPageList type="vector">` and end with `</ControlPageList>`
- Ensure all device IDs are valid integers
- Check for XML syntax errors (unclosed tags, invalid characters)

### Page appears but elements are missing

- Verify `ImageFileName` values match actual image names (case-sensitive)
- Check `Position` values are within page `Size` bounds
- Ensure `ControlType` is set correctly for each element

### Page appears but devices show "not found"

- Device IDs must match real devices in your Indigo installation
- Re-run Phase 1 (DISCOVER) to get current device IDs
- Verify device IDs are integers, not strings

### Script errors

- Requires Python 3.10+ (ships with Indigo 2025.1)
- Use the Python bundled with Indigo: `/Library/Frameworks/Python.framework/Versions/Current/bin/python3`
- Ensure XML input is not empty

---

## Manual Alternative

If the script is unavailable, you can create a `.textClipping` manually:

1. Copy the complete XML to the clipboard
2. Open TextEdit (plain text mode)
3. Paste the XML
4. Select all text
5. Drag the selected text to the Desktop
6. macOS creates a `.textClipping` file automatically
7. Drag that file onto Indigo's Control Pages list
