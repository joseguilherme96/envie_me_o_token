import logging
import os


def test_deve_carregar_variaveis_ambiente_dynaconf(tmp_path, caplog, mocker):

    caplog.set_level(level="INFO")
    file_path = tmp_path / "settings.toml"

    with open(file_path, "w+") as file:
        variables = '''[default]\nTESTE="TESTE"\nTESTE2="TESTE2"'''
        file.write(variables)

    logging.info(str(file_path))
    mocker.patch.dict(
        os.environ,
        {
            "SETTINGS_FILE_FOR_DYNACONF": str(file_path),
            "ENV_FOR_DYNACONF": "default",
        },
        clear=True,
    )

    from dynaconf import Dynaconf

    settings = Dynaconf(environments=True)

    assert settings.TESTE == "TESTE"
    assert settings.TESTE2 == "TESTE2"
