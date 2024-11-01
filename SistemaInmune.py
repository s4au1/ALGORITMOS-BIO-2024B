import numpy as np
import random

# Función para generar detectores aleatorios
def generar_detector(longitud, rango=(0, 1)):
    return np.array([random.uniform(*rango) for _ in range(longitud)])

# Función para comprobar si un dato coincide con un detector
def comparar(dato, detector, umbral):
    distancia = np.linalg.norm(dato - detector)
    return distancia < umbral

# Genera detectores para representar patrones normales
def generar_detectores(num_detectores, longitud, umbral, datos_normales):
    detectores = []
    while len(detectores) < num_detectores:
        detector = generar_detector(longitud)
        # Agrega el detector solo si no coincide con ningún dato normal (selección negativa)
        if all(not comparar(dato, detector, umbral) for dato in datos_normales):
            detectores.append(detector)
    return np.array(detectores)

# Función de detección de anomalías
def detectar_anomalia(dato, detectores, umbral):
    return all(not comparar(dato, detector, umbral) for detector in detectores)

# Parámetros de ejemplo
longitud_dato = 5  # Longitud del vector de características
num_detectores = 10  # Número de detectores a generar
umbral = 0.5  # Umbral de distancia para coincidencia

# Datos normales de ejemplo
datos_normales = [np.random.rand(longitud_dato) for _ in range(100)]

# Generación de detectores
detectores = generar_detectores(num_detectores, longitud_dato, umbral, datos_normales)

# Dato nuevo para prueba
dato_prueba = np.random.rand(longitud_dato)

# Detección de anomalía
if detectar_anomalia(dato_prueba, detectores, umbral):
    print("Anomalía detectada")
else:
    print("Dato normal")
