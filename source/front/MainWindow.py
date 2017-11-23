import pygame
import numpy as np
from itertools import cycle
from ..back import Button, MonsterB, MonsterG, MonsterR, Game, Wave, Board
from ..front import HelloMenu, TowerIcons


class MainWindow:
    def __init__(self):
        monsters_list = [MonsterR.MonsterRed, MonsterG.MonsterGreen, MonsterB.MonsterBlue]
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

        self.clicked_tower = [False, None]
        self.last_shoot_red = pygame.time.get_ticks()
        self.last_shoot_green = pygame.time.get_ticks()
        self.last_shoot_blue = pygame.time.get_ticks()

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
                    self.clicked_tower = [False, None]
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

    def get_tower_icon_class(self, pos):
        for t in self.tower_icons:
            class_name = t.return_class_name(pos)
            if class_name is not None:
                return class_name

    def set_background(self):
        main_background = pygame.image.load('source\\images\\grass.png')
        self.screen.blit(main_background, (0, 0))
        self.draw_towers_on_screen()
        pygame.display.flip()

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

    def reset_memory(self):
        self.set_description_note()
        self.clicked_tower = [False, None]
        for t in self.tower_icons:
            t.clicked = False

    def draw_towers_on_screen(self):
        for t in self.board.full_places:
            self.screen.blit(t.image, (t.x, t.y))

    def condition_if_can_place_tower(self, mouse_pos):
        f_cond = mouse_pos[0] < 900
        s_cond = self.clicked_tower[1] is not None
        t_cond = False
        if s_cond:
            t_cond = self.game.check_gold(self.clicked_tower[1](0, 0).cost)

        return f_cond and s_cond and t_cond

    def calculate_distance_between_tower_and_monster(self, tower, monster):
        tower_pos = np.array((tower.x, tower.y))
        monster_pos = np.array((monster.x, monster.y))
        return np.linalg.norm(tower_pos - monster_pos)

    def calculate_distances_to_monsters_from_one_tower(self, tower):
        monster = None
        distances = []
        for m in self.wave.monsters:
            if m.y > 0:
                dist = self.calculate_distance_between_tower_and_monster(tower, m)
                if dist <= tower.area_radius:
                    distances.append(dist)
                    if dist == min(distances):
                        monster = m

        return monster

    def take_monsters_for_red_towers(self, red_towers):
        now = pygame.time.get_ticks()
        monsters_to_hit = []

        if now - self.last_shoot_red >= red_towers[0].time_period:
            for t in red_towers:
                m = self.calculate_distances_to_monsters_from_one_tower(t)
                if m:
                    monsters_to_hit.append([m, red_towers[0].strength])
            self.last_shoot_red = now

        return monsters_to_hit

    def take_monsters_for_green_towers(self, green_towers):
        now = pygame.time.get_ticks()
        monsters_to_hit = []

        if now - self.last_shoot_green >= green_towers[0].time_period:
            for t in green_towers:
                m = self.calculate_distances_to_monsters_from_one_tower(t)
                if m:
                    monsters_to_hit.append([m, green_towers[0].strength])
            self.last_shoot_green = now

        return monsters_to_hit

    def take_monsters_for_blue_towers(self, blue_towers):
        now = pygame.time.get_ticks()
        monsters_to_hit = []
        if now - self.last_shoot_blue >= blue_towers[0].time_period:
            for t in blue_towers:
                m = self.calculate_distances_to_monsters_from_one_tower(t)
                if m:
                    monsters_to_hit.append([m, blue_towers[0].strength])
            self.last_shoot_blue = now

        return monsters_to_hit

    def calculate_distance_for_all_towers(self):
        monsters_to_hit = []
        red_towers, green_towers, blue_towers = self.split_tower_by_class()

        if red_towers:
            monsters_to_hit += self.take_monsters_for_red_towers(red_towers)

        if green_towers:
            monsters_to_hit += self.take_monsters_for_green_towers(green_towers)

        if blue_towers:
            monsters_to_hit += self.take_monsters_for_blue_towers(blue_towers)

        return monsters_to_hit

    def hit_monsters(self):
        monsters_to_his = self.calculate_distance_for_all_towers()
        for m in monsters_to_his:
            m[0].decrease_health(m[1])

            if m[0].check_health():
                print(m[0])
                self.monster_killed(m[0])

    def monster_killed(self, monster):
        self.wave.monsters.remove(monster)
        self.game.increase_gold(monster.prize)
        self.set_stats_note()
        pygame.display.flip()

    def split_tower_by_class(self):
        red = []
        green = []
        blue = []
        for t in self.board.full_places:
            if 'TowerRed' in str(type(t)):
                red.append(t)
            elif 'TowerGreen' in str(type(t)):
                green.append(t)
            elif 'TowerBlue' in str(type(t)):
                blue.append(t)

        return red, green, blue

    def start(self):
        while self.menu_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_state = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        if self.play_button.button.collidepoint(mouse_pos):
                            self.play_button.on_click()
                            self.pause_pressed = not self.pause_pressed

                        if self.check_if_show_tower_desc(mouse_pos):
                            self.set_description_note()
                            description = self.get_tower_description()
                            self.display_tower_desc(description)
                            self.clicked_tower = [True, self.get_tower_icon_class(mouse_pos)]

                        if self.condition_if_can_place_tower(mouse_pos):
                            if self.board.check_if_place_free(mouse_pos):
                                if self.clicked_tower[0]:
                                    self.board.take_place(mouse_pos, self.clicked_tower[1])
                                    self.game.decrease_gold(self.clicked_tower[1](0, 0).cost)
                                    self.set_stats_note()
                                    self.reset_memory()
                                    self.set_background()
                                    pygame.display.flip()

                            else:
                                self.reset_memory()

                    elif event.button == 3:
                        self.reset_memory()

            if not self.pause_pressed:
                self.move_monsters()
                self.hit_monsters()

                if len(self.wave.monsters) != 10:
                    self.set_stats_note()
                    pygame.display.flip()
            else:
                self.draw_rect_for_towers()

            self.create_wave_if_neccesary()

            if self.check_if_game_over():
                self.menu_state = False
                if HelloMenu.HelloMenu('game_over.png').start() is not None:
                    MainWindow().start()
