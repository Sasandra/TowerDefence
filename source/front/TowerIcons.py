import pygame
from ..back import TowerRed, TowerGreen, TowerBlue
from ..texts import constatnts


class TowerIcon:
    def __init__(self, screen, name, x, y, class_):
        self.image = pygame.image.load('source\\images\\' + name)
        self.screen = screen
        self.coordinates = pygame.Rect((x, y, constatnts.TOWER_IMAGE_SIZE_X, constatnts.TOWER_IMAGE_SIZE_Y))

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

    def return_class_name(self, pos):
        if self.coordinates.collidepoint(pos):
            return self.class_name
        else:
            return None


class RedTowerIcon(TowerIcon):
    def __init__(self, screen):
        super(RedTowerIcon, self).__init__(screen, constatnts.RED_TOWER_IMAGE, constatnts.RED_TOWER_ICON_X,
                                           constatnts.RED_TOWER_ICON_Y, TowerRed.TowerRed)

    def draw_icon(self):
        super(RedTowerIcon, self).draw_icon()

    def check_if_collidepoint(self, pos):
        return super(RedTowerIcon, self).check_if_collidepoint(pos)

    def return_class_name(self, pos):
        return super(RedTowerIcon, self).return_class_name(pos)


class GreenTowerIcon(TowerIcon):
    def __init__(self, screen):
        super(GreenTowerIcon, self).__init__(screen, constatnts.GREEN_TOWER_IMAGE, constatnts.GREEN_TOWER_ICON_X,
                                             constatnts.GREEN_TOWER_ICON_Y, TowerGreen.TowerGreen)

    def draw_icon(self):
        super(GreenTowerIcon, self).draw_icon()

    def check_if_collidepoint(self, pos):
        return super(GreenTowerIcon, self).check_if_collidepoint(pos)

    def return_class_name(self, pos):
        return super(GreenTowerIcon, self).return_class_name(pos)


class BlueTowerIcon(TowerIcon):
    def __init__(self, screen):
        super(BlueTowerIcon, self).__init__(screen, constatnts.BLUE_TOWER_IMAGE, constatnts.BLUE_TOWER_ICON_X,
                                            constatnts.BLUE_TOWER_ICON_Y, TowerBlue.TowerBlue)

    def draw_icon(self):
        super(BlueTowerIcon, self).draw_icon()

    def check_if_collidepoint(self, pos):
        return super(BlueTowerIcon, self).check_if_collidepoint(pos)

    def return_class_name(self, pos):
        return super(BlueTowerIcon, self).return_class_name(pos)
