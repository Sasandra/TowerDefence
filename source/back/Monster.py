import pygame
from ..texts import constatnts


class Monster:
    def __init__(self, speed_, health_, prize_, image_name, x_, y_, direction_):
        self.speed = speed_
        self.health = health_
        self.prize = prize_
        self.image_name = image_name
        self.image = pygame.image.load(constatnts.IMAGES_PATH + image_name + '_right-0.png')
        self.x = x_
        self.y = y_
        self.direction = direction_
        self.coordinates = pygame.Rect(x_, y_, 26, 26)
        self.original_health = health_
        self.clicked = False
        self.cross_amount = 0
        self.health_level = 0

        self.change_image()

    def decrease_health(self, amount):
        self.health -= amount

    def check_health(self):
        return self.health <= 0

    def level_up(self):
        self.health *= 1.2
        self.health = int(self.health)
        self.original_health *= 1.2
        self.original_health = int(self.original_health)

    def update_coordinates(self, x_, y_):
        self.coordinates = pygame.Rect(x_, y_, 26, 26)

    def change_health_level(self):
        heal = self.original_health
        if 0.65 * heal < self.health <= heal:
            self.health_level = 0
        elif 0.30 * heal < self.health <= 0.65 * heal:
            self.health_level = 1
        elif 0 < self.health <= 0.30 * heal:
            self.health_level = 2

    def check_if_collidepoint(self, pos):
        return self.coordinates.collidepoint(pos)

    def check_if_clicked(self):
        return self.clicked

    def return_description(self):
        desc = ''
        desc += "Speed:     " + str(self.speed) + '\n'
        desc += "Health:    " + str(self.health) + '/' + str(self.original_health) + '\n'
        desc += "Prize:     " + str(self.prize) + '\n'
        # desc += "Level:       " + str(self.level) + '\n'
        return desc

    def change_image(self):
        name = self.image_name + '_' + self.direction + '-' + str(self.health_level) + '.png'
        self.image = pygame.image.load(constatnts.IMAGES_PATH + name)
