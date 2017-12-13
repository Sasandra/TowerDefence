import pygame
from ..texts import constatnts


class Monster:
    def __init__(self, speed_, health_, prize_, image_name, x_, y_, direction_):
        self.speed = speed_
        self.health = health_
        self.prize = prize_
        self.image_name = image_name
        self.image = pygame.image.load('source\\images\\' + image_name + '-0'
                                                                         '.png')
        self.x = x_
        self.y = y_
        self.direction = direction_
        self.coordinates = pygame.Rect(x_, y_, 26, 26)
        self.original_health = health_
        self.clicked = False

        self.change_direction_image()


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

    def change_image(self):
        heal = self.original_health
        if 0.80 * heal < self.health <= heal:
            self.image = pygame.image.load('source\\images\\' + self.image_name + '-0.png')
        elif 0.60 * heal < self.health <= 0.80 * heal:
            self.image = pygame.image.load('source\\images\\' + self.image_name + '-1.png')
        elif 0.40 * heal < self.health <= 0.60 * heal:
            self.image = pygame.image.load('source\\images\\' + self.image_name + '-2.png')
        elif 0.20 < self.health <= 0.40 * heal:
            self.image = pygame.image.load('source\\images\\' + self.image_name + '-3.png')
        elif 0 < self.health <= 0.20 * heal:
            self.image = pygame.image.load('source\\images\\' + self.image_name + '-4.png')

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

    def change_direction_image(self):
        pass
        # if self.direction == 'left':
        #     self.image = pygame.image.load('source\\images\\' + self.image_name + '_left.png')
        # elif self.direction == 'right':
        #     self.image = pygame.image.load('source\\images\\' + self.image_name + '_right.png')
        # elif self.direction == 'down':
        #     self.image = pygame.image.load('source\\images\\' + self.image_name + '_down.png')
        # elif self.direction == 'up':
        #     self.image = pygame.image.load('source\\images\\' + self.image_name + '_up.png')

