import pygame
import sys
from NormalGame.Normal import NormalGame
from UltimateGame.Ultimate import UltimateGame


class Menu:
    def __init__(self):
        pygame.init()
        self.width, self.height = 500, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tic Tac Toe Menu')
        self.bg_color = (50, 50, 50)
        self.button_color = (70, 130, 180)
        self.button_highlight = (100, 150, 200)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.title_font = pygame.font.SysFont(
            'Arial', 38, bold=True)  # Larger font for the title
        self.normal_button = pygame.Rect((self.width - 200) // 2, 100, 200, 50)
        self.ultimate_button = pygame.Rect(
            (self.width - 200) // 2, 200, 200, 50)
        self.moves_ahead = 3

    def run(self):
        running = True
        while running:
            self.screen.fill(self.bg_color)

            # Draw the title
            title_rect = pygame.Rect(0, 20, self.width, 60)
            self.draw_text('Ultimate Tic-Tac-Toe AI', title_rect,
                           center=True, font_size=48, font=self.title_font)

            self.draw_button(self.normal_button, 'Normal')
            self.draw_button(self.ultimate_button, 'Ultimate')

            instruction_rect = pygame.Rect(
                (self.width - 350) // 2, 350, 360, 30)
            self.draw_text('Use UP/DOWN keys to change depth',
                           instruction_rect, center=False, font_size=20)

            moves_ahead_rect = pygame.Rect(
                (self.width - 260) // 2, 300, 200, 50)

            if self.moves_ahead == 0:
                self.draw_text('Moves Ahead: INF',
                               moves_ahead_rect, center=False)
            else:
                self.draw_text('Moves Ahead: ' + str(self.moves_ahead),
                               moves_ahead_rect, center=False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.normal_button.collidepoint(event.pos):
                        self.start_game(NormalGame)
                        running = False
                    elif self.ultimate_button.collidepoint(event.pos):
                        self.start_game(UltimateGame)
                        running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.moves_ahead += 1
                    elif event.key == pygame.K_DOWN and self.moves_ahead > 0:
                        self.moves_ahead -= 1

            pygame.display.update()

    def draw_button(self, rect, text):
        mouse_pos = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.button_highlight, rect)
        else:
            pygame.draw.rect(self.screen, self.button_color, rect)
        self.draw_text(text, rect)

    def draw_text(self, text, rect, center=True, font_size=36, font=None):
        if font is None:
            font = pygame.font.SysFont('Arial', font_size, bold=True)
        text_surface = font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect()
        if center:
            text_rect.center = rect.center
        else:
            text_rect.topleft = rect.topleft
        self.screen.blit(text_surface, text_rect)

    def start_game(self, game_class):
        game = game_class(self.moves_ahead)
        game.run()
