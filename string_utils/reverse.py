def reverse(s) -> str:
    """Retorna la cadena en orden inverso"""
    if not isinstance(s, (str, int, float)):
        raise TypeError(f"El valor '{s}' de tipo {type(s)} no es válido. Solo se permiten str, int o float.")
    return str(s)[::-1]