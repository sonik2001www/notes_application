from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    user: str
    password: str
    host: str
    name: str


@dataclass
class SettingsConfig:
    secret_key: str
    debug: bool
    client_id: str
    secret: str
    email_host_user: str
    email_host_password: str


@dataclass
class Config:
    settings_config: SettingsConfig
    db_config: DatabaseConfig
