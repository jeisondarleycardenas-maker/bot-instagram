from config import USERNAME
from content_manager import obtener_siguiente_post
from state_manager import marcar_como_publicado


def publicar_post():
    print(f"👤 Usuario: {USERNAME}")

    post = obtener_siguiente_post()

    if not post:
        print("⚠️ No hay contenido disponible\n")
        return

    ruta_imagen, caption, identificador = post

    print(f"📸 Publicando imagen: {ruta_imagen}")
    print("📝 Caption:")
    print(caption)

    # Aquí luego va la publicación real en Instagram
    print("✅ Publicado correctamente\n")

    marcar_como_publicado(identificador)