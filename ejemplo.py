from pathlib import Path
import json
from datetime import datetime

# 🔥 RUTA BASE FIJA (TU PROYECTO)
ROOT_DIR = Path(r"C:\Users\jeiso\OneDrive\Desktop\instagram")

BASE_DIR = ROOT_DIR / "contenido"
STATE_FILE = ROOT_DIR / "estado.json"

DAY_MAP = {
    "monday": "lunes",
    "tuesday": "martes",
    "wednesday": "miercoles",
    "thursday": "jueves",
    "friday": "viernes",
    "saturday": "sabado",
    "sunday": "domingo",
}

def load_state():
    if not STATE_FILE.exists():
        state = {day: 0 for day in DAY_MAP.values()}
        STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
        return state
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))

def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")

def get_today_folder():
    english_day = datetime.now().strftime("%A").lower()
    return DAY_MAP.get(english_day)

def get_next_content(day_folder, state):
    folder = BASE_DIR / day_folder

    print(f"📂 Carpeta usada: {folder}")

    if not folder.exists():
        raise FileNotFoundError(f"No existe la carpeta: {folder}")

    current_index = state[day_folder] + 1

    image_file = folder / f"{current_index}.jpg"
    text_file = folder / f"{current_index}.txt"

    print(f"🔍 Buscando imagen: {image_file}")
    print(f"🔍 Buscando texto: {text_file}")

    print("¿Existe imagen?", image_file.exists())
    print("¿Existe texto?", text_file.exists())

    if not image_file.exists() or not text_file.exists():
        return None, None, current_index

    caption = text_file.read_text(encoding="utf-8").strip()
    return image_file, caption, current_index

def main():
    day_folder = get_today_folder()
    state = load_state()

    image_file, caption, index = get_next_content(day_folder, state)

    if image_file is None:
        print(f"No hay más contenido para publicar en {day_folder}. Reiniciando desde 1...")

        state[day_folder] = 0
        save_state(state)

        image_file, caption, index = get_next_content(day_folder, state)

        if image_file is None:
            print(f"❌ La carpeta {day_folder} está vacía o mal configurada.")
            return

    print("\n✅ Contenido seleccionado:")
    print(f"Día: {day_folder}")
    print(f"Imagen: {image_file}")
    print(f"Texto: {caption}")

    state[day_folder] = index
    save_state(state)

    print("💾 Estado actualizado correctamente.")

if __name__ == "__main__":
    main()