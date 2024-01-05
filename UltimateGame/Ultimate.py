import pygame
import sys


class UltimateGame:
    def __init__(self, max_depth=-1):
        pygame.init()
        self.width, self.height = 600, 600
        self.line_width = 2
        self.rows, self.cols = 9, 9
        self.cell_size = self.width // self.cols
        self.bg_color = (28, 170, 156)
        self.line_color = (23, 145, 135)
        self.main_line_color = (0, 0, 0)  # Black color for main lines
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Ultimate Tic Tac Toe')
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.player = 1  # Player 1 starts (represented by 1, player 2 by 2)

    def run(self):
        self.screen.fill(self.bg_color)
        self.draw_lines()
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

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit()  # Replace with logic to return to menu later

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    clicked_row = mouseY // self.cell_size
                    clicked_col = mouseX // self.cell_size
                    if self.board[clicked_row][clicked_col] == 0:
                        self.board[clicked_row][clicked_col] = self.player
                        self.player = 3 - self.player  # Switch player

                    self.draw_figures()

                # Additional game logic goes here

            pygame.display.update()


if __name__ == '__main__':
    game = UltimateGame()
    game.run()
