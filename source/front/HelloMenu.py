import pygame
from ..back import Button
from ..texts import constatnts


class HelloMenu:
    def __init__(self, name):
        self.screen = pygame.display.set_mode(constatnts.HELLO_MENU_SCREEN_SIZE)
        self.start_button = Button.Button('start', constatnts.HELLO_MENU_START_BUTTON_IMAGE,
                                          constatnts.HELLO_MENU_START_BUTTON_RECT,
                                          constatnts.HELLO_MENU_START_BUTTON_SIZE, self.screen)

        self.exit_button = Button.Button('exit', constatnts.HELLO_MENU_EXIT_BUTTON_IMAGE,
                                         constatnts.HELLO_MENU_EXIT_BUTTON_RECT,
                                         constatnts.HELLO_MENU_EXIT_BUTTON_SIZE, self.screen)
        self.menu_state = True

        self.set_layout(name)

    def set_layout(self, name):
        menu_background = pygame.image.load(constatnts.IMAGES_PATH + constatnts.HELLO_MENU_IMAGE)
        self.screen.blit(menu_background, constatnts.HELLO_MENU_BACKGROUND_BLIT)

        tittle = pygame.image.load(constatnts.IMAGES_PATH + name)
        tittle = pygame.transform.scale(tittle, constatnts.HELLO_MENU_TITLE_TRANSFORM)
        self.screen.blit(tittle, constatnts.HELLO_MENU_TITLE_BLIT)

        self.start_button.read_image()
        self.exit_button.read_image()
        pygame.display.flip()

    def start(self):
        while self.menu_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_state = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.start_button.button.collidepoint(pygame.mouse.get_pos()):
                            self.start_button.on_click()

                        elif self.exit_button.button.collidepoint(pygame.mouse.get_pos()):
                            self.exit_button.on_click()

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.start_button.button.collidepoint(pygame.mouse.get_pos()):
                            self.start_button.on_click()
                            return "start"

                        elif self.exit_button.button.collidepoint(pygame.mouse.get_pos()):
                            self.exit_button.on_click()
                            self.menu_state = False
                            return None
