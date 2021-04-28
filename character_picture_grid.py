# character picture grid
grid = [['.', '.', '.', '.', '.', '.'],        ['.', 'O', 'O', '.', '.', '.'],        ['O', 'O', 'O', 'O', '.', '.'],        ['O', 'O', 'O', 'O', 'O', '.'],        ['.', 'O', 'O', 'O', 'O', 'O'],        ['O', 'O', 'O', 'O', 'O', '.'],        ['O', 'O', 'O', 'O', '.', '.'],        ['.', 'O', 'O', '.', '.', '.'],        ['.', '.', '.', '.', '.', '.']]
height = len(grid)
width = len(grid[0])

for y in range(height):
    for x in range(width):
        print(grid[y][x], end='')
    print()
