[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE.md)

[![hacs][hacsbadge]](hacs)
![Project Maintenance][maintenance-shield]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

_Component to integrate with [ApiSensor][ApiSensor]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`binary_sensor` | Show something `True` or `False`.
`sensor` | Show info from ApiSensor API.
`switch` | Switch something `True` or `False`.

![example][exampleimg]

{% if not installed %}
## Installation

1. Click install.
1. Add `ApiSensor:` to your HA configuration.

{% endif %}
## Example configuration.yaml

```yaml
api-sensor:
  username: my_username
  password: my_password
  binary_sensor:
    - enabled: true
      name: My custom name
  sensor:
    - enabled: true
      name: My custom name
  switch:
    - enabled: true
      name: My custom name
```

## Configuration options

Key | Type | Required | Description
-- | -- | -- | --
`username` | `string` | `False` | Username for the client.
`password` | `string` | `False` | Password for the client.
`binary_sensor` | `list` | `False` | Configuration for the `binary_sensor` platform.
`sensor` | `list` | `False` | Configuration for the `sensor` platform.
`switch` | `list` | `False` | Configuration for the `switch` platform.

### Configuration options for `binary_sensor` list

Key | Type | Required | Default | Description
-- | -- | -- | -- | --
`enabled` | `boolean` | `False` | `True` | Boolean to enable/disable the platform.
`name` | `string` | `False` | `api-sensor` | Custom name for the entity.

### Configuration options for `sensor` list

Key | Type | Required | Default | Description
-- | -- | -- | -- | --
`enabled` | `boolean` | `False` | `True` | Boolean to enable/disable the platform.
`name` | `string` | `False` | `api-sensor` | Custom name for the entity.


### Configuration options for `switch` list

Key | Type | Required | Default | Description
-- | -- | -- | -- | --
`enabled` | `boolean` | `False` | `True` | Boolean to enable/disable the platform.
`name` | `string` | `False` | `api-sensor` | Custom name for the entity.