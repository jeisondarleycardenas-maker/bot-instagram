import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_ESTADO = os.path.join(BASE_DIR, "estado.json")

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