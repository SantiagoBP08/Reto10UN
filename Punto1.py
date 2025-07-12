def leer_matriz(filas, columnas):
"""Lee una matriz desde el teclado"""
matriz = []
print("Ingrese los valores de la matriz:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = float(input(f"Matriz[{i}][{j}]: "))  # Pide cada elemento
        fila.append(valor)  # Agrega a la fila
    matriz.append(fila)  # Agrega la fila a la matriz
return matriz

def imprimir_matriz(matriz):
    """Imprime la matriz fila por fila"""
    for fila in matriz:
        print(fila)

def suma_resta_matrices(m1, m2, operacion):
    """Suma o resta dos matrices, según la operación indicada"""
    filas = len(m1)
    columnas = len(m1[0])
    resultado = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            if operacion == "+":
                fila.append(m1[i][j] + m2[i][j])  # Suma elementos
            elif operacion == "-":
                fila.append(m1[i][j] - m2[i][j])  # Resta elementos
        resultado.append(fila)
    return resultado

if __name__ == "__main__":
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))

    print("\n--- Matriz A ---")
    A = leer_matriz(filas, columnas)

    print("\n--- Matriz B ---")
    B = leer_matriz(filas, columnas)

    op = input("¿Desea sumar (+) o restar (-) las matrices?: ")

    if op not in ["+", "-"]:
        print("Operación inválida.")
    else:
        resultado = suma_resta_matrices(A, B, op)
        print("\n✅ Resultado:")
        imprimir_matriz(resultado)
