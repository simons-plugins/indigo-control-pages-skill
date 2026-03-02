# External Images (ControlType 101)

Display external images from the local filesystem with optional auto-refresh. Used for security cameras, album art, timetables, and any dynamically updating content.

> **Verified against working .textClipping exports from production Indigo installations.**

---

## Overview

Unlike standard device controls that use `ImageFileName` to reference built-in Indigo images, ControlType 101 elements use `ImageFileURL` to load images from any `file:///` path on the Indigo server. Combined with `ImageRefreshDuration`, this creates live-updating displays.

---

## Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ControlType` | integer | Yes | Must be `101` |
| `ImageFileURL` | string | Yes | `file:///` URL to the image on disk |
| `ImageRefreshDuration` | integer | No | Auto-refresh interval in milliseconds (e.g., `1000` = 1 second) |
| `Size` | string | Yes | Element dimensions `"width height"` — typically matches the image or page size |
| `Position` | string | Yes | `"X Y"` position. Negative values are valid (see Layout Notes) |
| `ShowStateImage` | bool | No | Usually `true` for external images |
| `ShowStateText` | bool | No | Usually `false` |

**Note:** `ImageFileURL` is used **instead of** `ImageFileName`. Do not use both on the same element.

---

## Common Refresh Intervals

| Use Case | Duration (ms) | Notes |
|----------|---------------|-------|
| Security camera | `1000` | 1 second — near real-time feed |
| Album art | `1000`–`4000` | Updates when track changes |
| Timetable / schedule | `30000` | 30 seconds — data changes infrequently |
| Static display | omit | No refresh needed |

---

## Anchor Element Pattern

Pages using external images commonly start with a small anchor element followed by a status text display. This pattern appears consistently across working examples:

```xml
<!-- 1. Tiny anchor element (18x18 icon indicator at top-left) -->
<PageElem type="dict">
	<ActionGroup type="dict">
		<ActionSteps type="vector">
		</ActionSteps>
		<ObjVers type="integer">2</ObjVers>
	</ActionGroup>
	<CaptionPlacement type="integer">4</CaptionPlacement>
	<ControlType type="integer">201</ControlType>
	<ObjVers type="integer">9</ObjVers>
	<Position type="string">2 2</Position>
	<ShowStateImage type="bool">true</ShowStateImage>
	<ShowStateText type="bool">false</ShowStateText>
	<Size type="string">18 18</Size>
	<StateTextAlignment type="integer">0</StateTextAlignment>
</PageElem>

<!-- 2. Status text display -->
<PageElem type="dict">
	<ActionGroup type="dict">
		<ActionSteps type="vector">
		</ActionSteps>
		<ObjVers type="integer">2</ObjVers>
	</ActionGroup>
	<CaptionCurHeight type="integer">13</CaptionCurHeight>
	<CaptionCurWidth type="integer">35</CaptionCurWidth>
	<CaptionName type="string">status:</CaptionName>
	<CaptionPlacement type="integer">4</CaptionPlacement>
	<CaptionWraps type="bool">false</CaptionWraps>
	<ControlType type="integer">200</ControlType>
	<ObjVers type="integer">9</ObjVers>
	<Position type="string">61 4</Position>
	<ShowStateImage type="bool">false</ShowStateImage>
	<ShowStateText type="bool">true</ShowStateText>
	<Size type="string">364 13</Size>
	<StateTextAlignment type="integer">0</StateTextAlignment>
</PageElem>
```

---

## Examples

### Full-Screen Image (Train Timetable)

iPhone-sized page displaying an auto-refreshing timetable image. The element fills the entire page.

Source: verified working Walton-Waterloo .textClipping export.

```xml
<ControlPageList type="vector">
<ControlPage type="dict">
	<Category type="integer">0</Category>
	<ID type="integer">1624687364</ID>
	<Name type="string">Walton-Waterloo</Name>
	<ObjVers type="integer">5</ObjVers>
	<Size type="string">414 844</Size>
	<PageElemList type="vector">
		<PageElem type="dict">
			<ActionGroup type="dict">
				<ActionSteps type="vector">
					<Action type="dict">
						<Class type="integer">0</Class>
						<ObjVers type="integer">14</ObjVers>
					</Action>
				</ActionSteps>
				<ObjVers type="integer">2</ObjVers>
			</ActionGroup>
			<CaptionPlacement type="integer">1</CaptionPlacement>
			<ControlType type="integer">101</ControlType>
			<ImageFileURL type="string">file:////Users/simon/Documents/iTravel/WALWATtimetable_mobile.png</ImageFileURL>
			<ImageRefreshDuration type="integer">30000</ImageRefreshDuration>
			<ObjVers type="integer">9</ObjVers>
			<Position type="string">0 -1</Position>
			<ShowStateImage type="bool">true</ShowStateImage>
			<ShowStateText type="bool">false</ShowStateText>
			<Size type="string">414 844</Size>
		</PageElem>
	</PageElemList>
</ControlPage>
</ControlPageList>
```

