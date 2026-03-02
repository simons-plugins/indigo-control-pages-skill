# ControlPage XML Structure

The top-level XML structure for Indigo Control Pages.

## Wrapping Structure

All control pages must be wrapped in a `<ControlPageList>`:

```xml
<ControlPageList type="vector">
  <ControlPage type="dict">
    <!-- page properties -->
  </ControlPage>
</ControlPageList>
```

Multiple pages can be included in a single list for batch import.

## ControlPage Element

```xml
<ControlPage type="dict">
  <Category type="integer">0</Category>
  <Color type="string">19 19 19</Color>
  <ID type="integer">UNIQUE_ID</ID>
  <ImageFileName type="string"></ImageFileName>
  <Name type="string">Page Name</Name>
  <ObjVers type="integer">5</ObjVers>
  <Size type="string">375 667</Size>
  <PageElemList type="vector">
    <!-- PageElem elements here -->
  </PageElemList>
</ControlPage>
```

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `Category` | integer | Page category. Always `0` |
| `Color` | string | Background color as space-separated hex pairs (e.g., `19 19 19` for dark). Optional — omit for no background color |
| `DisplayInRemoteUI` | bool | Optional. Set to `false` to hide page from Indigo Touch and web clients. Defaults to `true` if omitted |
| `ID` | integer | Unique page ID. Generate with `python3 -c "import random; print(random.randint(100000000, 2147483647))"` |
| `ImageFileName` | string | Optional background image from `Web Assets/images/backgrounds/`. Empty string or omit for solid color |
| `Name` | string | Display name shown in Indigo's Control Pages list |
| `ObjVers` | integer | Object version. Always `5` |
| `Size` | string | Page dimensions as `"width height"` (e.g., `"375 667"`) |
| `PageElemList` | vector | Contains all `<PageElem>` elements on this page |

## Screen Size Presets

| Preset | Size | Use Case |
|--------|------|----------|
| iPhone | `375 667` | Standard phone |
| iPhone Plus | `414 736` | Large phone |
| iPad Portrait | `768 1024` | Tablet portrait |
| iPad Landscape | `1024 768` | Tablet landscape |
| Full HD | `1920 1080` | Desktop / large display |

## Backgrounds

### Solid Color Background

Set the `Color` property to a space-separated hex pair. Omit `ImageFileName` or set it to `""`.

```xml
<Color type="string">19 19 19</Color>
```

Common background colors:

| Color | Value | Use Case |
|-------|-------|----------|
| Dark (default) | `19 19 19` | Standard Indigo dark theme |
| Slightly lighter | `2A 2A 2A` | Better contrast with dark icons |
| Light gray | `CA CA CA` | Light theme, good for camera pages |
| Black | `00 00 00` | OLED-friendly |

### Background Image

Set `ImageFileName` to a filename from `Web Assets/images/backgrounds/`:

| Filename | Description |
|----------|-------------|
| `floorplan.png` | Floor plan background 1 |
| `floorplan2.png` | Floor plan background 2 |
| `floorplan3.png` | Floor plan background 3 |
| `indigo_logo.png` | Indigo logo |

### No Background (Full-Screen Image Pages)

For pages that display a full-screen external image (ControlType 101), both `Color` and `ImageFileName` can be omitted entirely. The external image element covers the page. This is the pattern used by camera feeds and timetable displays.

```xml
<!-- No Color or ImageFileName — the full-screen image IS the background -->
<ControlPage type="dict">
	<Category type="integer">0</Category>
	<ID type="integer">1624687364</ID>
	<Name type="string">Camera Feed</Name>
	<ObjVers type="integer">5</ObjVers>
	<Size type="string">1024 600</Size>
	<PageElemList type="vector">
		<!-- ControlType 101 element fills entire page -->
	</PageElemList>
</ControlPage>
```

## Critical XML Format Notes

> **Verified against real Indigo databases and working .textClipping exports:**
> - Boolean type is `type="bool"` NOT `type="boolean"`
> - Image filenames MUST include `.png` extension
> - PageElem `ObjVers` is `9` (ControlPage `ObjVers` remains `5`)
> - `ID` on PageElem is optional (Indigo assigns IDs on import)
> - `ImageFileName` on ControlPage is optional (omit for solid color background)

## Complete Example

A minimal control page with one light toggle (verified format):

```xml
<ControlPageList type="vector">
<ControlPage type="dict">
	<Category type="integer">0</Category>
	<Color type="string">19 19 19</Color>
	<ID type="integer">1234567890</ID>
	<Name type="string">Living Room</Name>
	<ObjVers type="integer">5</ObjVers>
	<Size type="string">375 667</Size>
	<PageElemList type="vector">
		<PageElem type="dict">
			<ActionGroup type="dict">
				<ActionSteps type="vector">
					<Action type="dict">
						<Class type="integer">1</Class>
						<DeviceAction type="integer">6</DeviceAction>
						<DeviceActionValue type="integer">0</DeviceActionValue>
						<DeviceID type="integer">123456789</DeviceID>
						<ObjVers type="integer">14</ObjVers>
					</Action>
				</ActionSteps>
				<ObjVers type="integer">2</ObjVers>
			</ActionGroup>
			<CaptionCurHeight type="integer">18</CaptionCurHeight>
			<CaptionCurWidth type="integer">90</CaptionCurWidth>
			<CaptionName type="string">Ceiling Light</CaptionName>
			<CaptionPlacement type="integer">4</CaptionPlacement>
			<CaptionPointSize type="integer">14</CaptionPointSize>
			<CaptionWraps type="bool">false</CaptionWraps>
			<ClientActionType type="integer">1014</ClientActionType>
			<ControlType type="integer">1</ControlType>
			<ImageFileName type="string">Dimmable Light 2x.png</ImageFileName>
			<ObjVers type="integer">9</ObjVers>
			<Position type="string">60 80</Position>
			<ShowStateImage type="bool">true</ShowStateImage>
			<ShowStateText type="bool">false</ShowStateText>
			<Size type="string">76 76</Size>
			<TargetElemID type="integer">123456789</TargetElemID>
			<TargetElemSubKey type="string">brightnessLevel</TargetElemSubKey>
		</PageElem>
	</PageElemList>
</ControlPage>
</ControlPageList>
```
