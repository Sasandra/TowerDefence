import random
import pygame
from ..texts import constatnts

opposite = {
    'left': 'right',
    'right': 'left',
    'up': 'down',
    'down': 'up'
}


class Wave:
    def __init__(self, monster, game_, screen_):
        self.monsters = []
        self.game = game_
        self.screen = screen_
        self.level_up_counter = -1
        self.wave_counter = 0
        self.road = ["empty"]
        self.point = None
        self.fill_monsters(monster)

    def read_points(self):
        points = {}
        with open(constatnts.TEXTS_PATH + 'start_points.txt', 'r') as r:
            data = r.readlines()
            for line in data:
                line_splited = line.rstrip().split(':')
                number_pair = line_splited[1].strip('()').split(',')
                number_pair = (int(number_pair[0]), int(number_pair[1]))
                direction_pair = line_splited[0].strip('()').split(',')
                direction_pair = (direction_pair[0], direction_pair[1])

                points.update({direction_pair: number_pair})

        return points

    def random_point(self):
        points = self.read_points()
        key = random.choice(list(points))
        self.point = {key: points[key]}

    def create_possible_roads(self):
        roads = []
        temp_roads = []
        point = list(self.point.keys())[0]
        roads.append([point[0], point[1], opposite[point[0]], opposite[point[0]]])
        roads.append([point[0], point[1], opposite[point[0]], point[1]])
        roads.append([point[1], point[0], opposite[point[1]], opposite[point[1]]])
        roads.append([point[1], point[0], opposite[point[1]], point[0]])

        for i in roads:
            if i[-1] != 'right':
                temp_roads.append(i)
            elif point[0] == 'down' and i[0] != 'right':
                temp_roads.append(i)
            elif point[0] == 'down' and i[1] != 'right':
                temp_roads.append(i)

        return temp_roads

    def random_road(self):
        roads = self.create_possible_roads()
        self.road = random.choice(roads)

    def fill_monsters(self, monster):
        self.wave_counter += 1
        self.random_point()
        self.random_road()

        point_x = list(self.point.values())[0][0]
        point_y = list(self.point.values())[0][1]
        point_direction = list(self.point.keys())[0][0]

        if point_direction == 'down':
            for i in range(1, constatnts.WAVE_LENGTH + 1):
                self.monsters.append(monster(point_x, point_y - 30 * i, point_direction))

        elif point_direction == 'up':
            for i in range(1, constatnts.WAVE_LENGTH + 1):
                self.monsters.append(monster(point_x, point_y + 30 * i, point_direction))

        elif point_direction == 'right':
            for i in range(1, constatnts.WAVE_LENGTH + 1):
                self.monsters.append(monster(point_x - 30 * i, point_y, point_direction))

        self.level_up_monsters()

    def level_up_monsters(self):
        if self.wave_counter % 3 == 1:
            self.level_up_counter += 1

        for i in range(self.level_up_counter):
            for m in self.monsters:
                m.level_up()
                print(m.health)

    def update_wave(self):
        temp_list = []
        for m in self.monsters:
            if m.check_health():
                self.game.increase_gold(m.prize)
            else:
                temp_list.append(m)

        self.monsters = temp_list

    def check_if_wave_end(self):
        if len(self.monsters) == 0:
            return True
        else:
            return False

    def check_if_monster_out_of_board(self, monster):
        left_edge = monster.x < -44 and monster.direction == 'left'
        top_edge = monster.y < -44 and monster.direction == 'up'
        down_edge = monster.y > 626 and monster.direction == 'down'

        return left_edge or top_edge or down_edge

    def check_if_all_monster_has_same_direction(self):
        dir = self.monsters[0].direction
        for m in self.monsters:
            if m.direction != dir:
                return False

        return True

    def check_if_last_monster(self, monster):
        length = len(self.monsters)
        index = self.monsters.index(monster)

        return (length - 1) == index

    def update_positions(self):

        point_1 = pygame.Rect(185, 440, 5, 5)
        point_2 = pygame.Rect(185, 155, 5, 5)
        point_3 = pygame.Rect(705, 440, 5, 5)
        point_4 = pygame.Rect(705, 155, 5, 5)

        last_monster_collision = False
        print(self.road)

        for m in self.monsters:
            if m.direction == 'down':
                m.y += m.speed

            elif m.direction == 'up':
                m.y -= m.speed

            elif m.direction == 'left':
                m.x -= m.speed

            elif m.direction == 'right':
                m.x += m.speed

            m.update_coordinates(m.x, m.y)
            print(m.coordinates.center)
            center_x = m.coordinates.center[0]
            center_y = m.coordinates.center[1]

            # if 173 < m.x < 178 and 433 < m.y < 438:
            #     m.direction = self.road[0]
            #
            #     if self.check_if_last_monster(m):
            #         print(len(self.monsters))
            #         print(self.monsters.index(m))
            #         last_monster_collision = True
            #
            # elif 173 < m.x < 178 and 142 < m.y < 147:
            #     m.direction = self.road[0]
            #
            #     if self.check_if_last_monster(m):
            #         print(len(self.monsters))
            #         print(self.monsters.index(m))
            #         last_monster_collision = True
            #
            # elif 695 < m.x < 698 and 432 < m.y < 436:
            #     m.direction = self.road[0]
            #
            #     if self.check_if_last_monster(m):
            #         print(len(self.monsters))
            #         print(self.monsters.index(m))
            #         last_monster_collision = True
            #
            # elif 695 < m.x < 698 and 140 < m.y < 144:
            #     m.direction = self.road[0]
            #
            #     if self.check_if_last_monster(m):
            #         print(len(self.monsters))
            #         print(self.monsters.index(m))
            #         last_monster_collision = True

            if 186 < center_x < 189 and 156 < center_y < 159:
                m.direction = self.road[0]

                if self.check_if_last_monster(m):
                    print(len(self.monsters))
                    print(self.monsters.index(m))
                    last_monster_collision = True

            elif 707 < center_x < 710 and 156 < center_y < 159:
                m.direction = self.road[0]

                if self.check_if_last_monster(m):
                    print(len(self.monsters))
                    print(self.monsters.index(m))
                    last_monster_collision = True

            elif 186 < center_x < 190 and 441 < center_y < 444:
                m.direction = self.road[0]

                if self.check_if_last_monster(m):
                    print(len(self.monsters))
                    print(self.monsters.index(m))
                    last_monster_collision = True

            elif 707 < center_x < 710 and 441 < center_y < 444:
                m.direction = self.road[0]

                if self.check_if_last_monster(m):
                    print(len(self.monsters))
                    print(self.monsters.index(m))
                    last_monster_collision = True

            m.change_direction_image()
            self.screen.blit(m.image, (m.x, m.y))

            if self.check_if_monster_out_of_board(m):
                print('dead!')
                self.monsters.remove(m)
                self.game.decrease_lives()

        if last_monster_collision:
            self.road.pop(0)
