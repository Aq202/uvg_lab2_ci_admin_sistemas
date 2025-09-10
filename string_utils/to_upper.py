def to_upper(s) -> str:
  """Convierte la cadena a mayúsculas"""
  if not isinstance(s, (str)):
      raise TypeError(f"El valor '{s}' de tipo {type(s)} no es válido. Solo se permiten str.")
  return str(s).upper()