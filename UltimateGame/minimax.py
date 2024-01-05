import random
import math


def check_win_or_tie_minimax(board):
    def check_small_board_win(board, start_row, start_col):
        # Check rows, columns, and diagonals in a 3x3 small board
        for i in range(3):
            if board[start_row + i][start_col] == board[start_row + i][start_col + 1] == board[start_row + i][start_col + 2] != 0:
                return board[start_row + i][start_col]
            if board[start_row][start_col + i] == board[start_row + 1][start_col + i] == board[start_row + 2][start_col + i] != 0:
                return board[start_row][start_col + i]

        if board[start_row][start_col] == board[start_row + 1][start_col + 1] == board[start_row + 2][start_col + 2] != 0:
            return board[start_row][start_col]
        if board[start_row + 2][start_col] == board[start_row + 1][start_col + 1] == board[start_row][start_col + 2] != 0:
            return board[start_row + 2][start_col]

        return None

    # Check each small board for a win or tie
    small_board_results = [[check_small_board_win(
        board, i * 3, j * 3) for j in range(3)] for i in range(3)]

    # Check the entire board for a win or tie
    for i in range(3):
        # Check rows and columns in the 3x3 grid of small boards
        if small_board_results[i][0] == small_board_results[i][1] == small_board_results[i][2] and small_board_results[i][0] is not None:
            return small_board_results[i][0]
        if small_board_results[0][i] == small_board_results[1][i] == small_board_results[2][i] and small_board_results[0][i] is not None:
            return small_board_results[0][i]

    # Check diagonals in the 3x3 grid of small boards
    if small_board_results[0][0] == small_board_results[1][1] == small_board_results[2][2] and small_board_results[0][0] is not None:
        return small_board_results[0][0]
    if small_board_results[2][0] == small_board_results[1][1] == small_board_results[0][2] and small_board_results[2][0] is not None:
        return small_board_results[2][0]

    # Check for a tie (no empty spaces left)
    for row in small_board_results:
        if any(result is None for result in row):
            return None  # Still ongoing

    return 0  # Tie


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
