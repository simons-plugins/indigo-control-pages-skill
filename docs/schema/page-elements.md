# PageElem Properties Reference

Complete reference for `<PageElem>` elements within a Control Page.

## PageElem Structure

Every element on a control page is a `<PageElem type="dict">` inside the `<PageElemList>`.

```xml
<PageElem type="dict">
  <!-- Core -->
  <ControlType type="integer">1</ControlType>
  <ID type="integer">UNIQUE_ID</ID>
  <ObjVers type="integer">5</ObjVers>
  <Position type="string">100 200</Position>
  <Size type="string">76 76</Size>

  <!-- Image -->
  <ImageFileName type="string">Dimmable Light 2x</ImageFileName>
  <ShowStateImage type="boolean">true</ShowStateImage>
  <ShowStateText type="boolean">true</ShowStateText>

  <!-- Caption (label) -->
  <CaptionName type="string">Label Text</CaptionName>
  <CaptionFontType type="integer">22</CaptionFontType>
  <CaptionFontColor type="string">BF BF BF</CaptionFontColor>
  <CaptionPointSize type="integer">20</CaptionPointSize>
  <CaptionPlacement type="integer">4</CaptionPlacement>
  <CaptionWraps type="boolean">true</CaptionWraps>
  <CaptionCurWidth type="integer">150</CaptionCurWidth>
  <CaptionCurHeight type="integer">25</CaptionCurHeight>

  <!-- State text -->
  <StateTextFontColor type="string">DB DB DB</StateTextFontColor>
  <StateTextFontType type="integer">201</StateTextFontType>
  <StateTextPointSize type="integer">20</StateTextPointSize>
  <StateTextAlignment type="integer">1</StateTextAlignment>

  <!-- Target device -->
  <TargetElemID type="integer">DEVICE_ID</TargetElemID>
  <TargetElemSubKey type="string">onOffState</TargetElemSubKey>

  <!-- Action -->
  <ActionGroup type="dict">...</ActionGroup>
  <ClientActionType type="integer">0</ClientActionType>
</PageElem>
```

---

## Property Groups

### Core Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ControlType` | integer | Yes | Element type. See enums.md |
| `ID` | integer | Yes | Unique element ID |
| `ObjVers` | integer | Yes | Always `5` |
| `Position` | string | Yes | `"X Y"` position from top-left of page |
| `Size` | string | No | `"width height"` in pixels. Default varies by image |

### Image Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `ImageFileName` | string | `""` | Base image name without `.png` extension. State suffixes added automatically |
| `ShowStateImage` | boolean | `false` | Show state-dependent image (e.g., on/off variant) |
| `ShowStateText` | boolean | `false` | Show device state as text overlay on the image |

**Image state behavior**: When `ShowStateImage` is true, Indigo appends the device state to the image filename. For example, `Dimmable Light 2x` becomes `Dimmable Light 2x+on.png` when the light is on.

### Caption Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `CaptionName` | string | `""` | Label text displayed with the element |
| `CaptionFontType` | integer | `20` | Font type. See enums.md |
| `CaptionFontColor` | string | `"BF BF BF"` | Caption color (hex pairs) |
| `CaptionPointSize` | integer | `20` | Font size in points |
| `CaptionPlacement` | integer | `4` | Position relative to image. See enums.md |
| `CaptionWraps` | boolean | `true` | Allow text wrapping |
| `CaptionCurWidth` | integer | `150` | Caption bounding box width |
| `CaptionCurHeight` | integer | `25` | Caption bounding box height |

### State Text Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `StateTextFontColor` | string | `"DB DB DB"` | State text color (hex pairs) |
| `StateTextFontType` | integer | `201` | Font for state text (201 = monospace) |
| `StateTextPointSize` | integer | `20` | State text font size |
| `StateTextAlignment` | integer | `1` | 0 = left, 1 = center |

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

### Text Label (Title)

```xml
<PageElem type="dict">
  <ActionGroup type="dict">
    <ActionSteps type="vector">
    </ActionSteps>
    <ObjVers type="integer">2</ObjVers>
  </ActionGroup>
  <CaptionFontColor type="string">FF FF FF</CaptionFontColor>
  <CaptionFontType type="integer">22</CaptionFontType>
  <CaptionName type="string">Living Room</CaptionName>
  <CaptionPlacement type="integer">5</CaptionPlacement>
  <CaptionPointSize type="integer">22</CaptionPointSize>
  <CaptionWraps type="boolean">true</CaptionWraps>
  <CaptionCurWidth type="integer">300</CaptionCurWidth>
  <CaptionCurHeight type="integer">30</CaptionCurHeight>
  <ControlType type="integer">100</ControlType>
  <ID type="integer">ELEM_ID</ID>
  <ImageFileName type="string"></ImageFileName>
  <ObjVers type="integer">5</ObjVers>
  <Position type="string">37 20</Position>
  <ShowStateImage type="boolean">false</ShowStateImage>
  <ShowStateText type="boolean">false</ShowStateText>
  <Size type="string">300 30</Size>
</PageElem>
```

### Light Toggle with State Image

Tapping toggles the light. Shows on/off image state.

