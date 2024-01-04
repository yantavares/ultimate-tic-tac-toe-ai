import pygame
from NormalGame.Normal import NormalGame
from UltimateGame.Ultimate import UltimateGame


class Menu:
    def __init__(self):
        pygame.init()
        self.width, self.height = 400, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tic Tac Toe Menu')
        self.bg_color = (28, 170, 156)
        self.button_color = (23, 145, 135)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.normal_button = pygame.Rect(100, 100, 200, 50)
        self.ultimate_button = pygame.Rect(100, 200, 200, 50)
        self.moves_ahead = 3  # Default value

    def run(self):
        running = True
        while running:
            self.screen.fill(self.bg_color)
            self.draw_text('Normal', self.normal_button)
            self.draw_text('Ultimate', self.ultimate_button)
            moves_ahead_rect = pygame.Rect(100, 300, 200, 50)
            self.draw_text('Moves Ahead: ' + str(self.moves_ahead),
                           moves_ahead_rect, center=False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
                    elif event.key == pygame.K_DOWN and self.moves_ahead > 1:
                        self.moves_ahead -= 1

            pygame.display.update()
        pygame.quit()

    def draw_text(self, text, rect, center=True):
        text_surface = self.font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect()
        if center:
            text_rect.center = rect.center
        else:
            text_rect.topleft = rect.topleft
        self.screen.blit(text_surface, text_rect)
        pygame.draw.rect(self.screen, self.button_color, rect, 2)

    def start_game(self, game_class):
        game = game_class(self.moves_ahead)
        game.run()


if __name__ == '__main__':
    menu = Menu()
    menu.run()
