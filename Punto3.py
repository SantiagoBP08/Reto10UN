def leer_matriz(filas, columnas):
"""Lee una matriz desde el teclado"""
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Matriz[{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)
return matriz

def imprimir_matriz(matriz):
    """Imprime la matriz fila por fila"""
    for fila in matriz:
        print(fila)

def transpuesta(matriz):
    """Retorna la matriz transpuesta"""
    filas = len(matriz)
    columnas = len(matriz[0])
    trans = []

    for j in range(columnas):  # Recorre columnas originales
        nueva_fila = []
        for i in range(filas):  # Recorre filas originales
            nueva_fila.append(matriz[i][j])  # Invierte las coordenadas
        trans.append(nueva_fila)
    return trans

if __name__ == "__main__":
    filas = int(input("Filas de la matriz: "))
    columnas = int(input("Columnas de la matriz: "))

    A = leer_matriz(filas, columnas)
    print("\n✅ Matriz original:")
    imprimir_matriz(A)

    T = transpuesta(A)
    print("\n📐 Matriz transpuesta:")
    imprimir_matriz(T)
