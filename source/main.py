import pygame, os, sys
from source.front import HelloMenu
from source.front import MainWindow
from source.texts import constatnts

pygame.init()
pygame.display.set_caption(constatnts.GAME_NAME)

os.environ['SDL_VIDEO_CENTERED'] = '1'

if HelloMenu.HelloMenu(constatnts.HELLO_MENU_TITLE_IMAGE).start() is not None:
    MainWindow.MainWindow().start()

else:
    pygame.quit()
