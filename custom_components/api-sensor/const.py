"""Constants for api-sensor."""
# Base component constants
from datetime import timedelta
DOMAIN = "api-sensor"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
PLATFORMS = [ "sensor"]
REQUIRED_FILES = [
    ".translations/en.json",
    "const.py",
    "config_flow.py",
    "manifest.json",
    "sensor.py",
]

SENSOR_URL = "http://192.168.2.173:5000/"
ISSUE_URL = "TODO"
ATTRIBUTION = "Data from this is provided by ApiSensor."
SCAN_INTERVAL = timedelta(seconds=10)

# Icons
ICON = "mdi:home-climate-outline"

# Configuration
CONF_SENSOR = "sensor"
CONF_ENABLED = "enabled"
CONF_NAME = "name"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN
