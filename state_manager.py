import json
import os

ARCHIVO_ESTADO = "estado.json"

def obtener_publicados():
    if not os.path.exists(ARCHIVO_ESTADO):
        return []

    with open(ARCHIVO_ESTADO, "r") as f:
        data = json.load(f)
        return data.get("publicados", [])

def marcar_como_publicado(imagen):
    data = {"publicados": []}

    if os.path.exists(ARCHIVO_ESTADO):
        with open(ARCHIVO_ESTADO, "r") as f:
            data = json.load(f)

    data["publicados"].append(imagen)

    with open(ARCHIVO_ESTADO, "w") as f:
        json.dump(data, f, indent=2)