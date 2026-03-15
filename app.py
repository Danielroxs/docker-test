import time
import sys

print("--- Sistema Arkham iniciando ---", flush=True)
print("--- Cargando modelo IA: TARS ---", flush=True)

try:
    while True:
        print("Analizando datos de trafico para Circle K... [OK]", flush=True)
        time.sleep(3)
except KeyboardInterrupt:
    print("\nDeteniendo Sistema...")