# RETO #10

Desarrolle la mayoría de los ejercicios en clase, por cada punto resuelto en clase tendrá media décima en el examen 2 (créanme, las van a necesitar). Para cada punto cree un programa individual. Al finalizar suba todo a un repo y súbalo al canal reto_11 en slack.

## Ejercicios en clase (por decimas en el parcial):

1. 

## 1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

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
        
## 2. Desarrolle un programa que permita realizar el producto de matrices . El programa debe validar las condiciones necesarias para ejecutar la operación.

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


## 3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

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


## 4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

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

## 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.

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

Aca terminamos los 5 puntos y los ejercicios de clase.   
