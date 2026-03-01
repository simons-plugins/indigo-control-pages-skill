# PageElem Properties Reference

Complete reference for `<PageElem>` elements within a Control Page.

> **CRITICAL CORRECTIONS (verified against real Indigo databases and working .textClipping exports):**
> - Boolean type is `type="bool"` NOT `type="boolean"`
> - Image filenames MUST include `.png` extension (e.g., `Dimmable Light 2x.png`)
> - PageElem `ObjVers` is `9` NOT `5`
> - `ID` on PageElem is optional (Indigo assigns IDs on import)
> - Device actions should include `<DeviceActionValue type="integer">0</DeviceActionValue>`
> - No-op actions use `<Class type="integer">0</Class>` inside ActionSteps
> - `Size` of `0 0` is valid — Indigo auto-sizes from the image

## PageElem Structure

Every element on a control page is a `<PageElem type="dict">` inside the `<PageElemList>`.

```xml
<PageElem type="dict">
  <!-- Core -->
  <ControlType type="integer">1</ControlType>
  <ObjVers type="integer">9</ObjVers>
  <Position type="string">100 200</Position>
  <Size type="string">76 76</Size>

  <!-- Image -->
  <ImageFileName type="string">Dimmable Light 2x.png</ImageFileName>
  <ShowStateImage type="bool">true</ShowStateImage>
  <ShowStateText type="bool">false</ShowStateText>

  <!-- Caption (label) -->
  <CaptionName type="string">Label Text</CaptionName>
  <CaptionPlacement type="integer">4</CaptionPlacement>
  <CaptionPointSize type="integer">14</CaptionPointSize>
  <CaptionWraps type="bool">false</CaptionWraps>
  <CaptionCurWidth type="integer">90</CaptionCurWidth>
  <CaptionCurHeight type="integer">18</CaptionCurHeight>

  <!-- State text (only when ShowStateText is true) -->
  <StateTextPointSize type="integer">20</StateTextPointSize>

  <!-- Target device -->
  <TargetElemID type="integer">DEVICE_ID</TargetElemID>
  <TargetElemSubKey type="string">brightnessLevel</TargetElemSubKey>

  <!-- Action -->
  <ActionGroup type="dict">...</ActionGroup>
  <ClientActionType type="integer">1014</ClientActionType>
</PageElem>
```

---

## Property Groups

### Core Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ControlType` | integer | Yes | Element type. See enums.md |
| `ObjVers` | integer | Yes | Always `9` for PageElems |
| `Position` | string | Yes | `"X Y"` position from top-left of page |
| `Size` | string | No | `"width height"` in pixels. Use `0 0` for auto-size from image |

### Image Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `ImageFileName` | string | `""` | Image name WITH `.png` extension (e.g., `Dimmable Light 2x.png`). State suffixes added automatically by Indigo |
| `ShowStateImage` | bool | `false` | Show state-dependent image (e.g., on/off variant) |
| `ShowStateText` | bool | `false` | Show device state as text overlay on the image |

**Image state behavior**: When `ShowStateImage` is true, Indigo automatically looks for state-suffixed images. For example, `Dimmable Light 2x.png` resolves to `Dimmable Light 2x+on.png` when the light is on.

### Caption Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `CaptionName` | string | `""` | Label text displayed with the element |
| `CaptionFontType` | integer | `22` | Font type (optional — omit to use Indigo defaults). See enums.md |
| `CaptionFontColor` | string | `"FF FF FF"` | Caption color (optional — omit to use defaults) |
| `CaptionPointSize` | integer | `14` | Font size in points |
| `CaptionPlacement` | integer | `4` | Position relative to image. See enums.md |
| `CaptionWraps` | bool | `false` | Allow text wrapping. Use `type="bool"` NOT `type="boolean"` |
| `CaptionCurWidth` | integer | `90` | Caption bounding box width |
| `CaptionCurHeight` | integer | `18` | Caption bounding box height |

