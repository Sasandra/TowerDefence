import pygame
from source.front import HelloMenu

pygame.init()
pygame.display.set_caption('TowerDefence')

print(HelloMenu.HelloMenu().start())
pygame.quit()