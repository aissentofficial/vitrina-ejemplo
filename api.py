"""
Módulo de ejemplo «Hola desde GitHub» (Vitrina, spec 016).
Cada función pública es una dirección: /api/<módulo>/saludar
"""


def saludar(datos):
    """Devuelve un saludo. Dato: nombre."""
    nombre = str(datos.get("nombre", "")).strip()
    if not nombre:
        raise ValueError("Escribe un nombre.")
    return {"mensaje": f"¡Hola, {nombre}! Te respondió el servidor, con código que vino de GitHub."}
