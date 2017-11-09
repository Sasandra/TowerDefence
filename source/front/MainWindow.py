import pygame
import ctypes
from ..back import Button


class MainWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 600))
        self.menu_state = True

        self.play_button = Button.Button('play', 'play.png', (1110, 520, 50, 46), None, self.screen)

        self.set_window_layout()

    def set_window_layout(self):
        main_background = pygame.image.load('source\\images\\grass.png')
        self.screen.blit(main_background, (0, 0))

        side_menu = pygame.image.load('source\\images\\wood1.jpg')
        self.screen.blit(side_menu, (900, 0))

        self.update_lives()
        self.update_wave()
        self.update_gold()

        self.play_button.read_image()

        pygame.display.flip()

    def read_lives_sign(self):
        lives_sign = pygame.image.load('source\\images\\lives_thin.png')
        self.screen.blit(lives_sign, (900, 0))
        pygame.display.flip()

    def read_wave_sign(self):
        wave_sign = pygame.image.load('source\\images\\wave_thin.png')
        self.screen.blit(wave_sign, (900, 32))
        pygame.display.flip()

    def read_gold_sign(self):
        gold_sign = pygame.image.load('source\\images\\gold_thin.png')
        self.screen.blit(gold_sign, (900, 63))
        pygame.display.flip()

    def show_text(self, text, size, coor, color, style):
        pygame.font.init()
        myfont = pygame.font.SysFont(style, size)
        textsurface = myfont.render(text, False, color)
        self.screen.blit(textsurface, coor)

    def update_lives(self):
        self.read_lives_sign()
        self.show_text('16', 27, (1000, 8), (255, 255, 255), 'cinnamon-cake')

    def update_wave(self):
        self.read_wave_sign()
        self.show_text('1', 27, (1000, 32), (255, 255, 255), 'cinnamon-cake')

    def update_gold(self):
        self.read_gold_sign()
        self.show_text('100', 27, (1000, 71), (255, 255, 255), 'cinnamon-cake')

    def show_help(self):
        pass

    def hide_help(self):
        pass

    def start(self):
        while self.menu_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_state = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.play_button.button.collidepoint(pygame.mouse.get_pos()):
                            self.play_button.on_click()


