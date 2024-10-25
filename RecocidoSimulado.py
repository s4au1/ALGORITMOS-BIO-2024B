import math
import random

# Función objetivo (puede cambiarse según el problema)
def objetivo(x):
    return x**2  # Queremos minimizar la función cuadrática

# Función de aceptación de un nuevo estado
def probabilidad_aceptacion(energia_actual, energia_nueva, temperatura):
    if energia_nueva < energia_actual:
        return 1.0
    else:
        return math.exp((energia_actual - energia_nueva) / temperatura)

# Algoritmo de recocido simulado
def recocido_simulado(temperatura_inicial, tasa_enfriamiento, iteraciones):
    # Generar una solución inicial aleatoria
    solucion_actual = random.uniform(-10, 10)
    energia_actual = objetivo(solucion_actual)
    
    mejor_solucion = solucion_actual
    mejor_energia = energia_actual

    temperatura = temperatura_inicial

    for i in range(iteraciones):
        # Generar un vecino (solución candidata)
        nuevo_vecino = solucion_actual + random.uniform(-1, 1)
        energia_nueva = objetivo(nuevo_vecino)

        # Decidir si aceptamos el nuevo estado
        if probabilidad_aceptacion(energia_actual, energia_nueva, temperatura) > random.random():
            solucion_actual = nuevo_vecino
            energia_actual = energia_nueva

        # Actualizar la mejor solución encontrada
        if energia_nueva < mejor_energia:
            mejor_solucion = nuevo_vecino
            mejor_energia = energia_nueva

        # Enfriar la temperatura
        temperatura *= tasa_enfriamiento

    return mejor_solucion, mejor_energia

# Parámetros del algoritmo
temperatura_inicial = 1000
tasa_enfriamiento = 0.99
iteraciones = 1000

# Ejecutar el algoritmo
mejor_solucion, mejor_energia = recocido_simulado(temperatura_inicial, tasa_enfriamiento, iteraciones)

print(f"Mejor solución: {mejor_solucion}")
print(f"Mejor energía (valor de la función objetivo): {mejor_energia}")
