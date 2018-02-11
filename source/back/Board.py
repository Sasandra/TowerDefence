import pygame
import copy
from ..texts import constatnts


class Board:
    def __init__(self):
        self.places = []
        self.free_places = []
        self.full_places = []

        self.read_places_from_file()

    def read_places_from_file(self):
        with open(constatnts.TEXTS_PATH + 'towers_board_coordinates.txt', 'r') as r:
            data = r.readlines()
            for line in data:
                line = line.rstrip().split(',')
                for i in range(len(line)):
                    line[i] = int(line[i])

                if line not in self.places:
                    self.places.append(pygame.Rect(line))

        self.free_places = self.places

    def take_place(self, pos, class_name):
        for p in self.free_places:
            if p.collidepoint(pos):
                self.free_places.remove(p)
                self.full_places.append(class_name(p.left, p.top))
                return

    def check_if_place_free(self, pos):
        for p in self.free_places:
            if p.collidepoint(pos):
                return True

        return False

    def take_tower_cost(self, pos):
        for p in self.full_places:
            if p.coordinates.collidepoint(pos):
                class_name = type(p)
                temp = class_name(0, 0)
                return int(0.8 * temp.cost)

        return 0

    def free_place(self, pos):
        for p in self.full_places:
            if p.coordinates.collidepoint(pos):
                temp = copy.deepcopy(p.coordinates)
                self.full_places.remove(p)
                self.free_places.append(temp)