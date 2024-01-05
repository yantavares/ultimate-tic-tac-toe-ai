import pygame
import sys

if __name__ == "__main__":
    from minimax import make_move
else:
    from NormalGame.minimax import make_move


class NormalGame:
    def __init__(self, max_depth=0):
        pygame.init()
        self.width, self.height = 300, 300
        self.line_width = 15
        self.rows, self.cols = 3, 3
        self.circle_radius, self.circle_width = 40, 15
        self.cross_width, self.cross_size = 20, 30
        self.space = 55
        self.red = (255, 0, 0)
        self.bg_color = (28, 170, 156)
        self.line_color = (23, 145, 135)
        self.circle_color = (239, 231, 200)
        self.cross_color = (66, 66, 66)
        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption('Tic Tac Toe')
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.player = 2
        self.game_count = 0

        self.max_depth = max_depth

    def run(self):
        self.screen.fill(self.bg_color)
        self.draw_lines()
        self.main_loop()

    def draw_lines(self):
        pygame.draw.line(self.screen, self.line_color,
                         (0, 100), (300, 100), self.line_width)
        pygame.draw.line(self.screen, self.line_color,
                         (0, 200), (300, 200), self.line_width)
        pygame.draw.line(self.screen, self.line_color,
                         (100, 0), (100, 300), self.line_width)
        pygame.draw.line(self.screen, self.line_color,
                         (200, 0), (200, 300), self.line_width)

    def draw_figures(self):
        for row in range(self.rows):
            for col in range(self.cols):
                centerX = col * 100 + 50
                centerY = row * 100 + 50
                if self.board[row][col] == 1:
                    pygame.draw.circle(
                        self.screen,
                        self.circle_color,
                        (centerX, centerY),
                        self.circle_radius,
                        self.circle_width)

                elif self.board[row][col] == 2:
                    pygame.draw.line(self.screen,
                                     self.cross_color,
                                     (centerX - self.cross_size,
                                      centerY - self.cross_size),
                                     (centerX + self.cross_size,
                                      centerY + self.cross_size),
                                     self.cross_width)

                    pygame.draw.line(self.screen,
                                     self.cross_color,
                                     (centerX + self.cross_size,
                                      centerY - self.cross_size),
                                     (centerX - self.cross_size,
                                      centerY + self.cross_size),
                                     self.cross_width)

    def draw_winning_line(self, row1, col1, row2, col2):
        pygame.draw.line(self.screen, self.red, (col1 * 100 + 50,
                         row1 * 100 + 50), (col2 * 100 + 50, row2 * 100 + 50), 10)

    def clean_board(self):
        self.screen.fill(self.bg_color)
        self.draw_lines()
        for row in range(self.rows):
            for col in range(self.cols):
                self.board[row][col] = 0

    def check_win_or_tie(self):
        for row in range(self.rows):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != 0:
                self.draw_winning_line(row, 0, row, 2)
                return self.board[row][0]

        for col in range(self.cols):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != 0:
                self.draw_winning_line(0, col, 2, col)
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.draw_winning_line(0, 0, 2, 2)
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.draw_winning_line(0, 2, 2, 0)
            return self.board[0][2]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    return None

        return 0

    def main_loop(self):
        result = None

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    sys.exit()  # TODO make return to menu instead

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                    self.clean_board()
                    result = None
                    self.game_count += 1
                    self.player = 2 if self.game_count % 2 == 0 else 1

                if (event.type == pygame.MOUSEBUTTONDOWN or self.player == 2) and result is None:
                    if self.player == 2:
                        self.board = make_move(self.board, self.max_depth)
                        self.player = 1
                    else:
                        mouseX, mouseY = event.pos[0] // 100, event.pos[1] // 100
                        if self.board[mouseY][mouseX] in [1, 2]:
                            continue
                        if self.player == 1:
                            self.board[mouseY][mouseX] = 1
                            self.player = 2

                    self.draw_figures()
                    result = self.check_win_or_tie()
                    if result is not None and result != 0:
                        print("Press 'R' to restart!")
                    if result == 1:
                        print('Player 1 wins!')
                    elif result == 2:
                        print('AI wins!')
                    elif result == 0:
                        print('Tie!')

                pygame.display.update()


if __name__ == '__main__':
    game = NormalGame()
    game.run()
