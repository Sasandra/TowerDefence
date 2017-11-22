import pygame


class Monster:
    def __init__(self, speed_, health_, prize_, image_name, x_, y_):
        self.speed = speed_
        self.health = health_
        self.prize = prize_
        self.image_name = image_name
        self.image = pygame.image.load('source\\images\\' + image_name)
        self.x = x_
        self.y = y_
        self.direction = "down"
        self.coordinates = pygame.Rect(x_, y_, 26, 26)

    def decrease_health(self, amount):
        self.health -= amount

    def check_health(self):
        return self.health <= 0

    def update_coordinates(self, x_, y_):
        self.coordinates = pygame.Rect(x_, y_, 26, 26)
