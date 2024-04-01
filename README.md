# Battleship Bandits

Battleship Bandits is a web game created using the template provided by Code Institute and deployed through Heroku. This is a game for users to test themselves against an automated computer. The aim of the game is to sink all the computer's battleships before it sinks yours.

Link to the live game: https://portfolio4-battleships-2a70410d4d1b.herokuapp.com/

![image](https://github.com/zyprech/portf4/assets/161986102/0092b144-d3b7-49a1-b04e-9e2b099d732b)

How to play

Each player has a 5x5 grid where their battleships are randomly spawned. The goal is to guess correct coordinates inorder to sink the opponents ships.
The user and computer take turns guessing coordinates (column and row) within the range of 1 to 5.
X indicates a location that has not been guessed yet, * indicated a missed location and # represents a location where a battleship has been sunk.
The winner is declared once all of someones ships have been sunk or after 10 turns whoever has sunk the most ships wins.


Features

Randomized ship placements - Ships are randomly places everytime at the start of the game.
Feedback - The game will give you feedback based on the guesses you make.
Data - The game will keep track of data to determine the winner.

![image](https://github.com/zyprech/portf4/assets/161986102/598d7721-9265-4229-9744-9d1b1d8e760c)
![image](https://github.com/zyprech/portf4/assets/161986102/13f860fc-27c1-4f34-886d-364fa2862346)

Error handling: Game makes sure that users type in the correct coordinate range and that they input only numbers.
![image](https://github.com/zyprech/portf4/assets/161986102/17aebfc3-3e6d-47ed-86a8-17eed730a688)


Testing

Tested using https://pep8ci.herokuapp.com/: No errors


Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

The steps for deployment are as follows:

Fork or clone this repository
Create a new Heroku app
Set the buildpacks to Python and NodeJS in that order
Link the Heroku app to the repository
Click on Deploy


Credits

Code institute for the deployment terminal
Game inspiration: Code institute portfolio example.



