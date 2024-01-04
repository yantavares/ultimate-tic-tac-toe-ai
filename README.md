# Ultimate Tic-Tac-Toe AI - Work in progress

## Overview

This project features an AI-powered Ultimate Tic-Tac-Toe game using the Minimax Algorithm. Ultimate Tic-Tac-Toe takes the classic game and adds a layer of complexity, with each cell of the Tic-Tac-Toe board containing another Tic-Tac-Toe board. The AI uses reinforcement learning to train itself for an arbitrary amount of time, continually improving its strategy. Players can choose to play the classic version or the more complex Ultimate version against the AI.

## Minimax Algorithm

### Overview

This project employs the Minimax algorithm to enhance the AI's decision-making abilities in both the Classic and Ultimate versions of Tic-Tac-Toe. Minimax is a recursive algorithm used in decision-making and game theory to find the optimal move for a player, assuming that the opponent is also playing optimally.

### How Minimax Works

The Minimax algorithm works by simulating all possible moves in the game (both by the AI and its opponent), creating a game tree of possibilities. Each node of the tree represents a possible state of the game after a series of moves. The algorithm explores these nodes, assigning a score to each possible state:

- **Positive Score:** Indicates a state where the AI wins.
- **Negative Score:** Represents a state where the opponent wins.
- **Zero Score:** Denotes a draw.

The algorithm performs the following steps:

1. **Generate Game Tree:** Starting from the current state of the game, the algorithm generates all possible moves and their outcomes, building a tree of game states.

2. **Evaluate Leaf Nodes:** At the leaf nodes (where the game ends), the algorithm evaluates the outcome assigning scores (win, lose, draw).

3. **Minimize and Maximize:** The algorithm assumes that the AI aims to maximize its score (win), while the opponent aims to minimize the AI's score (making the AI lose). At each level, the algorithm chooses the move that provides the maximum score for the AI and the minimum score for the opponent.

4. **Recursion:** The process continues recursively, with the algorithm moving back up the tree, selecting the best possible move at each level, until it reaches the current state of the game.

5. **Best Move:** The top of the tree then contains the AI's optimal move based on the assumption that the opponent also plays optimally.

## Ultimate Tic-Tac-Toe: How It Works

In Ultimate Tic-Tac-Toe, each move affects which board the next player must play in. For example, if Player X places an 'X' in the top right square of a small board, Player O must play their next move on the small board located in the top right of the overall grid.

### Visual Explanation:

```
Main Board:     |   Small Board:
[0][1][2]       |   [0][1][2]
[3][4][5]  ->   |   [3][4][5]
[6][7][8]       |   [6][7][8]

- Each cell [0]-[8] in the Main Board contains a full Small Board.
- A move in cell [n] in any Small Board directs the next move to the Small Board at cell [n] in the Main Board.
```

<div id="img" align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/Ultimate_tic-tac-toe_X_victory.png" alt="Ultimate Tic-Tac-Toe Diagram" title="Ultimate Tic-Tac-Toe Board Example" width="300" style="margin: 0 auto; display: block;"/>
</div>

<div id="caption" align="center">
    <figcaption style="margin: 0 auto;" align="center">
        Figure 1: Ultimate Tic-Tac-Toe game board illustration. Image from
        <a href="https://commons.wikimedia.org/wiki/File:Ultimate_tic-tac-toe_X_victory.png">Wikimedia</a>
    </figcaption>
</div>

## Installation

1. **Clone the Repository:**

   ```
   git clone https://github.com/yantavares/ultimate-tic-tac-toe-ai
   cd ultimate-tic-tac-toe-ai
   ```

2. **Install Dependencies:**
   - Ensure Python is installed on your system.
   - Install required packages using `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

## How to Play

1. **Start the Game:**

   - Launch the game by running a single script.
     ```
     python game.py
     ```

2. **Train the AI:**

   - Upon starting the script, you'll be prompted to enter the training duration for the AI. This step is optional; you can enter `0` or skip it to use the AI's existing training level.

3. **Choose Game Mode:**

   - After the AI training (if opted), you'll be prompted to choose between the Classic and Ultimate version of Tic-Tac-Toe.

4. **Game Rules:**

   - Follow the on-screen instructions to play against the AI. The game rules for both Classic and Ultimate Tic-Tac-Toe will be displayed.

## License

This project is licensed under the [GNU LICENSE](LICENSE).
