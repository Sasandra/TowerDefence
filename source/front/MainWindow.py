import pygame
from itertools import cycle
from ..back import Button, MonsterB, MonsterG, MonsterR, Game, Wave, Board
from ..front import HelloMenu, TowerIcons


class MainWindow:
    def __init__(self):
        monsters_list = [MonsterB.MonsterBlue, MonsterG.MonsterGreen, MonsterR.MonsterRed]
        self.monster_cycle = cycle(monsters_list)
        self.screen = pygame.display.set_mode((1200, 600))

        self.tower_icons = [TowerIcons.RedTowerIcon(self.screen), TowerIcons.GreenTowerIcon(self.screen),
                            TowerIcons.BlueTowerIcon(self.screen)]

        self.menu_state = True
        self.pause_pressed = True
        self.game = Game.Game()
        self.wave = Wave.Wave(next(self.monster_cycle), self.game, self.screen)
        self.board = Board.Board()

        self.play_button = Button.Button('play', 'play.png', (1110, 520, 50, 46), None, self.screen)

        self.set_window_layout()
        self.set_background()
        self.draw_towers_icons()

    def draw_rect_for_towers(self):
        for i in self.board.places:
            pygame.draw.rect(self.screen, (255, 0, 0), i, 1)
            pygame.display.flip()

    def create_wave_if_neccesary(self):
        if self.wave.check_if_wave_end():
            self.wave = Wave.Wave(next(self.monster_cycle), self.game, self.screen)
            self.game.waves += 1
            self.set_stats_note()

    def draw_towers_icons(self):
        for i in self.tower_icons:
            i.draw_icon()

    def check_if_show_tower_desc(self, pos):
        for t in self.tower_icons:
            if t.check_if_collidepoint(pos):
                if t.clicked:
                    self.set_description_note()
                    t.clicked = False
                    return False
                else:
                    t.clicked = True
                    self.change_tower_clicked_value(t)
                    return True

        return False

    def change_tower_clicked_value(self, tower):
        for t in self.tower_icons:
            if t is not tower:
                t.clicked = False

    def get_tower_description(self):
        for t in self.tower_icons:
            if t.clicked:
                return t.class_name(t.coordinates.left, t.coordinates.top).return_description()

    def set_background(self):
        main_background = pygame.image.load('source\\images\\grass.png')
        self.screen.blit(main_background, (0, 0))

    def set_window_layout(self):
        self.set_background()

        side_menu = pygame.image.load('source\\images\\wood.jpg')
        self.screen.blit(side_menu, (900, 0))

        self.play_button.read_image()
        self.set_description_note()
        self.set_stats_note()

        pygame.display.flip()

    def display_tower_desc(self, desc):
        desc = desc.split('\n')
        for i in range(len(desc)):
            self.show_text(desc[i], 18, (980, 250 + i * 20), (0, 0, 0), 'cinnamon-cake')

    def show_text(self, text, size, coor, color, style):
        pygame.font.init()
        myfont = pygame.font.SysFont(style, size)
        textsurface = myfont.render(text, True, color)
        self.screen.blit(textsurface, coor)
        pygame.display.flip()

    def set_description_note(self):
        img = pygame.image.load('source\\images\\note.png')
        self.screen.blit(img, (950, 215))
        pygame.display.flip()

    def set_stats_note(self):
        img = pygame.image.load('source\\images\\note1.png')
        self.screen.blit(img, (970, 5))

        self.show_text('Lives:  ' + str(self.game.lives), 27, (995, 20), (0, 0, 0), 'cinnamon-cake')
        self.show_text('Waves:  ' + str(self.game.waves), 27, (995, 50), (0, 0, 0), 'cinnamon-cake')
        self.show_text('Gold:   ' + str(self.game.gold), 27, (995, 80), (0, 0, 0), 'cinnamon-cake')

        pygame.display.flip()

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

                        if self.check_if_show_tower_desc(pygame.mouse.get_pos()):
                            self.set_description_note()
                            description = self.get_tower_description()
                            self.display_tower_desc(description)

            if not self.pause_pressed:
                self.move_monsters()
            else:
                self.draw_rect_for_towers()

            self.create_wave_if_neccesary()

            if self.check_if_game_over():
                self.menu_state = False
                if HelloMenu.HelloMenu('game_over.png').start() is not None:
                    MainWindow().start()
