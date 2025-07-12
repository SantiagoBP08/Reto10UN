def leer_matriz(filas, columnas):
"""
Lee una matriz de tamaño filas x columnas desde el teclado.
Retorna la matriz como una lista de listas.
"""
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Ingrese el valor en posición [{i}][{j}]: "))
        fila.append(valor)  # Se añade el valor a la fila
    matriz.append(fila)  # Se añade la fila a la matriz
return matriz

def imprimir_matriz(matriz):
    """
    Imprime cada fila de la matriz.
    """
    print("\n📋 Matriz ingresada:")
    for fila in matriz:
        print(fila)

def sumar_fila(matriz, fila_objetivo):
    """
    Suma los elementos de una fila específica de la matriz.

    Parámetros:
    - matriz: lista de listas con números (la matriz).
    - fila_objetivo: número entero (índice de la fila que se quiere sumar).

    Retorna:
    - suma de los elementos de la fila seleccionada.
    """
    return sum(matriz[fila_objetivo])  # Suma directa de la fila

# Bloque principal
if __name__ == "__main__":
    # Se piden las dimensiones de la matriz
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    # Se lee la matriz desde el usuario
    matriz = leer_matriz(filas, columnas)
    imprimir_matriz(matriz)

    # Se pide la fila que se quiere sumar
    fila = int(input(f"Ingrese el índice de la fila a sumar (0 a {filas - 1}): "))

    # Validación del índice ingresado
    if 0 <= fila < filas:
        suma = sumar_fila(matriz, fila)
        print(f"\n✅ La suma de los elementos de la fila {fila} es: {suma}")
    else:
        print("Error: índice fuera del rango.")
