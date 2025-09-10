def concat(a, b) -> str:
  """Concatena dos valores (str o número)"""
  if not isinstance(a, (str, int, float)):
      raise TypeError(f"El valor '{a}' de tipo {type(a)} no es válido. Solo se permiten str, int o float.")
  if not isinstance(b, (str, int, float)):
      raise TypeError(f"El valor '{b}' de tipo {type(b)} no es válido. Solo se permiten str, int o float.")
  return str(a) + str(b)