**Note:** `CaptionFontType` and `CaptionFontColor` are optional. Working examples from real Indigo pages often omit them, letting Indigo use its defaults.

### State Text Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `StateTextPointSize` | integer | `20` | State text font size |
| `StateTextAlignment` | integer | `0` | 0 = left, 1 = center |

**Note:** `StateTextFontColor` and `StateTextFontType` are optional. Working examples often only include `StateTextPointSize`.

### Target Properties

| Property | Type | Description |
|----------|------|-------------|
| `TargetElemID` | integer | Device ID to monitor/control |
| `TargetElemSubKey` | string | Which device state to display. See enums.md for values |

### Action Properties

| Property | Type | Description |
|----------|------|-------------|
| `ActionGroup` | dict | Action to execute when element is tapped. See actions.md |
| `ClientActionType` | integer | Client-side action. `0` = none, `1014` = popup control dialog |

---

## Common Element Examples

> **All examples below are verified against real Indigo databases and working .textClipping exports.**

### Text Label (Title)

```xml
<PageElem type="dict">
	<ActionGroup type="dict">
		<ActionSteps type="vector">
		</ActionSteps>
		<ObjVers type="integer">2</ObjVers>
	</ActionGroup>
	<CaptionCurHeight type="integer">26</CaptionCurHeight>
	<CaptionCurWidth type="integer">100</CaptionCurWidth>
	<CaptionFontColor type="string">FF FF FF</CaptionFontColor>
	<CaptionFontType type="integer">22</CaptionFontType>
	<CaptionName type="string">Living Room</CaptionName>
	<CaptionPlacement type="integer">5</CaptionPlacement>
	<CaptionPointSize type="integer">22</CaptionPointSize>
	<CaptionWraps type="bool">false</CaptionWraps>
	<ControlType type="integer">100</ControlType>
	<ObjVers type="integer">9</ObjVers>
	<Position type="string">138 20</Position>
	<ShowStateImage type="bool">false</ShowStateImage>
	<ShowStateText type="bool">false</ShowStateText>
	<Size type="string">0 0</Size>
</PageElem>
```

### Light Toggle with State Image and Dimmer Popup

Tapping toggles the light. Long-press opens dimmer popup.
Source: verified against Indigo 2025.1 Sample House database.

```xml
<PageElem type="dict">
	<ActionGroup type="dict">
		<ActionSteps type="vector">
			<Action type="dict">
				<Class type="integer">1</Class>
				<DeviceAction type="integer">6</DeviceAction>
				<DeviceActionValue type="integer">0</DeviceActionValue>
				<DeviceID type="integer">DEVICE_ID</DeviceID>
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
	<TargetElemID type="integer">DEVICE_ID</TargetElemID>
	<TargetElemSubKey type="string">brightnessLevel</TargetElemSubKey>
</PageElem>
```

### Thermostat with Temperature Display and Popup

Shows current temperature. Tapping opens thermostat control popup.

```xml
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
	<CaptionCurHeight type="integer">18</CaptionCurHeight>
	<CaptionCurWidth type="integer">90</CaptionCurWidth>
	<CaptionName type="string">Thermostat</CaptionName>
	<CaptionPlacement type="integer">4</CaptionPlacement>
	<CaptionPointSize type="integer">14</CaptionPointSize>
	<CaptionWraps type="bool">false</CaptionWraps>
	<ClientActionType type="integer">1014</ClientActionType>
	<ControlType type="integer">1</ControlType>
	<ImageFileName type="string">Temperature Sensor 2x.png</ImageFileName>
	<ObjVers type="integer">9</ObjVers>
	<Position type="string">150 350</Position>
	<ShowStateImage type="bool">true</ShowStateImage>
	<ShowStateText type="bool">true</ShowStateText>
	<Size type="string">76 76</Size>
	<StateTextPointSize type="integer">20</StateTextPointSize>
	<TargetElemID type="integer">DEVICE_ID</TargetElemID>
	<TargetElemSubKey type="string">temperatureInputsAll</TargetElemSubKey>
</PageElem>
```

