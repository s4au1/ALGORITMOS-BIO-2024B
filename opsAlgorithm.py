import random

# Generar una permutación de los valores
def generar_permutacion(valores):
    valores_permutados = list(valores)
    random.shuffle(valores_permutados)  # Desordena aleatoriamente los valores
    return valores_permutados

# Crear diccionarios para mapear valores en claro a valores cifrados y viceversa
def crear_mapeo_ope(valores_claros):
    valores_cifrados = generar_permutacion(valores_claros)
    # Crear un mapeo de claro a cifrado
    ope_mapeo = {valor_claro: valor_cifrado for valor_claro, valor_cifrado in zip(sorted(valores_claros), sorted(valores_cifrados))}
    return ope_mapeo

# Función para cifrar un conjunto de valores
def cifrar(valores, ope_mapeo):
    return [ope_mapeo[valor] for valor in valores]

# Función para descifrar un conjunto de valores
def descifrar(valores_cifrados, ope_mapeo):
    # Invertir el mapeo para descifrar
    mapeo_invertido = {v: k for k, v in ope_mapeo.items()}
    return [mapeo_invertido[valor_cifrado] for valor_cifrado in valores_cifrados]

# Ejemplo de uso
if __name__ == "__main__":
    # Conjunto de datos a cifrar
    valores_claros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Crear el mapeo de OPE
    ope_mapeo = crear_mapeo_ope(valores_claros)

    print("Mapeo claro -> cifrado:")
    print(ope_mapeo)

    # Valores que queremos cifrar
    valores_a_cifrar = [20, 40, 60, 80, 100]
    print(f"\nValores a cifrar: {valores_a_cifrar}")

    # Cifrar los valores
    valores_cifrados = cifrar(valores_a_cifrar, ope_mapeo)
    print(f"Valores cifrados: {valores_cifrados}")

    # Descifrar los valores
    valores_descifrados = descifrar(valores_cifrados, ope_mapeo)
    print(f"Valores descifrados: {valores_descifrados}")
