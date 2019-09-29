[![License][license-shield]](LICENSE.md)

[![hacs][hacsbadge]](hacs)
![Project Maintenance][maintenance-shield]

_Component to integrate with [ApiSensor][ApiSensor]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show info from ApiSensor API.

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
  sensor:
    - enabled: true
      name: My custom name
```

## Configuration options

Key | Type | Required | Description
-- | -- | -- | --
`username` | `string` | `False` | Username for the client.
`password` | `string` | `False` | Password for the client.
`sensor` | `list` | `False` | Configuration for the `sensor` platform.

### Configuration options for `sensor` list

Key | Type | Required | Default | Description
-- | -- | -- | -- | --
`enabled` | `boolean` | `False` | `True` | Boolean to enable/disable the platform.
`name` | `string` | `False` | `api-sensor` | Custom name for the entity.
