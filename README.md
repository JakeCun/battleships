# Battleships

[Live Deployment of the game here](https://battle-ships-jc-e50b599c051e.herokuapp.com/)

![amiresponsive](docs/images/amiresponsive.png)

## How to play

In this game of Battleships, they player gets their grid with randomly placed ships represented by "X" the player then gets to guess the location of the computers ships, which are not marked on the grid.

If the player guesses correctly and hits a ship, that is represented by "*" if they guess incorrectly, a miss is represented by "O".

the player and computer take turns guessing coordinates until all ships are sank and a score of 4 is reached, after this score is reached then the player get the option to play again, and an overall tally tracks the results of each game played, this can go on until the player choses not to play any more.

## Features

## Testing

I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
- Tested in my local terminal and the Code Institute Heroku terminal

### Unfixed Bugs

There are no unfixed bugs

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
- Fork or clone this repository
- Create a new Heroku app
- Set the build backs to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on Deploy

## Credits
