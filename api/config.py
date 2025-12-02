
from dynaconf import Dynaconf
from pathlib import Path

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
    environments=True
)

