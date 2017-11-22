import pygame
from ..back import TowerRed, TowerGreen, TowerBlue


class TowerIcon:
    def __init__(self, screen, name, x, y, class_):
        self.image = pygame.image.load('source\\images\\' + name)
        self.screen = screen
        self.coordinates = pygame.Rect((x, y, 24, 24))
        self.class_name = class_
        self.clicked = False

    def __eq__(self, other):
        f_cond = self.image == other.image
        s_cond = self.coordinates == other.coordinates
        t_cond = self.class_name == other.class_name
        return f_cond and s_cond and t_cond

    def draw_icon(self):
        self.screen.blit(self.image, [self.coordinates.left, self.coordinates.top])
        pygame.display.flip()

    def check_if_collidepoint(self, pos):
        return self.coordinates.collidepoint(pos)


class RedTowerIcon(TowerIcon):
    def __init__(self, screen):
        super(RedTowerIcon, self).__init__(screen, 'tower_red.png', 1000, 155, TowerRed.TowerRed)

    def draw_icon(self):
        super(RedTowerIcon, self).draw_icon()

    def check_if_collidepoint(self, pos):
        return super(RedTowerIcon, self).check_if_collidepoint(pos)


class GreenTowerIcon(TowerIcon):
    def __init__(self, screen):
        super(GreenTowerIcon, self).__init__(screen, 'tower_green.png', 1040, 155, TowerGreen.TowerGreen)

    def draw_icon(self):
        super(GreenTowerIcon, self).draw_icon()

    def check_if_collidepoint(self, pos):
        return super(GreenTowerIcon, self).check_if_collidepoint(pos)


class BlueTowerIcon(TowerIcon):
    def __init__(self, screen):
        super(BlueTowerIcon, self).__init__(screen, 'tower_blue.png', 1080, 155, TowerBlue.TowerBlue)

    def draw_icon(self):
        super(BlueTowerIcon, self).draw_icon()

    def check_if_collidepoint(self, pos):
        return super(BlueTowerIcon, self).check_if_collidepoint(pos)
