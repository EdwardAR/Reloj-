"Reloj que se actualiza cada segundo en consola"

import time
from datetime import datetime

while True:
    ahora = datetime.now().strftime("%H:%M:%S")
    print(f"\rHora actual: {ahora}",end="")
    time.sleep(1)
    