import pygame
import sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('IronHeart')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # load icon
        new_icon = pygame.image.load('../graphics/icon.png')
        pygame.display.set_icon(new_icon)

        # load music
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.play(loops=-1)
        main_sound.set_volume(0.5)

        # load background image
        self.background_image = pygame.image.load('../graphics/tilemap/background.jpg')

        # Menu setup
        self.is_in_menu = True
        self.menu_font = pygame.font.Font(None, 50)
        self.menu_font_title = pygame.font.Font("../graphics/font/font.ttf", 70)
        self.start_button = pygame.Rect(
            self.screen.get_width() // 2 - 100,
            self.screen.get_height() // 2 - 50,
            200,
            50
        )
        self.quit_button = pygame.Rect(
            self.screen.get_width() // 2 - 100,
            self.screen.get_height() // 2 + 50,
            200,
            50
        )

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # p --> main_menu
                        self.is_in_menu = not self.is_in_menu
                    if event.key == pygame.K_m:  # m --> upgrade_menu
                        self.level.toggle_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        if self.start_button.collidepoint(event.pos):
                            self.start_game()
                        elif self.quit_button.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

            if self.is_in_menu:
                self.draw_menu()
            else:
                self.screen.fill(WATER_COLOR)  # Fill the screen with water color
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)

    def draw_menu(self):
        self.screen.blit(pygame.transform.scale(self.background_image, (WIDTH, HEIGTH)), (0, 0))
        start_text = self.menu_font.render("Iniciar", True, TEXT_COLOR_SELECTED)
        quit_text = self.menu_font.render("Salir", True, TEXT_COLOR_SELECTED)
        pygame.draw.rect(self.screen, TEXT_COLOR, self.start_button)
        pygame.draw.rect(self.screen, TEXT_COLOR, self.quit_button)
        self.screen.blit(start_text, (self.start_button.x + 10, self.start_button.y + 10))
        self.screen.blit(quit_text, (self.quit_button.x + 10, self.quit_button.y + 10))

        # Texto centrado
        welcome_text = self.menu_font_title.render("Menú Principal", True, "#b68f40")
        text_rect = welcome_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 200))
        self.screen.blit(welcome_text, text_rect)
        pygame.display.update()

    def start_game(self):
        self.is_in_menu = False


if __name__ == '__main__':
    game = Game()
    game.run()
