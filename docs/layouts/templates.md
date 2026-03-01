# Layout Templates

Pre-built templates for common control page layouts. Each includes an ASCII wireframe, element positions, and complete XML.

Use placeholder `DEVICE_ID_N` values — the workflow replaces these with real device IDs.

---

## Template 1: Basic Room

Simple 2-4 light grid with optional thermostat. iPhone sized.

### Wireframe

```
+--------- Basic Room (375x667) ---------+
|                                         |
|            "Bedroom"                    |
|                                         |
|    [light-bulb]      [light-bulb]      |
|    Ceiling Light      Bedside Lamp     |
|                                         |
|    [light-bulb]      [thermometer]     |
|    Floor Lamp         Thermostat       |
|                       "72°F"           |
|                                         |
+-----------------------------------------+
```

### Element Positions (iPhone 375px, 2-column)

| Element | Position | Size | Image |
|---------|----------|------|-------|
| Title "Bedroom" | 37 20 | 300 30 | — |
| Ceiling Light | 65 70 | 76 76 | `Dimmable Light 2x` |
| Bedside Lamp | 232 70 | 76 76 | `Dimmable Light 2x` |
| Floor Lamp | 65 160 | 76 76 | `Dimmable Light 2x` |
| Thermostat | 232 160 | 76 76 | `Temperature Sensor 2x` |

### XML

