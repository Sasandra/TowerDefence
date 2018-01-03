import pygame, os
import numpy as np
from itertools import cycle
from ..back import Button, MonsterB, MonsterG, MonsterR, Game, Wave, Board
from ..front import HelloMenu, TowerIcons
from ..texts import constatnts

os.environ['SDL_VIDEO_CENTERED'] = '1'


class MainWindow:
    def __init__(self):
        monsters_list = [MonsterR.MonsterRed, MonsterG.MonsterGreen, MonsterB.MonsterBlue]
        self.monster_cycle = cycle(monsters_list)
        self.screen = pygame.display.set_mode(constatnts.MAIN_WINDOW_SCREEN_SIZE)

        self.tower_icons = [TowerIcons.RedTowerIcon(self.screen), TowerIcons.GreenTowerIcon(self.screen),
                            TowerIcons.BlueTowerIcon(self.screen)]

        self.menu_state = True
        self.pause_pressed = True
        self.game = Game.Game()
        self.wave = Wave.Wave(next(self.monster_cycle), self.game, self.screen)
        self.board = Board.Board()

        self.play_button = Button.Button('play', constatnts.MAIN_WINDOW_PLAY_BUTTON_IMAGE,
                                         constatnts.MAIN_WINDOW_PLAY_BUTTON_RECT, None, self.screen)

        self.set_original_background()
        self.set_window_layout()
        self.set_background()
        self.draw_towers_icons()
        self.set_road()

        self.clicked_tower = [False, None]
        self.clicked_monster = [False, None]
        self.last_shoot_red = pygame.time.get_ticks()
        self.last_shoot_green = pygame.time.get_ticks()
        self.last_shoot_blue = pygame.time.get_ticks()
        self.last_monster_update = pygame.time.get_ticks()

    def set_window_layout(self):
        side_menu = pygame.image.load(constatnts.IMAGES_PATH + constatnts.MAIN_WINDOW_SIDE_MENU_IMAGE)
        self.screen.blit(side_menu, constatnts.MAIN_WINDOW_SIDE_MENU_BLIT)

        self.play_button.read_image()
        self.set_description_note()
        self.set_stats_note()

        pygame.display.flip()

    def set_original_background(self):
        main_background = pygame.image.load(constatnts.IMAGES_PATH + constatnts.MAIN_WINDOW_BACKGROUND_ORIGINAL_IMAGE)
        self.screen.blit(main_background, constatnts.MAIN_WINDOW_BACKGROUND_ORIGINAL_IMAGE_BLIT)
        pygame.display.flip()

    def set_background(self):
        main_background = pygame.image.load(constatnts.IMAGES_PATH + constatnts.MAIN_WINDOW_BACKGROUND_IMAGE)
        self.screen.blit(main_background, constatnts.MAIN_WINDOW_BACKGROUND_IMAGE_BLIT)
        pygame.display.flip()

    def set_road(self):
        road = pygame.image.load(constatnts.IMAGES_PATH + constatnts.MAIN_WINDOW_ROAD_IMAGE)
        self.screen.blit(road, constatnts.MAIN_WINDOW_ROAD_BLIT)
        pygame.display.flip()

    def draw_towers_icons(self):
        for i in self.tower_icons:
            i.draw_icon()

    def set_description_note(self):
        img = pygame.image.load(constatnts.IMAGES_PATH + constatnts.MAIN_MENU_DESCRIPTION_NOTE_IMAGE)
        self.screen.blit(img, constatnts.MAIN_MENU_DESCRIPTION_NOTE_IMAGE_BLIT)
        pygame.display.flip()

    def set_stats_note(self):
        img = pygame.image.load(constatnts.IMAGES_PATH + constatnts.MAIN_MENU_STATS_NOTE_IMAGE)
        self.screen.blit(img, constatnts.MAIN_MENU_STATS_NOTE_IMAGE_BLIT)

        self.show_text('Lives:  ' + str(self.game.lives), constatnts.MAIN_WINDOW_STATS_FONT_SIZE,
                       constatnts.MAIN_WINDOW_STATS_LIVES, constatnts.MAIN_WINDOW_STATS_FONT_COLOR,
                       constatnts.MAIN_WINDOW_STATS_FONT_FAMILY)
        self.show_text('Waves:  ' + str(self.game.waves), constatnts.MAIN_WINDOW_STATS_FONT_SIZE,
                       constatnts.MAIN_WINDOW_STATS_WAVES, constatnts.MAIN_WINDOW_STATS_FONT_COLOR,
                       constatnts.MAIN_WINDOW_STATS_FONT_FAMILY)
        self.show_text('Gold:   ' + str(self.game.gold), constatnts.MAIN_WINDOW_STATS_FONT_SIZE,
                       constatnts.MAIN_WINDOW_STATS_GOLD, constatnts.MAIN_WINDOW_STATS_FONT_COLOR,
                       constatnts.MAIN_WINDOW_STATS_FONT_FAMILY)

        pygame.display.flip()

    def draw_towers_on_screen(self):
        for t in self.board.full_places:
            self.screen.blit(t.image, (t.x, t.y))

    def draw_rect_for_towers(self):
        for i in self.board.places:
            pygame.draw.rect(self.screen, constatnts.MAIN_WINDOW_PLACES_FOR_TOWERS_COLOR, i, 1)
            pygame.display.flip()

        pygame.display.flip()

    def show_text(self, text, size, coor, color, style):
        pygame.font.init()
        myfont = pygame.font.SysFont(style, size)
        textsurface = myfont.render(text, True, color)
        self.screen.blit(textsurface, coor)
        pygame.display.flip()

    def create_wave_if_neccesary(self):
        if self.wave.check_if_wave_end():
            self.wave.fill_monsters(next(self.monster_cycle))
            self.game.waves += 1
            self.set_stats_note()

    def check_if_show_monster_desc(self, pos):
        for m in self.wave.monsters:
            if m.check_if_collidepoint(pos):

                self.clicked_tower = [False, None]
                self.change_tower_clicked_value(None)

                if m.clicked:
                    self.set_description_note()
                    m.clicked = False
                    self.clicked_monster = [False, None]
                    return False
                else:
                    m.clicked = True
                    self.change_monster_clicked_value(m)
                    return True

        return False

    def check_if_show_tower_desc(self, pos):
        for t in self.tower_icons:
            if t.check_if_collidepoint(pos):

                self.clicked_monster = [False, None]
                self.change_monster_clicked_value(None)

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

    def check_if_game_over(self):
        return self.game.lives <= 0

    def change_tower_clicked_value(self, tower):
        for t in self.tower_icons:
            if t is not tower:
                t.clicked = False

    def change_monster_clicked_value(self, monster):
        for m in self.wave.monsters:
            if m is not monster:
                m.clicked = False

    def get_tower_description(self):
        for t in self.tower_icons:
            if t.clicked:
                return t.class_name(t.coordinates.left, t.coordinates.top).return_description()

    def get_monster_description_and_type(self):
        for m in self.wave.monsters:
            if m.clicked:
                return m.return_description(), m

    def get_tower_icon_class(self, pos):
        for t in self.tower_icons:
            class_name = t.return_class_name(pos)
            if class_name is not None:
                return class_name

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

    def display_desc(self, desc):
        desc = desc.split('\n')
        for i in range(len(desc)):
            self.show_text(desc[i], constatnts.MAIN_WINDOWS_DESCRIPTION_FONT_SIZE,
                           (constatnts.MAIN_WINDOWS_DESCRIPTION_X, constatnts.MAIN_WINDOWS_DESCRIPTION_Y + i * 20),
                           constatnts.MAIN_WINDOWS_DESCRIPTION_FONT_COLOR,
                           constatnts.MAIN_WINDOWS_DESCRIPTION_FONT_FAMILY)

    def move_monsters(self):
        now = pygame.time.get_ticks()

        if now - self.last_monster_update >= constatnts.MAIN_WINDOW_REFRESH_PERIOD:
            # self.set_road()
            self.wave.update_positions()
            pygame.display.flip()
            self.last_monster_update = now

    def reset_memory(self):
        self.set_description_note()
        self.clicked_tower = [False, None]
        self.clicked_monster = [False, None]
        for t in self.tower_icons:
            t.clicked = False
        for m in self.wave.monsters:
            m.clicked = False

    def condition_if_can_place_tower(self, mouse_pos):
        f_cond = mouse_pos[0] < constatnts.MAIN_WINDOW_SIDE_MENU_BLIT[0]
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
                dist = self.calculate_distance_between_tower_and_monster(tower, m)
                if dist <= tower.area_radius:
                    distances.append(dist)
                    if dist == min(distances):
                        monster = m

        return monster

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
            if m[0].clicked:
                self.set_monster_desc()

            m[0].decrease_health(m[1])
            m[0].change_health_level()
            m[0].change_image()

            if m[0].check_health():
                self.monster_killed(m[0])
                self.wave.update_positions()

    def monster_killed(self, monster):
        if monster.clicked:
            self.clicked_monster = [False, None]
            self.set_description_note()
        if monster in self.wave.monsters:
            print(monster.x, monster.y)
            image = pygame.image.load(constatnts.IMAGES_PATH + 'empty.png')
            self.screen.blit(image, (monster.x, monster.y))
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

    def draw_monsters_after_place_tower(self):
        for m in self.wave.monsters:
            self.screen.blit(m.image, (m.x, m.y))

    def set_monster_desc(self):
        self.set_description_note()
        description, monster = self.get_monster_description_and_type()
        self.display_desc(description)
        self.clicked_monster = [True, monster]

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
                            self.display_desc(description)
                            self.clicked_tower = [True, self.get_tower_icon_class(mouse_pos)]

                        if self.check_if_show_monster_desc(mouse_pos):
                            self.set_monster_desc()

                        if self.condition_if_can_place_tower(mouse_pos):
                            if self.board.check_if_place_free(mouse_pos):
                                if self.clicked_tower[0]:
                                    self.board.take_place(mouse_pos, self.clicked_tower[1])
                                    self.game.decrease_gold(self.clicked_tower[1](0, 0).cost)
                                    self.set_stats_note()
                                    self.reset_memory()
                                    self.set_background()
                                    self.set_road()
                                    self.draw_towers_on_screen()
                                    pygame.display.flip()

                            else:
                                self.reset_memory()

                    elif event.button == 3:
                        self.reset_memory()

                        if not self.board.check_if_place_free(mouse_pos):
                            cost = self.board.take_tower_cost(mouse_pos)
                            print('cost', cost)
                            if cost != 0:
                                self.game.increase_gold(cost)
                                self.set_stats_note()
                                self.board.free_place(mouse_pos)
                                self.set_background()
                                self.set_road()
                                self.draw_towers_on_screen()

            if not self.pause_pressed:
                self.move_monsters()
                self.hit_monsters()
            # else:
            #    self.draw_rect_for_towers()

            self.create_wave_if_neccesary()

            if self.check_if_game_over():
                self.menu_state = False
                if HelloMenu.HelloMenu(constatnts.HELLO_MENU_GAME_OVER_IMAGE).start() is not None:
                    MainWindow().start()
