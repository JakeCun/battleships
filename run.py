import random

grid_size = 5 
num_ships = 4

# Initialize grids
player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
revealed_player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
revealed_computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

# Function to display a grid
def display_grid(grid, hide_ships=False):
    """
    Display a grid.

    Args:
        grid (list): The grid to display.
        hide_ships (bool): Whether to hide ships or not (default is False).
    """
    for i in range(grid_size):
        for j in range(grid_size):
            # If hiding ships for the computer and the cell contains a ship
            if hide_ships and grid is computer_grid and revealed_computer_grid[i][j] == 'X':
                print('.', end=' ')  # Print '.' to hide the ship
            else:
                print(grid[i][j], end=' ')  # Print the content of the cell
        print()

# Function to randomly place ships on the grid
def place_ships_randomly(grid, num_ships, hide_ships=False):
    """
    Randomly place ships on the grid.

    Args:
        grid (list): The grid on which to place ships.
        num_ships (int): The number of ships to place.
        hide_ships (bool): Whether to hide ships or not (default is False).
    """
    for _ in range(num_ships):
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        # Place ships only if not hiding ships for the computer
        if not (hide_ships and grid is computer_grid):
            grid[row][col] = 'X'  # Mark the cell as containing a ship

# Function for the player's turn
def player_turn():
    """
    Handle the player's turn.
    """
    while True:
        try:
            row = int(input("Enter the row to attack (0-4): "))
            col = int(input("Enter the column to attack (0-4): "))
            
            # Validate input coordinates
            if 0 <= row < grid_size and 0 <= col < grid_size:
                # Check if the cell has already been attacked
                if revealed_computer_grid[row][col] != '.':
                    print("You've already attacked this cell. Please choose another location.")
                    continue
                else:
                    # Check if the attack hits or misses
                    if computer_grid[row][col] == 'X':
                        print("Hit!\n")
                        revealed_computer_grid[row][col] = '*'  # Mark the attack as a hit
                    else:
                        print("Miss!\n")
                        revealed_computer_grid[row][col] = 'O'  # Mark the attack as a miss
                    break
            else:
                print("Coordinates must be within the range 0-4. Please try again.")
        except ValueError:
            print("Please enter valid integers for row and column.")

# Randomly place ships for both player and computer
place_ships_randomly(player_grid, num_ships)
place_ships_randomly(computer_grid, num_ships, hide_ships=True)  # Hide ships for the computer

# Display player's grid
print("Player's Grid:")
display_grid(player_grid)

# Display computer's grid with hidden ships
print("Computer's Grid:")
display_grid(computer_grid, hide_ships=True)

# Player's turn
print("Player's Turn:\n")
player_turn()

# Display updated player's grid
print("Player's Grid:")
display_grid(player_grid)

# Display updated computer's grid with hidden ships
print("\nComputer's Grid:")
display_grid(computer_grid, hide_ships=True)
