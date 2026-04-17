import time
from bot_instagram import publicar_post
from config import INTERVALO_MINUTOS

def iniciar_scheduler():
    intervalo = INTERVALO_MINUTOS * 60

    while True:
        try:
            print("🔄 Ejecutando tarea...")
            publicar_post()
        except Exception as e:
            print(f"❌ Error en scheduler: {e}")

        print(f"⏱️ Esperando {INTERVALO_MINUTOS} minutos...\n")
        time.sleep(intervalo)