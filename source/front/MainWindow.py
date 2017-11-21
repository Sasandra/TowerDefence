import pygame
from itertools import cycle
from ..back import Button, MonsterB, MonsterG, MonsterR, Game, Wave
from ..front import HelloMenu


class MainWindow:
    def __init__(self):
        monsters_list = [MonsterB.MonsterBlue, MonsterG.MonsterGreen, MonsterR.MonsterRed]
        self.monster_cycle = cycle(monsters_list)

        self.screen = pygame.display.set_mode((1200, 600))
        self.menu_state = True
        self.pause_pressed = False
        self.game = Game.Game()
        self.wave = Wave.Wave(next(self.monster_cycle), self.game, self.screen)

        self.play_button = Button.Button('play', 'play.png', (1110, 520, 50, 46), None, self.screen)

        self.set_window_layout()
        self.set_background()

    def create_wave_if_neccesary(self):
        if self.wave.check_if_wave_end():
            self.wave = Wave.Wave(next(self.monster_cycle), self.game, self.screen)
            self.game.waves += 1
            self.update_texts()

    def set_background(self):
        main_background = pygame.image.load('source\\images\\grass1.png')
        self.screen.blit(main_background, (0, 0))

    def set_window_layout(self):
        self.set_background()

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
        self.show_text(str(self.game.lives), 27, (1002, 8), (255, 255, 255), 'cinnamon-cake')

    def update_wave(self):
        self.read_wave_sign()
        self.show_text(str(self.game.waves), 27, (1002, 32), (255, 255, 255), 'cinnamon-cake')

    def update_gold(self):
        self.read_gold_sign()
        self.show_text(str(self.game.gold), 27, (1002, 71), (255, 255, 255), 'cinnamon-cake')

    def update_texts(self):
        self.update_gold()
        self.update_wave()
        self.update_lives()

    def show_help(self):
        pass

    def hide_help(self):
        pass

    def move_monsters(self):
        self.set_background()
        self.wave.update_positions()
        pygame.display.flip()

    def check_if_game_over(self):
        return self.game.lives <= 0

    def start(self):
        while self.menu_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_state = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.play_button.button.collidepoint(pygame.mouse.get_pos()):
                            self.play_button.on_click()
                            self.pause_pressed = not self.pause_pressed

            if not self.pause_pressed:
                self.move_monsters()

            self.create_wave_if_neccesary()

            if self.check_if_game_over():
                self.menu_state = False
                if HelloMenu.HelloMenu('game_over.png').start() is not None:
                    MainWindow().start()
