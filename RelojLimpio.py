import time
from datetime import datetime
import os

try:
    while True:
        # Limpiar la pantalla (funciona en Windows y Linux)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Obtener la hora actual
        ahora = datetime.now().strftime("%H:%M:%S")
        
        # Imprimir la hora actual
        print(f"Hora actual: {ahora}", end="\r", flush=True)
        
        # Esperar 1 segundo antes de actualizar
        time.sleep(1)

except KeyboardInterrupt:
    print("\nReloj detenido.")