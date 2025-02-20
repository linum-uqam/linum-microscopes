import logging
from pathlib import Path

import tomli


def initialise_logging():
    logging.basicConfig(
        format=f"%(levelname)s - %(asctime)s [{Path(__file__).name}:%(lineno)s | %(funcName)s()] %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S")


class ConfigManager:
    default_config_file = Path(__file__).parent.parent.parent / "config.toml"
    config: dict

    def __init__(self, config_file):
        if config_file is None:
            config_file = self.default_config_file
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, mode="rb") as f:
            config = tomli.load(f)
        return config

    def get_config(self):
        return self.config

    def get_config_section(self, section):
        return self.config[section]

    def get_config_value(self, section, key):
        return self.config[section][key]

    def set_config_value(self, section, key, value):
        self.config[section][key] = value
