def leer_matriz(filas, columnas):
"""Lee una matriz ingresada por el usuario"""
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Matriz[{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)
return matriz

def imprimir_matriz(matriz):
    """Imprime la matriz en pantalla"""
    for fila in matriz:
        print(fila)

def sumar_columna(matriz, col):
    """Suma los elementos de una columna específica"""
    suma = 0
    for fila in matriz:
        suma += fila[col]  # Suma el valor de la columna indicada
    return suma

if __name__ == "__main__":
    filas = int(input("Filas de la matriz: "))
    columnas = int(input("Columnas de la matriz: "))

    A = leer_matriz(filas, columnas)
    imprimir_matriz(A)

    col = int(input(f"Ingrese el índice de la columna a sumar (0 a {columnas - 1}): "))

    if 0 <= col < columnas:
        total = sumar_columna(A, col)
        print(f"✅ La suma de la columna {col} es: {total}")
    else:
        print("Índice fuera de rango.")
