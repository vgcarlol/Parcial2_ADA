def largest_cross(grid):
    n = len(grid)
    if n == 0:
        return 0

    left = [[0]*n for _ in range(n)]
    right = [[0]*n for _ in range(n)]
    top = [[0]*n for _ in range(n)]
    bottom = [[0]*n for _ in range(n)]

    # Primera pasada: llenar left y top
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                left[i][j] = (left[i][j-1] if j > 0 else 0) + 1
                top[i][j] = (top[i-1][j] if i > 0 else 0) + 1

    # Segunda pasada: llenar right y bottom
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if grid[i][j] == 1:
                right[i][j] = (right[i][j+1] if j < n-1 else 0) + 1
                bottom[i][j] = (bottom[i+1][j] if i < n-1 else 0) + 1

    max_cross = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                arm_length = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
                if arm_length > 0:
                    size = 4 * (arm_length - 1) + 1
                    max_cross = max(max_cross, size)

    return max_cross

# Ejecución:
if __name__ == "__main__":
    grid = [
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
    print(f"Tamaño de la cruz más grande: {largest_cross(grid)}")
