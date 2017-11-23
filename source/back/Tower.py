import pygame


class Tower:
    def __init__(self, strength_, area_, cost_, image_, x_, y_, time_):
        self.strength = strength_
        self.area_radius = area_
        self.level = 1
        self.cost = cost_
        self.image = pygame.image.load('source\\images\\' + image_)
        self.x = x_
        self.y = y_
        self.coordinates = pygame.Rect(x_, y_, 24, 24)
        self.time_period = time_

    def check_level(self):
        return self.level <= 5

    def level_up(self):
        self.area_radius *= 1.5
        self.strength *= 1.5
        self.cost *= 1.5

    def check_if_collidepoint(self, pos):
        return self.coordinates.collidepoint(pos)

    def return_description(self):
        desc = ''
        desc += "Strength:          " + str(self.strength) + '\n'
        desc += "Area radius:       " + str(self.area_radius) + '\n'
        desc += "Cost:                " + str(self.cost) + '\n'
        desc += "Time period:       " + str(self.time_period/1000) + 's\n'
        # desc += "Level:       " + str(self.level) + '\n'
        return desc
