# Python-Project1-Game2048

## Game2048 Visualization

This repository contains a visualization of the game 2048, implemented as a 4x4 grid (matrix). Initially, the grid contains two random cells with the number 2, while the remaining cells are empty. In each round, a new random 2 is generated in an empty cell. I can press 'w', 's', 'a', or 'd' to move the tiles up, down, left, or right, respectively. When a key is pressed, the tiles move in the corresponding direction. If two tiles with the same number collide in a move, they merge to form a tile with the sum of their values, and the rest of the cells become empty again. If no tiles with the same number are adjacent, all tiles move in the specified direction to fill the available space in that row or column. The objective is to reach the tile with the number 2048 to win the game. If I reach 2048, I can choose to restart or end the game. If no further moves are possible, the game ends, and one can choose to either restart or end it.

The repository includes exception handling to manage all invalid inputs. It consists of two files: the main file, which runs all the code and imports all functions from the second file, and the second Python file, which contains all the necessary functions.
