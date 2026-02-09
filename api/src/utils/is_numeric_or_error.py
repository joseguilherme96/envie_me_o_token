def isNumericOrError(dados, atributo, message):
    try:
        int(dados.get(f"{atributo}"))
    except (ValueError, TypeError, AttributeError):
        raise Exception({"message": message, "status_code": 400})
