import os
from datetime import datetime
from state_manager import obtener_publicados

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_PRINCIPAL = os.path.join(BASE_DIR, "contenido")


def obtener_dia_actual():
    dias = {
        0: "lunes",
        1: "martes",
        2: "miercoles",
        3: "jueves",
        4: "viernes",
        5: "sabado",
        6: "domingo"
    }
    return dias[datetime.now().weekday()]


def obtener_siguiente_post():
    if not os.path.exists(CARPETA_PRINCIPAL):
        print("❌ La carpeta 'contenido' no existe")
        return None

    dia_actual = obtener_dia_actual()
    carpeta_dia = os.path.join(CARPETA_PRINCIPAL, dia_actual)

    print(f"📅 Día actual detectado: {dia_actual}")

    if not os.path.exists(carpeta_dia):
        print(f"❌ No existe la carpeta del día: {carpeta_dia}")
        return None

    archivos = os.listdir(carpeta_dia)
    print(f"📂 Archivos encontrados en '{dia_actual}':", archivos)

    imagenes = [
        f for f in archivos
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]
    print(f"🖼️ Imágenes válidas en '{dia_actual}':", imagenes)

    if not imagenes:
        print(f"⚠️ No hay imágenes válidas en la carpeta '{dia_actual}'")
        return None

    publicados = obtener_publicados()
    print("✅ Ya publicadas:", publicados)

    for img in imagenes:
        identificador = f"{dia_actual}/{img}"

        if identificador not in publicados:
            ruta_imagen = os.path.join(carpeta_dia, img)

            nombre_base = os.path.splitext(img)[0]
            ruta_txt = os.path.join(carpeta_dia, f"{nombre_base}.txt")

            print("🔎 Buscando caption en:", ruta_txt)

            if os.path.exists(ruta_txt):
                print("✅ Archivo de texto encontrado")
                with open(ruta_txt, "r", encoding="utf-8") as archivo:
                    caption = archivo.read().strip()
            else:
                print("⚠️ No se encontró archivo .txt para esta imagen")
                caption = f"Publicación automática: {img}"

            return ruta_imagen, caption, identificador

    print(f"⚠️ Todas las imágenes de '{dia_actual}' ya fueron publicadas")
    return None