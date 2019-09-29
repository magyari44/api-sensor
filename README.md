# Notice

This was created from the custom_components blueprint.
https://github.com/custom-components/blueprint

***
README content if this was a published component:
***

# api-sensor

[![License][license-shield]](LICENSE.md)

[![hacs][hacsbadge]][hacs]


_Component to integrate with [api-sensor][api-sensor]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show info from Api-sensor API.

![example][exampleimg]

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `api-sensor`.
4. Download _all_ the files from the `custom_components/api-sensor/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. Choose:
   - Add `api-sensor:` to your HA configuration.
   - In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Api-sensor"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/api-sensor/.translations/en.json
custom_components/api-sensor/.translations/nb.json
custom_components/api-sensor/.translations/sensor.nb.json
custom_components/api-sensor/__init__.py
custom_components/api-sensor/config_flow.py
custom_components/api-sensor/const.py
custom_components/api-sensor/manifest.json
custom_components/api-sensor/sensor.py
```

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
`sensor` | `list` | `False` | Configuration for the `sensor` platform.

### Configuration options for `sensor` list

Key | Type | Required | Default | Description
-- | -- | -- | -- | --
`enabled` | `boolean` | `False` | `True` | Boolean to enable/disable the platform.
`name` | `string` | `False` | `api-sensor` | Custom name for the entity.


## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***
