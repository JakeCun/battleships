import random

grid_size = 5 
num_ships = 4
player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
revealed_player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
revealed_computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

def display_grid(grid, hide_ships=False):
    for i in range(grid_size):
        for j in range(grid_size):
            if hide_ships and grid is computer_grid and revealed_computer_grid[i][j] == 'X':
                print('.', end=' ')  # Hide computer's ships
            else:
                print(grid[i][j], end=' ')
        print()

def place_ships_randomly(grid, num_ships, hide_ships=False):
    for _ in range(num_ships):
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        if not (hide_ships and grid is computer_grid):
            grid[row][col] = 'X'  # Only place ships if hide_ships is False

place_ships_randomly(player_grid, num_ships)
place_ships_randomly(computer_grid, num_ships, hide_ships=True)  # Hide ships for the computer

print("Player's Grid:")
display_grid(player_grid)

print("Computer's Grid:\n")
display_grid(computer_grid, hide_ships=True)  # Hide ships for the computer
