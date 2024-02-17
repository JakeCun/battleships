import random

grid_size = 5 
num_ships = 4

# Initialize scores
player_score = 0
computer_score = 0

# Keep track of attacked positions
player_attacks = set()
computer_attacks = set()

# Function to display a grid
def display_grid(grid, hide_ships=False, revealed_guesses=None):
    for i in range(grid_size):
        for j in range(grid_size):
            if hide_ships and grid is computer_grid:
                if revealed_guesses and revealed_guesses[i][j] == '*':
                    print('*', end=' ')  # Display hits as '*' for the computer's guesses
                elif revealed_guesses and revealed_guesses[i][j] == 'O':
                    print('O', end=' ')  # Display misses as 'O' for the computer's guesses
                elif grid[i][j] == 'X':
                    print('.', end=' ')  # Print '.' to hide the computer's ships
                else:
                    print(grid[i][j], end=' ')
            else:
                print(grid[i][j], end=' ')
        print()

# Function to randomly place ships on the grid
def place_ships_randomly(grid, num_ships):
    placed_ships = set()  # Keep track of placed ships
    while len(placed_ships) < num_ships:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        if (row, col) not in placed_ships:  # Check if the position is not occupied
            grid[row][col] = 'X'
            placed_ships.add((row, col))  # Add the placed ship position to the set

# Function to display ship locations
def display_ship_locations(grid):
    print("Ship Locations:")
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 'X':
                print(f"({i}, {j})", end=' ')
    print()

# Function for the player's turn
def player_turn():
    global player_score
    while True:
        try:
            row = int(input("Enter the row to attack (0-4): "))
            col = int(input("Enter the column to attack (0-4): "))
            
            if (row, col) in player_attacks:
                print("You've already attacked this cell. Please choose another location.")
                continue
            
            if 0 <= row < grid_size and 0 <= col < grid_size:
                player_attacks.add((row, col))  # Add the attacked position to the set
                if computer_grid[row][col] == 'X':
                    print("Hit!\n")
                    computer_grid[row][col] = '*'
                    player_score += 1  # Increment player's score when they hit the computer's ship
                else:
                    print("Miss!\n")
                    computer_grid[row][col] = 'O'
                break
            else:
                print("Coordinates must be within the range 0-4. Please try again.")
        except ValueError:
            print("Please enter valid integers for row and column.")

# Function for the computer's turn
def computer_turn():
    global computer_score
    while True:
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        
        if (row, col) in computer_attacks:
            continue  # If the computer has already attacked this position, choose another one
        
        computer_attacks.add((row, col))  # Add the attacked position to the set
        
        if player_grid[row][col] == 'X':
            print("Computer hit at ({}, {})!\n".format(row, col))
            player_grid[row][col] = '*'
            computer_score += 1  # Increment computer's score when it hits the player's ship
        else:
            print("Computer missed at ({}, {})!\n".format(row, col))
            player_grid[row][col] = 'O'
        break


# Function to play battleship game
def play_battleship():
    global player_grid
    global computer_grid
    global player_score
    global computer_score
    print("\n--- New Game ---")
    # Reset player's score
    player_score = 0
    computer_score = 0
    
    # Reset grids
    player_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    computer_grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Reset attacked positions
    player_attacks.clear()
    computer_attacks.clear()
    
    # Randomly place ships for both player and computer
    place_ships_randomly(player_grid, num_ships)
    place_ships_randomly(computer_grid, num_ships)
    
    # Display ship locations
    display_ship_locations(player_grid)
    display_ship_locations(computer_grid)
    
    # Display player's grid
    print("Player's Grid:")
    display_grid(player_grid)

    # Display computer's grid
    print("Computer's Grid:")
    display_grid(computer_grid, hide_ships=True)  # Hide computer's ships
    
    # Main game loop
    while True:
        # Player's turn
        print("Player's Turn:")
        player_turn()
        
        # Computer's turn
        print("\nComputer's Turn:")
        computer_turn()
        
        # Display grids after both turns
        print("\nPlayer's Grid:")
        display_grid(player_grid)
        print("Computer's Grid:")
        display_grid(computer_grid, hide_ships=True)
        
        # Print player's score
        print(f"Player's Score: {player_score}")

        # Print computer's score
        print(f"Computer's Score: {computer_score}")
        
        # Check for game end conditions
        if player_score == 4:
            print("Congratulations! You win!")
            break  # End the game
        elif computer_score == 4:
            print("Computer wins! Better luck next time.")
            break  # End the game

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        return True
    else:
        return False

# Main game loop
play_again = True
while play_again:
    play_again = play_battleship()
