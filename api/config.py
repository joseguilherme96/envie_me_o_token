
from dynaconf import Dynaconf
from pathlib import Path

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['api/settings.toml', 'api/.secrets.toml'],
    environments=True,
    
)

