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
    """Imprime una matriz en pantalla"""
    for fila in matriz:
        print(fila)

def producto_matrices(A, B):
    """Calcula el producto de dos matrices A y B"""
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])
    resultado = []

    for i in range(filas_A):  # Recorre filas de A
        fila = []
        for j in range(columnas_B):  # Recorre columnas de B
            suma = 0
            for k in range(columnas_A):  # Recorre columnas de A y filas de B
                suma += A[i][k] * B[k][j]  # Suma productos correspondientes
            fila.append(suma)  # Agrega resultado a la fila
        resultado.append(fila)  # Agrega fila al resultado
    return resultado

if __name__ == "__main__":
    f1 = int(input("Filas de A: "))
    c1 = int(input("Columnas de A: "))
    f2 = int(input("Filas de B: "))
    c2 = int(input("Columnas de B: "))

    # Validación de compatibilidad
    if c1 != f2:
        print("No se puede multiplicar: columnas de A deben ser igual a filas de B.")
    else:
        print("\n--- Matriz A ---")
        A = leer_matriz(f1, c1)
        print("\n--- Matriz B ---")
        B = leer_matriz(f2, c2)
        resultado = producto_matrices(A, B)
        print("\n✅ Resultado del producto:")
        imprimir_matriz(resultado)
