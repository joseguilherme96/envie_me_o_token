def notEmptyOrError(dados, atributo, message):
    if dados.get(f"{atributo}") == "":
        raise Exception({"message":message, "status_code":400})