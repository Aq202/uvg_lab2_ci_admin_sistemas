def count_vowels(s) -> int:
  """Cuenta el total de vocales en la cadena"""
  if not isinstance(s, (str, int, float)):
      raise TypeError(f"El valor '{s}' de tipo {type(s)} no es válido. Solo se permiten str, int o float.")
  vowels = "aeiou"
  return sum(1 for char in str(s).lower() if char in vowels)