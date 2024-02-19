# Battleships

[Live Deployment of the game here](https://battle-ships-jc-e50b599c051e.herokuapp.com/)

![amiresponsive](docs/images/amiresponsive.png)

## How to play

In this game of Battleships, they player gets their grid with randomly placed ships represented by "X" the player then gets to guess the location of the computers ships, which are not marked on the grid.

If the player guesses correctly and hits a ship, that is represented by "*" if they guess incorrectly, a miss is represented by "O".

the player and computer take turns guessing coordinates until all ships are sank and a score of 4 is reached, after this score is reached then the player get the option to play again, and an overall tally tracks the results of each game played, this can go on until the player choses not to play any more.

## Features

## Data Model

The BattleshipGame class controls a game of Battleship. It sets up the game board, places ships randomly, and manages turns for the player and computer. Players take turns attacking by inputting coordinates, and the game updates the board accordingly. The class handles scoring and determines the winner. The play_battleship method orchestrates the game, while start_game starts the game and allows for multiple rounds. Overall, it provides a structured way to play Battleship with clear rules and outcomes.

## Testing

I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
- Tested in my local terminal and the Code Institute Heroku terminal

### Solved Bugs

- The issue stemmed from ships overlapping during random placement, which could result in scenarios where the player couldn't finish the game and win. I addressed this by introducing a condition in the place_ships_randomly function to ensure that each selected position for ship placement was not already occupied, preventing ship overlap and ensuring fair gameplay. This fix enabled the player to have a reasonable chance of winning by eliminating the possibility of unsolvable game states due to ship overlap.

### Unsolved Bugs

- There are no unfixed bugs

### Validator testing
- PEP8
    - No error were returned from https://pep8ci.herokuapp.com/
    

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
- Fork or clone this repository
- Create a new Heroku app
- Set the build backs to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on Deploy

## Credits
