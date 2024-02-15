grid_size = 5 
player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
revealed_player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
revealed_computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

def display_grid(grid):
    for row in grid:
        print(' '.join(row))

print("Player's Grid:")
display_grid(player_grid)

print("\nComputer's Grid:")
display_grid(computer_grid)