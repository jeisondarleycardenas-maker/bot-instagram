import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
INTERVALO_MINUTOS = int(os.getenv("INTERVAL_MINUTES", 60))