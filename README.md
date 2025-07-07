# RETO #10

Desarrolle la mayoría de los ejercicios en clase, por cada punto resuelto en clase tendrá media décima en el examen 2 (créanme, las van a necesitar). Para cada punto cree un programa individual. Al finalizar suba todo a un repo y súbalo al canal reto_11 en slack.

## Ejercicios en clase (por decimas en el parcial):

## 1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

    def leer_matriz(filas, columnas, nombre="matriz"):
    print(f"Ingrese los valores para la {nombre}:")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"{nombre}[{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

    def imprimir_matriz(matriz):
        for fila in matriz:
            print(fila)

    def sumar_matrices(A, B):
        filas = len(A)
        columnas = len(A[0])
        suma = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(A[i][j] + B[i][j])
            suma.append(fila)
        return suma

    def restar_matrices(A, B):
        filas = len(A)
        columnas = len(A[0])
        resta = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(A[i][j] - B[i][j])
            resta.append(fila)
        return resta

    if __name__ == "__main__":
        filas = int(input("Ingrese el número de filas de las matrices: "))
        columnas = int(input("Ingrese el número de columnas de las matrices: "))

        A = leer_matriz(filas, columnas, "matriz A")
        B = leer_matriz(filas, columnas, "matriz B")

        print("¿Qué operación desea realizar?")
        print("1. Suma")
        print("2. Resta")
        opcion = input("Seleccione una opción (1/2): ")

        if opcion == "1":
            resultado = sumar_matrices(A, B)
            print("Resultado de la suma:")
            imprimir_matriz(resultado)
        elif opcion == "2":
            resultado = restar_matrices(A, B)
            print("Resultado de la resta:")
            imprimir_matriz(resultado)
        else:
            print("Opción no válida.")
            
## 2. Desarrolle un programa que permita realizar el producto de matrices . El programa debe validar las condiciones necesarias para ejecutar la operación.

    def leer_matriz(filas, columnas, nombre="matriz"):
    print(f"Ingrese los valores para la {nombre}:")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"{nombre}[{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

    def imprimir_matriz(matriz):
        for fila in matriz:
        print(fila)

    def multiplicar_matrices(A, B):
        m = len(A)
        n = len(A[0])       # columnas de A == filas de B
        p = len(B[0])       # columnas de B

        resultado = [[0 for _ in range(p)] for _ in range(m)]

        for i in range(m):
            for j in range(p):
                for k in range(n):
                    resultado[i][j] += A[i][k] * B[k][j]

        return resultado

    if __name__ == "__main__":
        filas_A = int(input("Ingrese el número de filas de la matriz A: "))
        columnas_A = int(input("Ingrese el número de columnas de la matriz A: "))

        filas_B = int(input("Ingrese el número de filas de la matriz B: "))
        columnas_B = int(input("Ingrese el número de columnas de la matriz B: "))

        if columnas_A != filas_B:
            print("❌ No se puede multiplicar: el número de columnas de A debe ser igual al número de filas de B.")
        else:
            A = leer_matriz(filas_A, columnas_A, "matriz A")
            B = leer_matriz(filas_B, columnas_B, "matriz B")

            producto = multiplicar_matrices(A, B)
            print("✅ Resultado del producto de matrices:")
            imprimir_matriz(producto)