```xml
<ControlPageList type="vector">
  <ControlPage type="dict">
    <Category type="integer">0</Category>
    <Color type="string">19 19 19</Color>
    <ID type="integer">PAGE_ID</ID>
    <ImageFileName type="string"></ImageFileName>
    <Name type="string">Bedroom</Name>
    <ObjVers type="integer">5</ObjVers>
    <Size type="string">375 667</Size>
    <PageElemList type="vector">
      <!-- Title -->
      <PageElem type="dict">
        <ActionGroup type="dict"><ActionSteps type="vector"></ActionSteps><ObjVers type="integer">2</ObjVers></ActionGroup>
        <CaptionFontColor type="string">FF FF FF</CaptionFontColor>
        <CaptionFontType type="integer">22</CaptionFontType>
        <CaptionName type="string">Bedroom</CaptionName>
        <CaptionPlacement type="integer">5</CaptionPlacement>
        <CaptionPointSize type="integer">22</CaptionPointSize>
        <CaptionWraps type="boolean">true</CaptionWraps>
        <CaptionCurWidth type="integer">300</CaptionCurWidth>
        <CaptionCurHeight type="integer">30</CaptionCurHeight>
        <ControlType type="integer">100</ControlType>
        <ID type="integer">ELEM_ID_1</ID>
        <ImageFileName type="string"></ImageFileName>
        <ObjVers type="integer">5</ObjVers>
        <Position type="string">37 20</Position>
        <ShowStateImage type="boolean">false</ShowStateImage>
        <ShowStateText type="boolean">false</ShowStateText>
        <Size type="string">300 30</Size>
      </PageElem>
      <!-- Ceiling Light -->
      <PageElem type="dict">
        <ActionGroup type="dict"><ActionSteps type="vector"><Action type="dict"><Class type="integer">1</Class><DeviceAction type="integer">6</DeviceAction><DeviceID type="integer">DEVICE_ID_1</DeviceID><ObjVers type="integer">14</ObjVers></Action></ActionSteps><ObjVers type="integer">2</ObjVers></ActionGroup>
        <CaptionFontColor type="string">BF BF BF</CaptionFontColor>
        <CaptionFontType type="integer">22</CaptionFontType>
        <CaptionName type="string">Ceiling Light</CaptionName>
        <CaptionPlacement type="integer">4</CaptionPlacement>
        <CaptionPointSize type="integer">20</CaptionPointSize>
        <ClientActionType type="integer">1014</ClientActionType>
        <ControlType type="integer">1</ControlType>
        <ID type="integer">ELEM_ID_2</ID>
        <ImageFileName type="string">Dimmable Light 2x</ImageFileName>
        <ObjVers type="integer">5</ObjVers>
        <Position type="string">65 70</Position>
        <ShowStateImage type="boolean">true</ShowStateImage>
        <ShowStateText type="boolean">false</ShowStateText>
        <Size type="string">76 76</Size>
        <TargetElemID type="integer">DEVICE_ID_1</TargetElemID>
        <TargetElemSubKey type="string">brightnessLevel</TargetElemSubKey>
      </PageElem>
      <!-- Bedside Lamp -->
      <PageElem type="dict">
        <ActionGroup type="dict"><ActionSteps type="vector"><Action type="dict"><Class type="integer">1</Class><DeviceAction type="integer">6</DeviceAction><DeviceID type="integer">DEVICE_ID_2</DeviceID><ObjVers type="integer">14</ObjVers></Action></ActionSteps><ObjVers type="integer">2</ObjVers></ActionGroup>
        <CaptionFontColor type="string">BF BF BF</CaptionFontColor>
        <CaptionFontType type="integer">22</CaptionFontType>
        <CaptionName type="string">Bedside Lamp</CaptionName>
        <CaptionPlacement type="integer">4</CaptionPlacement>
        <CaptionPointSize type="integer">20</CaptionPointSize>
        <ClientActionType type="integer">1014</ClientActionType>
        <ControlType type="integer">1</ControlType>
        <ID type="integer">ELEM_ID_3</ID>
        <ImageFileName type="string">Dimmable Light 2x</ImageFileName>
        <ObjVers type="integer">5</ObjVers>
        <Position type="string">232 70</Position>
        <ShowStateImage type="boolean">true</ShowStateImage>
        <ShowStateText type="boolean">false</ShowStateText>
        <Size type="string">76 76</Size>
        <TargetElemID type="integer">DEVICE_ID_2</TargetElemID>
        <TargetElemSubKey type="string">brightnessLevel</TargetElemSubKey>
      </PageElem>
      <!-- Floor Lamp -->
      <PageElem type="dict">
        <ActionGroup type="dict"><ActionSteps type="vector"><Action type="dict"><Class type="integer">1</Class><DeviceAction type="integer">6</DeviceAction><DeviceID type="integer">DEVICE_ID_3</DeviceID><ObjVers type="integer">14</ObjVers></Action></ActionSteps><ObjVers type="integer">2</ObjVers></ActionGroup>
        <CaptionFontColor type="string">BF BF BF</CaptionFontColor>
        <CaptionFontType type="integer">22</CaptionFontType>
        <CaptionName type="string">Floor Lamp</CaptionName>
        <CaptionPlacement type="integer">4</CaptionPlacement>
        <CaptionPointSize type="integer">20</CaptionPointSize>
        <ClientActionType type="integer">1014</ClientActionType>
        <ControlType type="integer">1</ControlType>
        <ID type="integer">ELEM_ID_4</ID>
        <ImageFileName type="string">Dimmable Light 2x</ImageFileName>
        <ObjVers type="integer">5</ObjVers>
        <Position type="string">65 160</Position>
        <ShowStateImage type="boolean">true</ShowStateImage>
        <ShowStateText type="boolean">false</ShowStateText>
        <Size type="string">76 76</Size>
        <TargetElemID type="integer">DEVICE_ID_3</TargetElemID>
        <TargetElemSubKey type="string">brightnessLevel</TargetElemSubKey>
      </PageElem>
      <!-- Thermostat -->
      <PageElem type="dict">
        <ActionGroup type="dict"><ActionSteps type="vector"></ActionSteps><ObjVers type="integer">2</ObjVers></ActionGroup>
        <CaptionFontColor type="string">BF BF BF</CaptionFontColor>
        <CaptionFontType type="integer">22</CaptionFontType>
        <CaptionName type="string">Thermostat</CaptionName>
        <CaptionPlacement type="integer">4</CaptionPlacement>
        <CaptionPointSize type="integer">20</CaptionPointSize>
        <ClientActionType type="integer">1014</ClientActionType>
        <ControlType type="integer">1</ControlType>
        <ID type="integer">ELEM_ID_5</ID>
        <ImageFileName type="string">Temperature Sensor 2x</ImageFileName>
        <ObjVers type="integer">5</ObjVers>
        <Position type="string">232 160</Position>
        <ShowStateImage type="boolean">true</ShowStateImage>
        <ShowStateText type="boolean">true</ShowStateText>
        <Size type="string">76 76</Size>
        <StateTextFontColor type="string">DB DB DB</StateTextFontColor>
        <StateTextFontType type="integer">201</StateTextFontType>
        <StateTextPointSize type="integer">20</StateTextPointSize>
        <StateTextAlignment type="integer">1</StateTextAlignment>
        <TargetElemID type="integer">DEVICE_ID_4</TargetElemID>
        <TargetElemSubKey type="string">temperatureInputsAll</TargetElemSubKey>
      </PageElem>
    </PageElemList>
  </ControlPage>
</ControlPageList>
```

---

## Template 2: Living Room

Lights section, climate section, media section. iPhone sized.

### Wireframe

```
+-------- Living Room (375x667) ---------+
|                                         |
|            "Living Room"                |
|                                         |
|    [light-bulb]      [light-bulb]      |
|    Ceiling Light      Floor Lamp       |
|                                         |
|    [light-bulb]      [fan]             |
|    Table Lamp         Ceiling Fan      |
|                                         |
|    [thermometer]     [humidity]        |
|    Thermostat         Humidity         |
|    "72°F"            "45%"             |
|                                         |
|    [motion]                            |
|    Motion Sensor                        |
|                                         |
+-----------------------------------------+
```

