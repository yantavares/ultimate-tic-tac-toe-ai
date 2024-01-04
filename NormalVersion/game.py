import pygame
import sys
from minimax import makeMove

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 40
CIRCLE_WIDTH = 15
CROSS_WIDTH = 20
CROSS_SIZE = 30
SPACE = 55

# Colors
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Board
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Draw lines


def draw_lines():
    # Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)

    # Vertical
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            centerX = col * 100 + 50
            centerY = row * 100 + 50

            if board[row][col] == 1:
                pygame.draw.circle(
                    screen, CIRCLE_COLOR, (centerX, centerY), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                # Draw first line of the cross (top-left to bottom-right)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (centerX - CROSS_SIZE,
                                  centerY - CROSS_SIZE),
                                 (centerX + CROSS_SIZE, centerY + CROSS_SIZE), CROSS_WIDTH)
                # Draw second line of the cross (top-right to bottom-left)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (centerX + CROSS_SIZE,
                                  centerY - CROSS_SIZE),
                                 (centerX - CROSS_SIZE, centerY + CROSS_SIZE), CROSS_WIDTH)


def draw_winning_line(row1, col1, row2, col2):
    pygame.draw.line(screen, RED, (col1 * 100 + 50, row1 *
                     100 + 50), (col2 * 100 + 50, row2 * 100 + 50), 10)


def clean_board():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


def check_win_or_tie(board):
    # Check rows
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            draw_winning_line(row, 0, row, 2)
            return board[row][0]

    # Check columns
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            draw_winning_line(0, col, 2, col)
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        draw_winning_line(0, 0, 2, 2)
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != 0:
        draw_winning_line(0, 2, 2, 0)
        return board[0][2]

    # Check tie
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return None

    return 0


def main():
    global board

    result = None

    draw_lines()
    player = 2

    game_count = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                sys.exit()

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                clean_board()
                result = None
                game_count += 1

                if game_count % 2 == 0:
                    player = 2
                else:
                    player = 1

            if (event.type == pygame.MOUSEBUTTONDOWN or player == 2) and result == None:

                if player == 2:
                    board = makeMove(board, result)
                    player = 1

                else:
                    mouseX = event.pos[0] // 100
                    mouseY = event.pos[1] // 100

                    if board[mouseY][mouseX] == 1 or board[mouseY][mouseX] == 2:
                        continue

                    if player == 1:
                        board[mouseY][mouseX] = 1
                        player = 2

                draw_figures()

                result = check_win_or_tie(board)
                if result != 0 and result != None:
                    print("Press 'R' to restart!")
                if result == 1:
                    print('Player 1 wins!')
                elif result == 2:
                    print('AI wins!')
                elif result == 0:
                    print('Tie!')

        pygame.display.update()


if __name__ == '__main__':
    main()
