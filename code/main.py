import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('The Lord')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # load icon
        new_icon = pygame.image.load('../graphics/icon.png')
        pygame.display.set_icon(new_icon)

        # load music
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.play(loops= -1 )
        main_sound.set_volume(0.5)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:  # m --> menu
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)  # rellena el mapa de agua para que no haya negro
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
