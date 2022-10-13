from typing import TypedDict

from config42 import ConfigManager
from config42.handlers import FileHandler


class ConfigData(TypedDict):
    openweather_api_key: str


CONFIG: ConfigData = ConfigManager(handler=FileHandler, path="config.json").as_dict()
