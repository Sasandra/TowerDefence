import pygame
from ..back import Button


class HelloMenu:
    def __init__(self, name):
        self.screen = pygame.display.set_mode((800, 600))
        self.start_button = Button.Button('start', 'start.png', (320, 400, 173, 80), (173, 80), self.screen)
        self.exit_button = Button.Button('exit', 'exit.png', (320, 500, 173, 80), (173, 80), self.screen)
        self.menu_state = True

        self.set_layout(name)

    def set_layout(self, name):
        menu_background = pygame.image.load('source\\images\\hello_menu_background.jpg')
        self.screen.blit(menu_background, (0, 0))

        tittle = pygame.image.load('source\\images\\' + name)
        tittle = pygame.transform.scale(tittle, (699, 540))
        self.screen.blit(tittle, (50, -120))

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
