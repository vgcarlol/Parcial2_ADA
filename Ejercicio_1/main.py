# Mapping del teclado
keypad = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

# Movimientos válidos
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

from functools import lru_cache

# Crear el mapa de posiciones
position = {}
for i in range(4):
    for j in range(3):
        if keypad[i][j] not in '*#':
            position[keypad[i][j]] = (i, j)

# Obtener adyacentes
def get_adjacent(digit):
    adj = []
    x, y = position[digit]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 3 and keypad[nx][ny] not in '*#':
            adj.append(keypad[nx][ny])
    return adj

# Función recursiva con memoización
@lru_cache(maxsize=None)
def count_combinations(digit, length):
    if length == 1:
        return 1
    total = 0
    for neighbor in get_adjacent(digit) + [digit]:
        total += count_combinations(neighbor, length - 1)
    return total

# Función principal
def total_combinations(n):
    total = 0
    for d in '0123456789':
        total += count_combinations(d, n)
    return total

# Para probar
if __name__ == "__main__":
    n = 2
    print(f"Total combinaciones posibles para n={n}: {total_combinations(n)}")
    n = 10
    print(f"Total combinaciones posibles para n={n}: {total_combinations(n)}")