### Sensor with State Display (Display Only)

Shows sensor state. No action on tap. Source: verified against working Alarm .textClipping export.

```xml
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
	<CaptionCurHeight type="integer">13</CaptionCurHeight>
	<CaptionCurWidth type="integer">58</CaptionCurWidth>
	<CaptionName type="string">Front Door</CaptionName>
	<CaptionWraps type="bool">false</CaptionWraps>
	<ControlType type="integer">1</ControlType>
	<ImageFileName type="string">alarm_zone_led_lg+.png</ImageFileName>
	<ObjVers type="integer">9</ObjVers>
	<Position type="string">330 299</Position>
	<ShowStateImage type="bool">true</ShowStateImage>
	<ShowStateText type="bool">false</ShowStateText>
	<Size type="string">48 30</Size>
	<TargetElemID type="integer">DEVICE_ID</TargetElemID>
	<TargetElemSubKey type="string">onOffState</TargetElemSubKey>
</PageElem>
```

### Action Group Button

Executes an Indigo action group when tapped.
Source: verified against Indigo 2025.1 Sample House database.

```xml
<PageElem type="dict">
	<ActionGroup type="dict">
		<ActionSteps type="vector">
			<Action type="dict">
				<ActionGroupID type="integer">ACTION_GROUP_ID</ActionGroupID>
				<Class type="integer">100</Class>
				<ObjVers type="integer">14</ObjVers>
			</Action>
		</ActionSteps>
		<ObjVers type="integer">2</ObjVers>
	</ActionGroup>
	<CaptionCurHeight type="integer">20</CaptionCurHeight>
	<CaptionCurWidth type="integer">32</CaptionCurWidth>
	<CaptionName type="string">All Off</CaptionName>
	<CaptionPlacement type="integer">1</CaptionPlacement>
	<CaptionPointSize type="integer">18</CaptionPointSize>
	<CaptionWraps type="bool">false</CaptionWraps>
	<ControlType type="integer">100</ControlType>
	<ImageFileName type="string">Light Button Solid Small.png</ImageFileName>
	<ObjVers type="integer">9</ObjVers>
	<Position type="string">150 400</Position>
	<ShowStateImage type="bool">true</ShowStateImage>
	<ShowStateText type="bool">false</ShowStateText>
	<Size type="string">92 29</Size>
	<TargetElemSubKey type="string">onOffState</TargetElemSubKey>
</PageElem>
```

### Relay / Switch Toggle

```xml
<PageElem type="dict">
	<ActionGroup type="dict">
		<ActionSteps type="vector">
			<Action type="dict">
				<Class type="integer">1</Class>
				<DeviceAction type="integer">6</DeviceAction>
				<DeviceActionValue type="integer">0</DeviceActionValue>
				<DeviceID type="integer">DEVICE_ID</DeviceID>
				<ObjVers type="integer">14</ObjVers>
			</Action>
		</ActionSteps>
		<ObjVers type="integer">2</ObjVers>
	</ActionGroup>
	<CaptionCurHeight type="integer">18</CaptionCurHeight>
	<CaptionCurWidth type="integer">90</CaptionCurWidth>
	<CaptionName type="string">Power Switch</CaptionName>
	<CaptionPlacement type="integer">4</CaptionPlacement>
	<CaptionPointSize type="integer">14</CaptionPointSize>
	<CaptionWraps type="bool">false</CaptionWraps>
	<ControlType type="integer">1</ControlType>
	<ImageFileName type="string">Switch 2x.png</ImageFileName>
	<ObjVers type="integer">9</ObjVers>
	<Position type="string">77 170</Position>
	<ShowStateImage type="bool">true</ShowStateImage>
	<ShowStateText type="bool">false</ShowStateText>
	<Size type="string">76 76</Size>
	<TargetElemID type="integer">DEVICE_ID</TargetElemID>
	<TargetElemSubKey type="string">onOffState</TargetElemSubKey>
</PageElem>
```