**Key points:**
- Element `Size` matches page `Size` (`414 844`) for full-screen display
- `Position: 0 -1` — slight negative Y offset is common for precise alignment
- `ImageRefreshDuration: 30000` — refreshes every 30 seconds
- No `Color` property on the page — the image covers everything

### Security Camera Feed (Landscape)

Large landscape page for a mounted display showing a security camera.

Source: verified working Drive Cam .textClipping export.

```xml
<ControlPageList type="vector">
<ControlPage type="dict">
	<Category type="integer">0</Category>
	<Color type="string">CA CA CA</Color>
	<ID type="integer">1365672249</ID>
	<Name type="string">Drive Cam</Name>
	<ObjVers type="integer">5</ObjVers>
	<Size type="string">1024 600</Size>
	<PageElemList type="vector">
		<!-- anchor + status elements omitted for brevity -->
		<PageElem type="dict">
			<ActionGroup type="dict">
				<ActionSteps type="vector">
					<Action type="dict">
						<Class type="integer">0</Class>
						<ObjVers type="integer">14</ObjVers>
					</Action>
				</ActionSteps>
				<ObjVers type="integer">2</ObjVers>
			</ActionGroup>
			<ControlType type="integer">101</ControlType>
			<ImageFileURL type="string">file:///Volumes/Recordings/SecuritySpy/Drive Cam.jpg</ImageFileURL>
			<ImageRefreshDuration type="integer">1000</ImageRefreshDuration>
			<ObjVers type="integer">9</ObjVers>
			<Position type="string">51 -39</Position>
			<ShowStateImage type="bool">true</ShowStateImage>
			<ShowStateText type="bool">false</ShowStateText>
			<Size type="string">1000 600</Size>
			<TargetElemSubKey type="string">sensorValue</TargetElemSubKey>
		</PageElem>
	</PageElemList>
</ControlPage>
</ControlPageList>
```

**Key points:**
- `ImageRefreshDuration: 1000` — 1-second refresh for near real-time camera feed
- Light gray background (`CA CA CA`) visible around the image edges
- Element slightly larger positioning with `Position: 51 -39` — negative Y shifts image up
- JPG format works — not limited to PNG for external images

### Album Art with Media Controls (Sonos)

Wide landscape page with two album art panels and transport controls.

Source: verified working Sonos .textClipping export.

```xml
<!-- Album art panel (one of two side-by-side) -->
<PageElem type="dict">
	<ActionGroup type="dict">
		<ActionSteps type="vector">
			<Action type="dict">
				<Class type="integer">0</Class>
				<ObjVers type="integer">14</ObjVers>
			</Action>
		</ActionSteps>
		<ObjVers type="integer">2</ObjVers>
	</ActionGroup>
	<ControlType type="integer">101</ControlType>
	<ImageFileURL type="string">file:///Library/Application%20Support/Perceptive%20Automation/images/Sonos/Study_art.jpg</ImageFileURL>
	<ImageRefreshDuration type="integer">4000</ImageRefreshDuration>
	<ObjVers type="integer">9</ObjVers>
	<Position type="string">11 40</Position>
	<ShowStateImage type="bool">true</ShowStateImage>
	<ShowStateText type="bool">false</ShowStateText>
	<Size type="string">500 500</Size>
	<TargetElemSubKey type="string">sensorValue</TargetElemSubKey>
</PageElem>
```

**Key points:**
- Two 500x500 art panels side-by-side in a 1200x704 page (x=11 and x=600)
- URL-encoded spaces in path (`%20`)
- Images served from Indigo's own Application Support directory
- Media transport buttons (ControlType 1/100 with Class 999 plugin actions) positioned below the art panels

---

## Layout Notes

### Negative Positions

Elements can use negative `Position` values. This is common for:
- Fine-tuning image alignment (e.g., `0 -1` to nudge up by 1px)
- Placing elements partially off-screen
- Hiding elements that serve as data sources but don't need to be visible

### Element Size vs Page Size

- For full-screen image displays, set element `Size` equal to page `Size`
- Elements can be larger than the page — they simply extend beyond the visible area
- There is no auto-scaling; the image is displayed at the specified pixel dimensions

### Image Formats

External images support multiple formats:
- `.png` — standard, supports transparency
- `.jpg` / `.jpeg` — smaller file size, good for photos and camera feeds
- The format is determined by the actual file, not the extension in the URL
