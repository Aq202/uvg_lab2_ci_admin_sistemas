def is_palindrome(s) -> bool:
    """Verifica si una cadena es palíndroma (ignora mayúsculas y espacios)"""
    if not isinstance(s, (str, int, float)):
        raise TypeError(f"El valor '{s}' de tipo {type(s)} no es válido. Solo se permiten str, int o float.")
    cleaned = ''.join(c.lower() for c in str(s) if c.isalnum())
    return cleaned == cleaned[::-1]