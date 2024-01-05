# Ultimate Tic-Tac-Toe AI

Welcome to the Ultimate Tic-Tac-Toe AI project! This application takes the beloved game of Tic-Tac-Toe and elevates it with a challenging twist and AI integration. You can test your skills against an advanced AI opponent in both the Classic and Ultimate versions of Tic-Tac-Toe.

## Project Overview

Ultimate Tic-Tac-Toe is a more complex variant of the traditional Tic-Tac-Toe. The game board consists of a 3x3 grid, where each cell itself is a smaller 3x3 Tic-Tac-Toe board. The AI, powered by the Minimax algorithm with variable depth, calculates moves ahead, providing a challenging gameplay experience.

### Key Features:

- **Two Modes:** Classic and Ultimate Tic-Tac-Toe.
- **Advanced AI:** AI uses the Minimax algorithm to simulate game scenarios.
- **Customizable Difficulty:** Adjustable AI depth to set the challenge level.
- **Interactive UI:** Engaging user interface for a seamless gaming experience.

## The Minimax Algorithm

The Minimax algorithm is a decision-making tool used in artificial intelligence for optimal game-playing. Here's a breakdown of how it functions in our game:

1. **Game Tree Generation:** It starts from the current game state and simulates all possible moves.
2. **Scoring System:** Each end state of the game is scored based on whether it's a win, loss, or draw.
3. **Optimization:** The algorithm seeks to maximize the AI's score while assuming the opponent is trying to do the opposite.
4. **Recursion and Backtracking:** Through recursion, it evaluates the best possible move from the current state.
5. **Depth Parameter:** The depth parameter controls how many moves ahead the AI will calculate, impacting the difficulty level.

[![MinMax](https://img.youtube.com/vi/zDskcx8FStA/0.jpg)](https://www.youtube.com/watch?v=zDskcx8FStA)

_Click on this video to see a beautiful visual approach to the algorithm. All credits go to Shaul Markovitch on YouTube_

## Ultimate Tic-Tac-Toe Rules

In this variant, each move directs where the next move will be. If a player places their symbol in a particular cell of a small board, the next move must be played in the corresponding cell of the main board.

### Game Board Illustration:

![Ultimate Tic-Tac-Toe Board](https://upload.wikimedia.org/wikipedia/commons/a/a7/Ultimate_tic-tac-toe_X_victory.png)

_Ultimate Tic-Tac-Toe game board (Image Credit: Wikimedia Commons)_

## Getting Started

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yantavares/ultimate-tic-tac-toe-ai
   cd ultimate-tic-tac-toe-ai
   ```

2. **Install Dependencies:**

- Python 3.x required.
- Run the following command to install necessary packages:
  ```bash
  pip install -r requirements.txt
  ```

### How to Play

1. **Launch the Game:**

   ```bash
   python game.py
   ```

2. **Set AI Depth:** Input the desired depth for the AI (number of moves ahead it should calculate).

3. **Choose Game Mode:** Select between Classic and Ultimate Tic-Tac-Toe.

4. **Play:** Follow the on-screen instructions to compete against the AI.

## License

This project is released under the [GNU General Public License v3.0](LICENSE).
