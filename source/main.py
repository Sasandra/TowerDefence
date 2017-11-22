import pygame
from source.front import HelloMenu
from source.front import MainWindow

pygame.init()
pygame.display.set_caption('TowerDefence')

if HelloMenu.HelloMenu('tittle.png').start() is not None:
    MainWindow.MainWindow().start()
else:
    pygame.quit()
