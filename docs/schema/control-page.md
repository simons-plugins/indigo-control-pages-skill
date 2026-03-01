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
| `Color` | string | Background color as space-separated hex pairs (e.g., `19 19 19` for dark) |
| `ID` | integer | Unique page ID. Generate with `python3 -c "import random; print(random.randint(100000000, 2147483647))"` |
| `ImageFileName` | string | Optional background image filename. Empty string for solid color |
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

## Background Images

Available from `Web Assets/images/backgrounds/`:

| Filename | Description |
|----------|-------------|
| `floorplan.png` | Floor plan background 1 |
| `floorplan2.png` | Floor plan background 2 |
| `floorplan3.png` | Floor plan background 3 |
| `indigo_logo.png` | Indigo logo |

Use empty string `""` for no background image (solid color only).

## Complete Example

A minimal control page with one light toggle:

```xml
<ControlPageList type="vector">
  <ControlPage type="dict">
    <Category type="integer">0</Category>
    <Color type="string">19 19 19</Color>
    <ID type="integer">1234567890</ID>
    <ImageFileName type="string"></ImageFileName>
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
              <DeviceID type="integer">123456789</DeviceID>
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
        <ControlType type="integer">1</ControlType>
        <ID type="integer">987654321</ID>
        <ImageFileName type="string">Dimmable Light 2x</ImageFileName>
        <ObjVers type="integer">5</ObjVers>
        <Position type="string">77 80</Position>
        <ShowStateImage type="boolean">true</ShowStateImage>
        <ShowStateText type="boolean">false</ShowStateText>
        <Size type="string">76 76</Size>
        <TargetElemID type="integer">123456789</TargetElemID>
        <TargetElemSubKey type="string">brightnessLevel</TargetElemSubKey>
      </PageElem>
    </PageElemList>
  </ControlPage>
</ControlPageList>
```