```xml
<PageElem type="dict">
  <ActionGroup type="dict">
    <ActionSteps type="vector">
      <Action type="dict">
        <Class type="integer">1</Class>
        <DeviceAction type="integer">6</DeviceAction>
        <DeviceID type="integer">DEVICE_ID</DeviceID>
        <ObjVers type="integer">14</ObjVers>
      </Action>
    </ActionSteps>
    <ObjVers type="integer">2</ObjVers>
  </ActionGroup>
  <CaptionFontColor type="string">BF BF BF</CaptionFontColor>
  <CaptionFontType type="integer">22</CaptionFontType>
  <CaptionName type="string">Ceiling Light</CaptionName>
  <CaptionPlacement type="integer">4</CaptionPlacement>
  <CaptionPointSize type="integer">20</CaptionPointSize>
  <ClientActionType type="integer">1014</ClientActionType>
  <ControlType type="integer">1</ControlType>
  <ID type="integer">ELEM_ID</ID>
  <ImageFileName type="string">Dimmable Light 2x</ImageFileName>
  <ObjVers type="integer">5</ObjVers>
  <Position type="string">77 80</Position>
  <ShowStateImage type="boolean">true</ShowStateImage>
  <ShowStateText type="boolean">false</ShowStateText>
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
    </ActionSteps>
    <ObjVers type="integer">2</ObjVers>
  </ActionGroup>
  <CaptionFontColor type="string">BF BF BF</CaptionFontColor>
  <CaptionFontType type="integer">22</CaptionFontType>
  <CaptionName type="string">Thermostat</CaptionName>
  <CaptionPlacement type="integer">4</CaptionPlacement>
  <CaptionPointSize type="integer">20</CaptionPointSize>
  <ClientActionType type="integer">1014</ClientActionType>
  <ControlType type="integer">1</ControlType>
  <ID type="integer">ELEM_ID</ID>
  <ImageFileName type="string">Temperature Sensor 2x</ImageFileName>
  <ObjVers type="integer">5</ObjVers>
  <Position type="string">267 170</Position>
  <ShowStateImage type="boolean">true</ShowStateImage>
  <ShowStateText type="boolean">true</ShowStateText>
  <Size type="string">76 76</Size>
  <StateTextFontColor type="string">DB DB DB</StateTextFontColor>
  <StateTextFontType type="integer">201</StateTextFontType>
  <StateTextPointSize type="integer">20</StateTextPointSize>
  <StateTextAlignment type="integer">1</StateTextAlignment>
  <TargetElemID type="integer">DEVICE_ID</TargetElemID>
  <TargetElemSubKey type="string">temperatureInputsAll</TargetElemSubKey>
</PageElem>
```

### Motion Sensor (Display Only)

Shows motion state. No action on tap.

```xml
<PageElem type="dict">
  <ActionGroup type="dict">
    <ActionSteps type="vector">
    </ActionSteps>
    <ObjVers type="integer">2</ObjVers>
  </ActionGroup>
  <CaptionFontColor type="string">BF BF BF</CaptionFontColor>
  <CaptionFontType type="integer">22</CaptionFontType>
  <CaptionName type="string">Hall Motion</CaptionName>
  <CaptionPlacement type="integer">4</CaptionPlacement>
  <CaptionPointSize type="integer">20</CaptionPointSize>
  <ControlType type="integer">1</ControlType>
  <ID type="integer">ELEM_ID</ID>
  <ImageFileName type="string">Motion Sensor 2x</ImageFileName>
  <ObjVers type="integer">5</ObjVers>
  <Position type="string">77 260</Position>
  <ShowStateImage type="boolean">true</ShowStateImage>
  <ShowStateText type="boolean">true</ShowStateText>
  <Size type="string">76 76</Size>
  <StateTextFontColor type="string">DB DB DB</StateTextFontColor>
  <StateTextFontType type="integer">201</StateTextFontType>
  <StateTextPointSize type="integer">20</StateTextPointSize>
  <StateTextAlignment type="integer">1</StateTextAlignment>
  <TargetElemID type="integer">DEVICE_ID</TargetElemID>
  <TargetElemSubKey type="string">onOffState</TargetElemSubKey>
</PageElem>
```

### Action Group Button

Executes an Indigo action group when tapped.

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
  <CaptionFontColor type="string">BF BF BF</CaptionFontColor>
  <CaptionFontType type="integer">22</CaptionFontType>
  <CaptionName type="string">All Lights Off</CaptionName>
  <CaptionPlacement type="integer">4</CaptionPlacement>
  <CaptionPointSize type="integer">20</CaptionPointSize>
  <ControlType type="integer">100</ControlType>
  <ID type="integer">ELEM_ID</ID>
  <ImageFileName type="string">Light Button Solid Medium 2x</ImageFileName>
  <ObjVers type="integer">5</ObjVers>
  <Position type="string">150 400</Position>
  <ShowStateImage type="boolean">false</ShowStateImage>
  <ShowStateText type="boolean">false</ShowStateText>
  <Size type="string">76 38</Size>
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
        <DeviceID type="integer">DEVICE_ID</DeviceID>
        <ObjVers type="integer">14</ObjVers>
      </Action>
    </ActionSteps>
    <ObjVers type="integer">2</ObjVers>
  </ActionGroup>
  <CaptionFontColor type="string">BF BF BF</CaptionFontColor>
  <CaptionFontType type="integer">22</CaptionFontType>
  <CaptionName type="string">Power Switch</CaptionName>
  <CaptionPlacement type="integer">4</CaptionPlacement>
  <CaptionPointSize type="integer">20</CaptionPointSize>
  <ControlType type="integer">1</ControlType>
  <ID type="integer">ELEM_ID</ID>
  <ImageFileName type="string">Switch 2x</ImageFileName>
  <ObjVers type="integer">5</ObjVers>
  <Position type="string">77 170</Position>
  <ShowStateImage type="boolean">true</ShowStateImage>
  <ShowStateText type="boolean">false</ShowStateText>
  <Size type="string">76 76</Size>
  <TargetElemID type="integer">DEVICE_ID</TargetElemID>
  <TargetElemSubKey type="string">onOffState</TargetElemSubKey>
</PageElem>
```
