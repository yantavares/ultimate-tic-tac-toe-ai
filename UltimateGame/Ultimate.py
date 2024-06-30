import pygame
import sys

if __name__ == "__main__":
    from minimax import make_move
else:
    from UltimateGame.minimax import make_move


class UltimateGame:
    def __init__(self, max_depth=3):
        pygame.init()
        self.width, self.height = 600, 600
        self.line_width = 2
        self.rows, self.cols = 9, 9
        self.cell_size = self.width // self.cols
        self.bg_color = (28, 170, 156)
        self.line_color = (23, 145, 135)
        self.winning_symbol_color = (255, 0, 0)
        self.main_line_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Ultimate Tic Tac Toe')
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.player = 1  # Player 1 starts (represented by 1, player 2 by 2)

        self.is_thinking = False

        self.max_depth = max_depth
        self.locked_locations = []

        self.result_small_boards = [[0 for _ in range(3)] for _ in range(3)]
        self.game_over = False

    def run(self):
        self.screen.fill(self.bg_color)
        self.draw_lines()
        print("Moves ahead:", self.max_depth)
        self.main_loop()

    def draw_lines(self):
        # Drawing the grid lines for the ultimate tic-tac-toe board
        for row in range(1, self.rows):
            line_width = self.line_width if row % 3 else 7
            line_color = self.line_color if row % 3 else self.main_line_color
            pygame.draw.line(self.screen, line_color, (0, self.cell_size * row),
                             (self.width, self.cell_size * row), line_width)

        for col in range(1, self.cols):
            line_width = self.line_width if col % 3 else 7
            line_color = self.line_color if col % 3 else self.main_line_color
            pygame.draw.line(self.screen, line_color, (self.cell_size * col, 0),
                             (self.cell_size * col, self.height), line_width)

    def draw_figures(self):
        for row in range(self.rows):
            for col in range(self.cols):
                centerX = col * self.cell_size + self.cell_size // 2
                centerY = row * self.cell_size + self.cell_size // 2
                if self.board[row][col] == 1:  # Player 1 (X)
                    pygame.draw.line(self.screen, self.main_line_color,
                                     (centerX - 20, centerY - 20),
                                     (centerX + 20, centerY + 20), self.line_width)
                    pygame.draw.line(self.screen, self.main_line_color,
                                     (centerX + 20, centerY - 20),
                                     (centerX - 20, centerY + 20), self.line_width)
                elif self.board[row][col] == 2:  # Player 2 (O)
                    pygame.draw.circle(self.screen, self.main_line_color,
                                       (centerX, centerY), 20, self.line_width)

    def check_win_or_tie_small_board(self, first_row, first_col):
        # Check for a win in the small board
        for row in range(first_row, first_row + 3):
            if self.board[row][first_col] == self.board[row][first_col + 1] == self.board[row][first_col + 2] != 0:

                return self.board[row][first_col]

        for col in range(first_col, first_col + 3):
            if self.board[first_row][col] == self.board[first_row + 1][col] == self.board[first_row + 2][col] != 0:

                return self.board[first_row][col]

        if self.board[first_row][first_col] == self.board[first_row + 1][first_col + 1] == self.board[first_row + 2][
                first_col + 2] != 0:

            return self.board[first_row][first_col]

        if self.board[first_row + 2][first_col] == self.board[first_row + 1][first_col + 1] == self.board[first_row][
                first_col + 2] != 0:

            return self.board[first_row + 2][first_col]

        # Check for a tie in the small board
        for row in range(first_row, first_row + 3):
            for col in range(first_col, first_col + 3):
                if self.board[row][col] == 0:
                    return None

        return 0

    def draw_winning_symbol_on_small_board(self, row, col, winner):
        first_row = row * 3
        first_col = col * 3
        centerX = first_col * self.cell_size + 1.5 * self.cell_size
        centerY = first_row * self.cell_size + 1.5 * self.cell_size

        if winner == 1:  # Player 1 (X)
            pygame.draw.line(self.screen, self.winning_symbol_color,
                             (centerX - 50, centerY - 50),
                             (centerX + 50, centerY + 50), self.line_width)
            pygame.draw.line(self.screen, self.winning_symbol_color,
                             (centerX + 50, centerY - 50),
                             (centerX - 50, centerY + 50), self.line_width)
        elif winner == 2:  # Player 2 (O)
            pygame.draw.circle(self.screen, self.winning_symbol_color,
                               (int(centerX), int(centerY)), 50, self.line_width)

    def update_small_boards(self):
        for i in range(3):
            for j in range(3):
                first_row = i * 3
                first_col = j * 3
                winner = self.check_win_or_tie_small_board(
                    first_row, first_col)
                if winner is not None:
                    self.result_small_boards[i][j] = winner

                    # Lock the locations of the won small board
                    for row in range(first_row, first_row + 3):
                        for col in range(first_col, first_col + 3):
                            if (row, col) not in self.locked_locations:
                                self.locked_locations.append((row, col))

                    # Draw the winning symbol on the won small board
                    self.draw_winning_symbol_on_small_board(i, j, winner)

    def draw_winning_line(self, row1, col1, row2, col2):
        start_x = col1 * 3 * self.cell_size + 1.5 * self.cell_size
        start_y = row1 * 3 * self.cell_size + 1.5 * self.cell_size
        end_x = col2 * 3 * self.cell_size + 1.5 * self.cell_size
        end_y = row2 * 3 * self.cell_size + 1.5 * self.cell_size
        pygame.draw.line(self.screen, self.main_line_color,
                         (start_x, start_y), (end_x, end_y), 10)

    def check_win_or_tie(self):
        for row in range(3):  # Iterate over 3 rows instead of self.rows
            if self.result_small_boards[row][0] == self.result_small_boards[row][1] == self.result_small_boards[row][2] != 0:
                self.draw_winning_line(row, 0, row, 2)
                self.game_over = True
                return self.result_small_boards[row][0]

        for col in range(3):  # Iterate over 3 columns instead of self.cols
            if self.result_small_boards[0][col] == self.result_small_boards[1][col] == self.result_small_boards[2][col] != 0:
                self.draw_winning_line(0, col, 2, col)
                self.game_over = True
                return self.result_small_boards[0][col]

        if self.result_small_boards[0][0] == self.result_small_boards[1][1] == self.result_small_boards[2][2] != 0:
            self.draw_winning_line(0, 0, 2, 2)
            self.game_over = True
            return self.result_small_boards[0][0]

        if self.result_small_boards[0][2] == self.result_small_boards[1][1] == self.result_small_boards[2][0] != 0:
            self.draw_winning_line(0, 2, 2, 0)
            self.game_over = True
            return self.result_small_boards[0][2]

        # Check for a tie
        for row in range(3):
            for col in range(3):
                if self.result_small_boards[row][col] == 0:
                    return None

        self.game_over = True
        return 0

    def main_loop(self):
        while True:
            event = None
            # Process all available events and keep only the latest
            for e in pygame.event.get():
                event = e

            if event:
                if event.type == pygame.QUIT:
                    sys.exit()

                if self.is_thinking:
                    continue  # Skip processing any events if AI is thinking

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()  # Exit the game
                    elif event.key == pygame.K_r:  # Restart game
                        self.reset_game()

                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over and self.player == 1:
                    mouseX, mouseY = event.pos
                    clicked_row = mouseY // self.cell_size
                    clicked_col = mouseX // self.cell_size
                    if self.board[clicked_row][clicked_col] == 0 and (clicked_row, clicked_col) not in self.locked_locations:
                        self.board[clicked_row][clicked_col] = self.player
                        self.player = 2

                    self.draw_figures()

                if self.player == 2 and not self.game_over and not self.is_thinking:
                    self.is_thinking = True
                    print("Thinking...")
                    self.board = make_move(self.board, self.max_depth, self.locked_locations)
                    self.player = 1
                    self.draw_figures()
                    self.is_thinking = False

            if self.game_over:
                self.update_small_boards()
                result = self.check_win_or_tie()
                if result is not None and not hasattr(self, 'message_shown'):
                    print("Game result:", "Tie!" if result == 0 else "Player wins!" if result == 1 else "AI wins!")
                    setattr(self, 'message_shown', True)  # Set flag to indicate message has been shown
            else:
                self.check_win_or_tie()
                self.update_small_boards()
                if hasattr(self, 'message_shown'):
                    delattr(self, 'message_shown')  # Reset the flag when the game is not over

            pygame.display.update()


if __name__ == '__main__':
    game = UltimateGame()
    game.run()
