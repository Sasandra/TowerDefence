import pygame
from ..texts import constatnts


class Button:
    def __init__(self, name, image, coordinates, scale, screen):
        self.name = name
        self.image_name = image
        self.button = pygame.Rect(coordinates)
        self.clicked = False
        self.scale = scale
        self.coordinates = [coordinates[0], coordinates[1]]
        self.screen = screen

    def on_click(self):
        if self.clicked is False:
            self.clicked = True
            name = self.image_name
            name = name.split('.')
            self.image_name = name[0] + '_click.' + name[1]
            self.read_image()
            return

        else:
            self.clicked = False
            name = self.image_name
            name = name.split('.')
            temp_name = name[0].split('_')
            self.image_name = temp_name[0] + '.' + name[1]
            self.read_image()
            return

    def read_image(self):
        image = pygame.image.load(constatnts.IMAGES_PATH + self.image_name)
        if self.scale is not None:
            image = pygame.transform.scale(image, self.scale)
        self.screen.blit(image, self.coordinates)
        pygame.display.flip()
