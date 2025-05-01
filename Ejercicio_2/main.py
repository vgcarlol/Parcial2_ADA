def cruz_mas_grande(matriz):
    n = len(matriz)
    if n == 0:
        return 0

    izquierda = [[0] * n for _ in range(n)]
    derecha = [[0] * n for _ in range(n)]
    arriba = [[0] * n for _ in range(n)]
    abajo = [[0] * n for _ in range(n)]

    # Primera pasada: calcular izquierda y arriba
    for fila in range(n):
        for columna in range(n):
            if matriz[fila][columna] == 1:
                izquierda[fila][columna] = (izquierda[fila][columna - 1] if columna > 0 else 0) + 1
                arriba[fila][columna] = (arriba[fila - 1][columna] if fila > 0 else 0) + 1

    # Segunda pasada: calcular derecha y abajo
    for fila in range(n - 1, -1, -1):
        for columna in range(n - 1, -1, -1):
            if matriz[fila][columna] == 1:
                derecha[fila][columna] = (derecha[fila][columna + 1] if columna < n - 1 else 0) + 1
                abajo[fila][columna] = (abajo[fila + 1][columna] if fila < n - 1 else 0) + 1

    max_cruz = 0
    # Verificar la cruz más grande posible en cada celda
    for fila in range(n):
        for columna in range(n):
            if matriz[fila][columna] == 1:
                brazo = min(izquierda[fila][columna], derecha[fila][columna],
                            arriba[fila][columna], abajo[fila][columna])
                if brazo > 0:
                    tamaño = 4 * (brazo - 1) + 1
                    max_cruz = max(max_cruz, tamaño)

    return max_cruz

# Ejecución de ejemplo
if __name__ == "__main__":
    matriz = [
        [1, 0, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1]
    ]
    resultado = cruz_mas_grande(matriz)
    print(f"Tamaño de la cruz más grande: {resultado}")
