def limpiar_texto(texto: str) -> str:
    """Elimina espacios en blanco y lo pasa a
    minúsculas."""

    return texto.replace(" ", "").lower()
