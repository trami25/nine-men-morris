# Nine Men's Morris Game

## Overview

This is a basic implementation of the **Nine Men's Morris** game, where a human player can play against the computer. The game follows the traditional rules of Nine Men's Morris, a strategy board game for two players that dates back to the Roman Empire.

The goal is to form "mills" — three of your pieces in a row — which allows you to remove an opponent's piece from the board. The game has three distinct phases: placing pieces, moving pieces, and jumping (when a player has only three pieces left).

## Features

- **Person vs. Computer Mode**: The player competes against a basic AI opponent.
- **Game Phases**: Supports the two phases of the game (placing, moving).
- **Simple AI**: The AI opponent has basic decision-making skills for placing and moving pieces.

## How to Play

### Rules of the Game

1. **Placing Pieces**: Each player takes turns placing one of their nine pieces on any vacant point on the board. If a player forms a mill (three pieces in a row), they can remove one of their opponent's pieces, provided it is not part of a mill.
   
2. **Moving Pieces**: After all pieces are placed, players take turns moving their pieces to adjacent vacant points. If a player forms a mill, they again remove one of their opponent's pieces.

3. **Flying (Jumping)**: When a player has only three pieces remaining, they can "jump" their pieces to any vacant point on the board, not just adjacent ones.

4. **Winning**: The game is won when the opponent is reduced to two pieces or cannot make a valid move.

### Game Flow

1. The game starts with the player placing one of their nine pieces.
2. The computer will respond by placing one of its pieces.
3. The game continues until all pieces are placed, after which the movement phase begins.
4. Players can move their pieces until one player wins.

### Controls

- **Placing Pieces**: Click on an empty spot on the board to place your piece.
- **Moving Pieces**: After the placing phase, click on a piece you want to move, then click on an adjacent empty spot to move it.
- **Removing Opponent's Pieces**: When a mill is formed, click on one of the opponent's pieces that isn't part of a mill to remove it.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/trami25/nine-men-morris.git
