from functools import lru_cache

# Definición del teclado y movimientos permitidos
TECLADO = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

MOVIMIENTOS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, abajo, izquierda, derecha

# Construir un mapa de posiciones para cada dígito (ignorando * y #)
def construir_mapa_posiciones():
    mapa = {}
    for fila in range(4):
        for columna in range(3):
            tecla = TECLADO[fila][columna]
            if tecla not in '*#':
                mapa[tecla] = (fila, columna)
    return mapa

POSICIONES = construir_mapa_posiciones()

# Función para obtener las teclas adyacentes válidas de un dígito
def obtener_adyacentes(digito):
    adyacentes = []
    x, y = POSICIONES[digito]
    for dx, dy in MOVIMIENTOS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 3:
            vecino = TECLADO[nx][ny]
            if vecino not in '*#':
                adyacentes.append(vecino)
    return adyacentes

# Función recursiva con memoización para contar combinaciones
@lru_cache(maxsize=None)
def contar_combinaciones(digito, longitud):
    if longitud == 1:
        return 1
    total = 0
    # Moverse a adyacentes
    for siguiente in obtener_adyacentes(digito):
        total += contar_combinaciones(siguiente, longitud - 1)
    # Quedarse en el mismo dígito
    total += contar_combinaciones(digito, longitud - 1)
    return total

# Función principal para calcular el total de combinaciones posibles
def calcular_combinaciones_totales(n):
    return sum(contar_combinaciones(d, n) for d in '0123456789')

# Ejecución para probar
if __name__ == "__main__":
    for n in [2, 10]:
        resultado = calcular_combinaciones_totales(n)
        print(f"Total de combinaciones posibles para n={n}: {resultado}")
