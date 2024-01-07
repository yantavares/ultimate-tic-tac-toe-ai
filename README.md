# Ultimate Tic-Tac-Toe AI with Enhanced Alpha-Beta Pruning

Welcome to the Ultimate Tic-Tac-Toe AI project, now upgraded with alpha-beta pruning to optimize performance! This application enhances the classic game of Tic-Tac-Toe, adding a more complex and strategic variant - Ultimate Tic-Tac-Toe, along with a challenging AI opponent.

## Project Overview

Ultimate Tic-Tac-Toe transforms the simple Tic-Tac-Toe game into a more sophisticated challenge. The game board is a 3x3 grid, with each cell containing another 3x3 Tic-Tac-Toe board. Our AI utilizes the Minimax algorithm, now improved with alpha-beta pruning, to calculate moves and provide an engaging gameplay experience.

### Key Features:

- **Two Modes:** Classic and Ultimate Tic-Tac-Toe.
- **Enhanced AI:** Uses Minimax algorithm with alpha-beta pruning for efficient decision-making.
- **Customizable Difficulty:** Vary the AI's calculation depth to adjust challenge levels.
- **Alpha-Beta Pruning:** Reduces the number of nodes evaluated by the minimax algorithm in the search tree, greatly improving performance, especially in the Ultimate Tic-Tac-Toe mode.

## Enhanced Minimax Algorithm

The Minimax algorithm, now with alpha-beta pruning, serves as the core of our AI's decision-making process:

1. **Game Tree Generation:** Generates potential game scenarios from the current state.
2. **Scoring System:** Assigns scores to terminal states (win, loss, draw).
3. **Alpha-Beta Pruning:** Optimizes the evaluation process by eliminating lesser paths earlier.
4. **Recursive Evaluation:** Determines the best move from the current game state.
5. **Depth Control:** Adjusts the calculation depth, affecting the difficulty level.

[![MiniMax](https://img.youtube.com/vi/zDskcx8FStA/0.jpg)](https://www.youtube.com/watch?v=zDskcx8FStA)

_Click on this video to see a beautiful visual approach to the Minimax algorithm. All credits go to Shaul Markovitch on YouTube_

## Ultimate Tic-Tac-Toe Rules

This variant's unique rule is that each move dictates the next play's location. If a player marks a cell in a small board, the next move must be in the corresponding cell of the main board.

### Game Board Illustration:

![Ultimate Tic-Tac-Toe Board](https://upload.wikimedia.org/wikipedia/commons/7/7d/Super_tic-tac-toe_rules_example.png)
_Figure 1: Ultimate Tic-Tac-Toe game board illustration. Image from Wikipedia._

## Getting Started

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yantavares/ultimate-tic-tac-toe-ai
   cd ultimate-tic-tac-toe-ai
   ```

2. **Install Dependencies:**

- Python 3.x required.
- Run `pip install -r requirements.txt`.

### How to Play

1. **Launch the Game:**

   ```bash
   python game.py
   ```

2. **Set AI Depth:** Input the desired depth (number of moves ahead to calculate).

3. **Choose Game Mode:** Select Classic or Ultimate Tic-Tac-Toe.

4. **Play:** Compete against the AI following on-screen instructions.

## Enhanced AI Mechanics

- **Alpha-Beta Pruning:** This technique is used in Ultimate Tic-Tac-Toe for better performance. It helps the AI to discard less promising moves faster, making the decision-making process much more efficient.

- **Board Evaluation:** In Ultimate Tic-Tac-Toe, the AI evaluates both each small board and the overall 3x3 grid to determine the best move. For the Classic mode, the approach is more brute-force due to the simpler game dynamics.

- **Depth Parameter:** In Ultimate Tic-Tac-Toe, a recommended depth is 2 due to the complexity of the algorithm. This ensures the AI is smart yet responsive. For the Classic version, setting the depth beyond one allows for unlimited moves ahead, ideal for simpler gameplay.

## License

This project is under the [GNU General Public License v3.0](LICENSE).
