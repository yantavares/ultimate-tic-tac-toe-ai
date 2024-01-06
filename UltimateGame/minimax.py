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


def minimax(board, isMaximizing, depth, maxDepth, alpha, beta, rows=9, cols=9):
    """
    Minimax algorithm with alpha-beta pruning.
    """
    result = check_win_or_tie_minimax(board)

    # Base cases
    if result is not None:
        return evaluate_result(result)  # Evaluate the result

    if maxDepth != 0 and depth == maxDepth:
        return evaluate_board(board)  # Evaluate the board state

    if isMaximizing:
        bestScore = -math.inf
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 0:
                    board[row][col] = 2
                    score = minimax(board, False, depth + 1,
                                    maxDepth, alpha, beta)
                    board[row][col] = 0
                    bestScore = max(score, bestScore)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
    else:
        bestScore = math.inf
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 0:
                    board[row][col] = 1
                    score = minimax(board, True, depth + 1,
                                    maxDepth, alpha, beta)
                    board[row][col] = 0
                    bestScore = min(score, bestScore)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
    return bestScore


def evaluate_result(result):
    if result == 1:  # Player wins
        return -10
    elif result == 2:  # AI Wins
        return 10
    else:
        return 0  # Tie


def evaluate_board(board):
    score = 0

    # Evaluate each small board
    for i in range(3):
        for j in range(3):
            score += evaluate_small_board(board, i * 3, j * 3)

    # Evaluate the overall 3x3 grid
    score += evaluate_overall_grid(board)

    return score


def evaluate_small_board(board, start_row, start_col):
    small_board_score = 0
    lines = []

    # Rows, columns and diagonals in small board
    for i in range(3):
        row = [board[start_row + i][start_col + j] for j in range(3)]
        col = [board[start_row + j][start_col + i] for j in range(3)]
        lines.append(row)
        lines.append(col)

    diag1 = [board[start_row + i][start_col + i] for i in range(3)]
    diag2 = [board[start_row + i][start_col + 2 - i] for i in range(3)]
    lines.append(diag1)
    lines.append(diag2)

    for line in lines:
        small_board_score += evaluate_line(line)

    # Extra score for the central cell
    if board[start_row + 1][start_col + 1] == 2:
        small_board_score += 3  # AI controls the center
    elif board[start_row + 1][start_col + 1] == 1:
        small_board_score -= 3  # Opponent controls the center

    return small_board_score


def evaluate_line(line):
    if line.count(2) == 3:
        return 100  # AI wins the line
    elif line.count(1) == 3:
        return -100  # Opponent wins the line
    elif line.count(2) == 2 and line.count(0) == 1:
        return 10  # AI is close to winning the line
    elif line.count(1) == 2 and line.count(0) == 1:
        return -10  # Opponent is close to winning the line
    return 0


def evaluate_overall_grid(board):
    overall_grid_score = 0
    small_boards = [[get_small_board_winner(
        board, i * 3, j * 3) for j in range(3)] for i in range(3)]

    # Check rows, columns, and diagonals in the overall 3x3 grid
    for i in range(3):
        # Row
        overall_grid_score += evaluate_line([small_boards[i][j]
                                            for j in range(3)])
        # Column
        overall_grid_score += evaluate_line([small_boards[j][i]
                                            for j in range(3)])

    # Diagonal 1
    overall_grid_score += evaluate_line([small_boards[i][i] for i in range(3)])
    # Diagonal 2
    overall_grid_score += evaluate_line([small_boards[i][2 - i]
                                        for i in range(3)])

    return overall_grid_score


def get_small_board_winner(board, start_row, start_col):
    # Check for winner in a 3x3 small board
    for i in range(3):
        if board[start_row + i][start_col] == board[start_row + i][start_col + 1] == board[start_row + i][start_col + 2] != 0:
            return board[start_row + i][start_col]
        if board[start_row][start_col + i] == board[start_row + 1][start_col + i] == board[start_row + 2][start_col + i] != 0:
            return board[start_row][start_col + i]

    if board[start_row][start_col] == board[start_row + 1][start_col + 1] == board[start_row + 2][start_col + 2] != 0:
        return board[start_row][start_col]
    if board[start_row + 2][start_col] == board[start_row + 1][start_col + 1] == board[start_row][start_col + 2] != 0:
        return board[start_row + 2][start_col]

    return 0  # No winner in the small board


def make_move(board, maxDepth, rows=9, cols=9):
    bestScore = -math.inf
    bestMoves = []

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                board[row][col] = 2  # AI move
                score = minimax(board, False, 0, maxDepth, -math.inf, math.inf)
                board[row][col] = 0  # Undo move

                if score > bestScore:
                    bestScore = score
                    bestMoves = [(row, col)]
                elif score == bestScore:
                    bestMoves.append((row, col))

    if bestMoves:
        # Choose randomly among the best moves
        bestMove = random.choice(bestMoves)
        board[bestMove[0]][bestMove[1]] = 2
    return board