### Element Positions

| Element | Position | Image |
|---------|----------|-------|
| Title | 37 20 | — |
| Ceiling Light | 65 70 | `Dimmable Light 2x` |
| Floor Lamp | 232 70 | `floorlamp_large` |
| Table Lamp | 65 160 | `lightbulb_large` |
| Ceiling Fan | 232 160 | `Fan 2x` |
| Thermostat | 65 250 | `Temperature Sensor 2x` |
| Humidity | 232 250 | `Humidity Sensor 2x` |
| Motion Sensor | 65 340 | `Motion Sensor 2x` |

---

## Template 3: Security

Alarm status, door/motion sensors, arm/disarm buttons. iPhone sized.

### Wireframe

```
+---------- Security (375x667) ----------+
|                                         |
|            "Security"                   |
|                                         |
|    [dot]             [dot]             |
|    Front Door         Back Door        |
|                                         |
|    [motion]          [motion]          |
|    Living Room        Hallway          |
|                                         |
|    [dot]             [dot]             |
|    Garage Door        Side Gate        |
|                                         |
|    [button]          [button]          |
|    Arm Away           Arm Home         |
|                                         |
+-----------------------------------------+
```

### Element Positions

| Element | Position | Image |
|---------|----------|-------|
| Title | 37 20 | — |
| Front Door | 65 70 | `Green Dot 2x` |
| Back Door | 232 70 | `Green Dot 2x` |
| Living Room Motion | 65 160 | `Motion Sensor 2x` |
| Hallway Motion | 232 160 | `Motion Sensor 2x` |
| Garage Door | 65 250 | `Green Dot 2x` |
| Side Gate | 232 250 | `Green Dot 2x` |
| Arm Away Button | 65 340 | `Light Button Solid Medium 2x` |
| Arm Home Button | 232 340 | `Light Button Solid Medium 2x` |

---

## Template 4: Climate Dashboard

Multiple thermostat readouts. iPad Portrait sized (3 columns).

### Wireframe

```
+------------ Climate (768x1024) ------------+
|                                             |
|              "Climate Control"              |
|                                             |
|  [thermometer]  [thermometer]  [thermometer]|
|  Living Room     Bedroom        Kitchen     |
|  "72°F"         "68°F"         "70°F"       |
|                                             |
|  [thermometer]  [humidity]     [humidity]   |
|  Guest Room      Living Room    Bedroom     |
|  "65°F"         "45%"          "50%"        |
|                                             |
|  [thermostat-mode]                          |
|  HVAC Mode                                  |
|                                             |
+---------------------------------------------+
```

### Element Positions (iPad Portrait 768px, 3-column)

| Element | Position | Image |
|---------|----------|-------|
| Title | 234 20 | — |
| Living Room Temp | 103 70 | `Temperature Sensor 2x` |
| Bedroom Temp | 345 70 | `Temperature Sensor 2x` |
| Kitchen Temp | 587 70 | `Temperature Sensor 2x` |
| Guest Room Temp | 103 160 | `Temperature Sensor 2x` |
| Living Room Humidity | 345 160 | `Humidity Sensor 2x` |
| Bedroom Humidity | 587 160 | `Humidity Sensor 2x` |
| HVAC Mode | 103 250 | `Light Thermostat Mode Control 2x` |

---

## Template 5: Outdoor

Garden lights, sprinklers, motion sensors. iPhone sized.

### Wireframe

```
+---------- Outdoor (375x667) -----------+
|                                         |
|            "Outdoor"                    |
|                                         |
|    [light-bulb]      [light-bulb]      |
|    Porch Light        Path Lights      |
|                                         |
|    [light-bulb]      [motion]          |
|    Garden Spots       Driveway         |
|                                         |
|    [sprinkler]       [sprinkler]       |
|    Front Lawn         Back Garden      |
|                                         |
|    [button]                            |
|    All Lights Off                       |
|                                         |
+-----------------------------------------+
```

### Element Positions

| Element | Position | Image |
|---------|----------|-------|
| Title | 37 20 | — |
| Porch Light | 65 70 | `lantern_large` |
| Path Lights | 232 70 | `pathwaylight_large` |
| Garden Spots | 65 160 | `floodlight_large` |
| Driveway Motion | 232 160 | `Motion Sensor 2x` |
| Front Lawn Sprinkler | 65 250 | `Sprinkler 2x` |
| Back Garden Sprinkler | 232 250 | `Sprinkler 2x` |
| All Lights Off | 150 340 | `Light Button Solid Medium 2x` |

The "All Lights Off" button uses an ActionGroup with Class 100 (execute action group) pointing to an Indigo action group that turns off all outdoor lights.
