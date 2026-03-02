# ActionGroup and Action Classes

How actions work in Control Page elements.

## ActionGroup Structure

Every `<PageElem>` contains an `<ActionGroup>` that defines what happens when the element is tapped.

```xml
<ActionGroup type="dict">
  <ActionSteps type="vector">
    <Action type="dict">
      <Class type="integer">CLASS_NUM</Class>
      <ObjVers type="integer">14</ObjVers>
      <!-- class-specific properties -->
    </Action>
  </ActionSteps>
  <ObjVers type="integer">2</ObjVers>
</ActionGroup>
```

### Empty ActionGroup (Display Only)

For elements that show state but have no tap action:

```xml
<ActionGroup type="dict">
  <ActionSteps type="vector">
  </ActionSteps>
  <ObjVers type="integer">2</ObjVers>
</ActionGroup>
```

### Multiple Actions

An ActionGroup can contain multiple Action steps that execute in sequence:

```xml
<ActionGroup type="dict">
  <ActionSteps type="vector">
    <Action type="dict">
      <Class type="integer">1</Class>
      <DeviceAction type="integer">4</DeviceAction>
      <DeviceID type="integer">111111111</DeviceID>
      <ObjVers type="integer">14</ObjVers>
    </Action>
    <Action type="dict">
      <Class type="integer">1</Class>
      <DeviceAction type="integer">4</DeviceAction>
      <DeviceID type="integer">222222222</DeviceID>
      <ObjVers type="integer">14</ObjVers>
    </Action>
  </ActionSteps>
  <ObjVers type="integer">2</ObjVers>
</ActionGroup>
```

---

## Action Classes

### Class 1: Device Control

Controls a device (on/off/toggle, set brightness, etc.).

```xml
<Action type="dict">
  <Class type="integer">1</Class>
  <DeviceAction type="integer">6</DeviceAction>
  <DeviceID type="integer">DEVICE_ID</DeviceID>
  <ObjVers type="integer">14</ObjVers>
</Action>
```

| Property | Type | Description |
|----------|------|-------------|
| `DeviceID` | integer | Target device ID |
| `DeviceAction` | integer | 4 = turn on, 5 = turn off, 6 = toggle |
| `DeviceActionValue` | integer | Optional. Brightness value (0-100) for "set brightness" action |

**Toggle** (most common for buttons):
```xml
<DeviceAction type="integer">6</DeviceAction>
```

**Set brightness to specific level**:
```xml
<DeviceAction type="integer">4</DeviceAction>
<DeviceActionValue type="integer">75</DeviceActionValue>
```

### Class 2: Sprinkler Control

Controls sprinkler devices.

```xml
<Action type="dict">
  <Class type="integer">2</Class>
  <DeviceID type="integer">DEVICE_ID</DeviceID>
  <ObjVers type="integer">14</ObjVers>
  <SprinklerAction type="integer">ACTION</SprinklerAction>
</Action>
```

| Property | Type | Description |
|----------|------|-------------|
| `DeviceID` | integer | Sprinkler device ID |
| `SprinklerAction` | integer | Sprinkler-specific action |
| `SprinklerZones` | string | Optional. Zone specification |

### Class 3: Thermostat Control

Controls thermostat devices. Verified against working Heating .textClipping export.

```xml
<Action type="dict">
  <Class type="integer">3</Class>
  <DeviceID type="integer">1351833195</DeviceID>
  <HVACAction type="integer">7</HVACAction>
  <ObjVers type="integer">14</ObjVers>
</Action>
```

| Property | Type | Description |
|----------|------|-------------|
| `DeviceID` | integer | Thermostat device ID |
| `HVACAction` | integer | HVAC action type. `7` observed in working examples |
| `HVACActionValue` | string | Optional. Temperature or mode value |

### Class 7: Speed Control

Controls speed control devices (fans).

