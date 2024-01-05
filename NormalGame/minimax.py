import random
import math


def check_win_or_tie_minimax(board, rows=3, cols=3):
    # Check rows
    for row in range(rows):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]

    # Check columns
    for col in range(cols):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    # Check tie
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                return None

    return 0


def minimax(board, isMaximizing, depth, maxDepth, rows=3, cols=3):
    result = check_win_or_tie_minimax(board)

    # Base cases
    if result != None:
        if result == 1:  # Player wins
            return -10
        elif result == 2:  # AI Wins
            return 10
        else:
            return 0  # Tie

    # Maximum depth reached (if maxDepth == 0, then there is no maximum depth)
    if maxDepth != 0 and depth == maxDepth:
        return 0  # Stop searching

    if isMaximizing:
        bestScore = -math.inf
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 0:
                    board[row][col] = 2
                    score = minimax(board, False, depth + 1, maxDepth)
                    board[row][col] = 0
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = math.inf
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 0:
                    board[row][col] = 1
                    score = minimax(board, True, depth + 1, maxDepth)
                    board[row][col] = 0
                    bestScore = min(score, bestScore)
        return bestScore


def make_move(board, maxDepth, rows=3, cols=3):
    bestScore = -math.inf
    bestMoves = []

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, False, 0, maxDepth)
                board[row][col] = 0

                if score > bestScore:
                    bestScore = score
                    bestMoves = [(row, col)]
                elif score == bestScore:
                    bestMoves.append((row, col))

    # Randomly choose one of the best moves
    bestMove = random.choice(bestMoves)
    board[bestMove[0]][bestMove[1]] = 2
    return board
