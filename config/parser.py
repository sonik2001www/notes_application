import configparser
import os
from functools import lru_cache

from config.models import Config, SettingsConfig, DatabaseConfig


@lru_cache
def load_config(path: str = None):
    if path is None:
        path = os.getenv("CONFIG_PATH", "secure.ini")

    parser = configparser.ConfigParser()
    parser.read(path)

    settings_data = parser["settings"]
    db_data = parser["database"]

    db_config = DatabaseConfig(
        user=db_data.get("db_user"),
        name=db_data.get("db_name"),
        host=db_data.get("db_host"),
        password=db_data.get("db_pass"),
    )

    settings_config = SettingsConfig(
        secret_key=settings_data.get("secret_key"),
        debug=settings_data.get("debug"),
        client_id=settings_data.get("client_id"),
        secret=settings_data.get("secret"),
        email_host_user=settings_data.get("email_host_user"),
        email_host_password=settings_data.get("email_host_password"),
    )

    return Config(
        settings_config=settings_config,
        db_config=db_config,
    )
