"""Utility module for configuration parameters."""
from pathlib import Path
import tomli

default_config_file = Path(__file__).parent.parent / "config.toml"
with open(default_config_file, mode="rb") as f:
    config = tomli.load(f)