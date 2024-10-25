import random

# Definir la función de aptitud (fitness)
def fitness(individuo):
    # Ejemplo de función de aptitud: suma de los genes
    return sum(individuo)

# Definir la función de selección
def seleccion(poblacion, num_seleccionados):
    # Selección por torneo
    seleccionados = []
    for _ in range(num_seleccionados):
        torneo = random.sample(poblacion, 3)
        seleccionados.append(max(torneo, key=fitness))
    return seleccionados

# Definir la función de cruzamiento
def cruzamiento(individuo1, individuo2):
    # Cruzamiento en un punto
    punto_cruzamiento = random.randint(1, len(individuo1) - 1)
    hijo1 = individuo1[:punto_cruzamiento] + individuo2[punto_cruzamiento:]
    hijo2 = individuo2[:punto_cruzamiento] + individuo1[punto_cruzamiento:]
    return hijo1, hijo2

# Definir la función de mutación
def mutacion(individuo):
    # Mutación aleatoria en un gen
    gen_mutado = random.randint(0, len(individuo) - 1)
    individuo[gen_mutado] = random.randint(0, 1)
    return individuo

# Parámetros del algoritmo
tam_poblacion = 100
num_generaciones = 100
num_seleccionados = 20

# Inicializar la población
poblacion = [[random.randint(0, 1) for _ in range(10)] for _ in range(tam_poblacion)]

# Ejecutar el algoritmo
for _ in range(num_generaciones):
    # Evaluación
    aptitudes = [fitness(individuo) for individuo in poblacion]
    
    # Selección
    seleccionados = seleccion(poblacion, num_seleccionados)
    
    # Cruzamiento
    hijos = []
    for _ in range(num_seleccionados):
        hijo1, hijo2 = cruzamiento(seleccionados[0], seleccionados[1])
        hijos.append(hijo1)
        hijos.append(hijo2)
    
    # Mutación
    mutados = [mutacion(hijo) for hijo in hijos]
    
    # Reemplazo
    poblacion = seleccionados + mutados

# Imprimir la mejor solución
mejor_solucion = max(poblacion, key=fitness)
print("Mejor solución:", mejor_solucion)
print("Aptitud:", fitness(mejor_solucion))
