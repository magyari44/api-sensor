"""Sensor platform for ApiSensor."""
from homeassistant.helpers.entity import Entity
from integrationhelper import WebClient, Logger
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import ATTRIBUTION, DEFAULT_NAME, DOMAIN_DATA, ICON, DOMAIN, SENSOR_URL


async def async_setup_platform(
    hass, config, async_add_entities, discovery_info=None
):  # pylint: disable=unused-argument
    """Setup sensor platform."""
    logger = Logger(__name__)
    logger.info("async_setup_platform phase")
    webclient = WebClient(async_get_clientsession(hass), logger)
    async_add_entities([ApiSensor(hass, discovery_info, webclient)], True)


async def async_setup_entry(hass, config_entry, async_add_entities, async_add_devices):
    """Setup sensor platform."""
    logger = Logger(__name__)
    logger.info("async_setup_entry phase")



class ApiSensor(Entity):
    """ApiSensor Sensor class."""

    def __init__(self, hass, config, webclient):
        self.hass = hass
        self.attr = {}
        self._state = None
        self._name = config.get("name", DEFAULT_NAME)
        self.webclient = webclient

    async def async_update(self):
        """Update the sensor."""
        apisensor = await self.webclient.async_get_json(
            SENSOR_URL, {"Accept": "application/json"}
        )
        self._state = apisensor.msg

        # Send update "signal" to the component
        # await self.hass.data[DOMAIN_DATA]["client"].update_data()

        # Get new data (if any)
        # updated = self.hass.data[DOMAIN_DATA]["data"].get("data", {})

        # Check the data and update the value.
        # if updated.get("static") is None:
        #     self._state = self._state
        # else:
        #     self._state = updated.get("static")

        # Set/update attributes
        # self.attr["attribution"] = ATTRIBUTION
        # self.attr["time"] = str(updated.get("time"))
        # self.attr["none"] = updated.get("none")

    @property
    def unique_id(self):
        """
        Return a unique ID to use for this sensor.
        TODO unique id generator
        """
        return (
            "random unique id"
        )

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": self.name,
            "manufacturer": "ApiSensor",
        }

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self.attr
