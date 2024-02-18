import random

class BattleshipGame:
    def __init__(self, grid_size=5, num_ships=4):
        self.grid_size = grid_size
        self.num_ships = num_ships
        self.player_score = 0
        self.computer_score = 0
        self.total_player_wins = 0
        self.total_computer_wins = 0
        self.player_attacks = set()
        self.computer_attacks = set()
        self.player_grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
        self.place_ships_randomly(self.player_grid)
        self.place_ships_randomly(self.computer_grid)

    def place_ships_randomly(self, grid):
        placed_ships = set()
        while len(placed_ships) < self.num_ships:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if (row, col) not in placed_ships:
                grid[row][col] = "X"
                placed_ships.add((row, col))

    def display_grid(self, grid, hide_ships=False, revealed_guesses=None):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if hide_ships and grid is self.computer_grid:
                    if revealed_guesses and revealed_guesses[i][j] == "*":
                        print("*", end=" ")
                    elif revealed_guesses and revealed_guesses[i][j] == "O":
                        print("O", end=" ")
                    elif grid[i][j] == "X":
                        print(".", end=" ")
                    else:
                        print(grid[i][j], end=" ")
                else:
                    print(grid[i][j], end=" ")
            print()

    def player_turn(self):
        while True:
            try:
                row = int(input("Enter the row to attack (0-4): "))
                col = int(input("Enter the column to attack (0-4): "))

                if (row, col) in self.player_attacks:
                    print("You've already attacked this cell. Please choose another location.")
                    continue

                if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
                    self.player_attacks.add((row, col))
                    if self.computer_grid[row][col] == "X":
                        print("Hit!\n")
                        self.computer_grid[row][col] = "*"
                        self.player_score += 1
                    else:
                        print("Miss!\n")
                        self.computer_grid[row][col] = "O"
                    break
                else:
                    print("Coordinates must be within 0-4. Please try again.")
            except ValueError:
                print("Please enter valid integers for row and column.")

    def computer_turn(self):
        while True:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if (row, col) in self.computer_attacks:
                continue
            self.computer_attacks.add((row, col))
            if self.player_grid[row][col] == "X":
                print("Computer hit at ({}, {})!\n".format(row, col))
                self.player_grid[row][col] = "*"
                self.computer_score += 1
            else:
                print("Computer missed at ({}, {})!\n".format(row, col))
                self.player_grid[row][col] = "O"
            break

    def play_battleship(self):
        print("\n--- New Game ---")
        self.player_score = 0
        self.computer_score = 0
        self.player_grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.computer_grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.player_attacks.clear()
        self.computer_attacks.clear()
        self.place_ships_randomly(self.player_grid)
        self.place_ships_randomly(self.computer_grid)
        print("Player's Grid:")
        self.display_grid(self.player_grid)
        print("Computer's Grid:")
        self.display_grid(self.computer_grid, hide_ships=True)

        while True:
            print("Player's Turn:")
            self.player_turn()
            print("\nComputer's Turn:")
            self.computer_turn()
            print("\nPlayer's Grid:")
            self.display_grid(self.player_grid)
            print("Computer's Grid:")
            self.display_grid(self.computer_grid, hide_ships=True)
            print(f"Player's Score: {self.player_score}")
            print(f"Computer's Score: {self.computer_score}")
            if self.player_score == self.num_ships:
                print("Congratulations! You win!")
                self.total_player_wins += 1
                break
            elif self.computer_score == self.num_ships:
                print("Computer wins! Better luck next time.")
                self.total_computer_wins += 1
                break
        print(f"Total Player Wins: {self.total_player_wins}")
        print(f"Total Computer Wins: {self.total_computer_wins}")

    def start_game(self):
        play = input("Guess the coordinates on your opponent's grid (e.g., 3,2) to locate their ships, aiming sink them while avoiding misses to win the game. \nDo you want to play Battleship? (y/n): ")
        while play.lower() == "y":
            self.play_battleship()
            play = input("Do you want to play again? (y/n): ")
        print("Goodbye!")

if __name__ == "__main__":
    game = BattleshipGame()
    game.start_game()
