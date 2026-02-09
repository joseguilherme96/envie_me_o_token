from dynaconf import Dynaconf
import os

environment = os.getenv("ENV_FOR_DYNACONF", None)

if environment is None:
    os.environ["ENV_FOR_DYNACONF"] = "development"

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["api/settings.toml", "api/.secrets.toml"],
    environments=True,
)
