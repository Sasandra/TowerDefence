import pygame


class Board:
    def __init__(self):
        self.places = []
        self.free_places = []
        self.full_places = []

        self.read_places_from_file()

    def read_places_from_file(self):
        with open('source\\texts\\towers_board_coordinates.txt', 'r') as r:
            data = r.readlines()
            for line in data:
                line = line.rstrip().split(',')
                for i in range(len(line)):
                    line[i] = int(line[i])

                if line not in self.places:
                    self.places.append(pygame.Rect(line))

        self.free_places = self.places

    def take_place(self, pos):
        for p in self.free_places:
            if (p.left, p.top) == pos:
                self.free_places.remove(p)
                self.full_places.append(p)
                return

    def check_if_place_free(self, pos):
        for p in self.free_places:
            if (p.left, p.top) == pos:
                return True

        return False
    