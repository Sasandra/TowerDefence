import pygame
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
