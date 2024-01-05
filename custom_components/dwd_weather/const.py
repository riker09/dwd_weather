"""Constants for the DWD Weather integration."""
from datetime import timedelta

from homeassistant.const import Platform

# Base component constants
NAME = "DWD Weather"
DOMAIN = "dwd_weather"
CONF_VERSION = 6
ATTRIBUTION = "Data provided by Deutscher Wetterdienst (DWD)"
# Platforms
PLATFORMS = [
    Platform.SENSOR,
    Platform.WEATHER,
]
INTEGRATION_VERSION = "2.0.9"
MIN_REQUIRED_HA_VERSION = "2022.7.1"

ATTR_LATEST_UPDATE = "latest_update_utc"
ATTR_REPORT_ISSUE_TIME = "report_time_utc"
ATTR_ISSUE_TIME = "forecast_time_utc"
ATTR_STATION_ID = "station_id"
ATTR_STATION_NAME = "station_name"

DEFAULT_SCAN_INTERVAL = timedelta(minutes=1)
DEFAULT_MAP_INTERVAL = timedelta(minutes=1)
DEFAULT_WIND_DIRECTION_TYPE = "degrees"
DEFAULT_INTERPOLATION = True

DWDWEATHER_DATA = "dwd_weather_data"
DWDWEATHER_COORDINATOR = "dwd_weather_coordinator"
DWDWEATHER_MONITORED_CONDITIONS = "dwd_weather_monitored_conditions"

CONF_ENTITY_TYPE = "entity_type"
CONF_ENTITY_TYPE_STATION = "weather_station"
CONF_ENTITY_TYPE_MAP = "weather_map"
CONF_STATION_ID = "station_id"
CONF_MAP_ID = "map_id"
CONF_CUSTOM_LOCATION = "custom_location"
CONF_LOCATION_COORDINATES = "location_type"
CONF_DATA_TYPE = "data_type"
CONF_DATA_TYPE_MIXED = "mixed_data"
CONF_DATA_TYPE_REPORT = "report_data"
CONF_DATA_TYPE_FORECAST = "forecast_data"
CONF_STATION_NAME = "station_name"
CONF_WIND_DIRECTION_TYPE = "wind_direction_type"
CONF_INTERPOLATE = "interpolate"
CONF_HOURLY_UPDATE = "hourly_update"