```xml
<Action type="dict">
  <Class type="integer">7</Class>
  <DeviceID type="integer">DEVICE_ID</DeviceID>
  <ObjVers type="integer">14</ObjVers>
  <SpeedControlAction type="integer">ACTION</SpeedControlAction>
</Action>
```

| Property | Type | Description |
|----------|------|-------------|
| `DeviceID` | integer | Speed control device ID |
| `SpeedControlAction` | integer | Speed control action |
| `SpeedControlActionValue` | integer | Optional. Speed level |

### Class 100: Execute Action Group

Executes a predefined Indigo action group.

```xml
<Action type="dict">
  <ActionGroupID type="integer">ACTION_GROUP_ID</ActionGroupID>
  <Class type="integer">100</Class>
  <ObjVers type="integer">14</ObjVers>
</Action>
```

| Property | Type | Description |
|----------|------|-------------|
| `ActionGroupID` | integer | ID of the action group to execute |

### Class 200: Enable/Disable

Enables or disables a device, trigger, schedule, or action group.

```xml
<Action type="dict">
  <Class type="integer">200</Class>
  <DoEnable type="boolean">true</DoEnable>
  <ObjVers type="integer">14</ObjVers>
  <TargetID type="integer">TARGET_ID</TargetID>
  <TargetType type="integer">TARGET_TYPE</TargetType>
</Action>
```

| Property | Type | Description |
|----------|------|-------------|
| `TargetID` | integer | ID of the target to enable/disable |
| `TargetType` | integer | Type of target (device, trigger, schedule, etc.) |
| `DoEnable` | boolean | `true` to enable, `false` to disable |

### Class 201: Variable

Sets or modifies an Indigo variable.

```xml
<Action type="dict">
  <Class type="integer">201</Class>
  <ObjVers type="integer">14</ObjVers>
  <VarAction type="integer">ACTION</VarAction>
  <VarID type="integer">VARIABLE_ID</VarID>
  <VarValue type="string">VALUE</VarValue>
</Action>
```

| Property | Type | Description |
|----------|------|-------------|
| `VarID` | integer | Variable ID |
| `VarValue` | string | Value to set |
| `VarAction` | integer | Variable action type |

### Class 999: Plugin Action

Executes a plugin-defined action. Verified against working Sonos .textClipping export.

```xml
<Action type="dict">
  <Class type="integer">999</Class>
  <DeviceID type="integer">494584985</DeviceID>
  <ObjVers type="integer">14</ObjVers>
  <PluginID type="string">com.ssi.indigoplugin.Sonos</PluginID>
  <TypeIdPlugin type="string">actionTogglePlay</TypeIdPlugin>
  <TypeLabelPlugin type="string">Sonos: Toggle Play</TypeLabelPlugin>
</Action>
```

| Property | Type | Description |
|----------|------|-------------|
| `DeviceID` | integer | Target device ID |
| `PluginID` | string | Plugin bundle identifier (e.g., `com.ssi.indigoplugin.Sonos`) |
| `TypeIdPlugin` | string | Plugin action type ID (e.g., `actionTogglePlay`, `actionStop`, `actionNext`, `actionPrevious`, `actionVolumeUp`, `actionVolumeDown`) |
| `TypeLabelPlugin` | string | Human-readable action label (e.g., `Sonos: Toggle Play`) |
| `MetaProps` | dict | Optional. Plugin-specific action properties |

---

## Common Patterns

### Toggle Button (Most Common)

```xml
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
```

### Display Only (Sensor, Status)

```xml
<ActionGroup type="dict">
  <ActionSteps type="vector">
  </ActionSteps>
  <ObjVers type="integer">2</ObjVers>
</ActionGroup>
```

### Popup Control Dialog

Add `ClientActionType` to the PageElem (not inside ActionGroup):

```xml
<ClientActionType type="integer">1014</ClientActionType>
```

This opens Indigo's built-in control popup when the element is tapped, allowing brightness sliders, thermostat controls, etc. The popup content depends on the device type.
