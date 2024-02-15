import random

grid_size = 5 
num_ships = 4
player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
revealed_player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
revealed_computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

def display_grid(grid):
    for row in grid:
        print(' '.join(row))

def place_ships_randomly(grid, num_ships):
    for _ in range(num_ships):
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        grid[row][col] = 'X'

place_ships_randomly(player_grid, num_ships)
place_ships_randomly(computer_grid, num_ships)

print("Player's Grid:")
display_grid(player_grid)

print("Computer's Grid:\n")
display_grid(computer_grid)