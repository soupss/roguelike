import pygame

from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE

from entities.player import Player


class Game:
    def __init__(self):
        pygame.init()
        window_size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption('Game')
        self.running = True
        self.entities = []
        self.player = Player()
        self.entities.append(self.player)


    def is_running(self) -> bool:
        return self.running


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def update(self):
        pass


    def draw(self):
        self.screen.fill(WHITE)
        for entity in self.entities:
            entity.draw(self.screen)
        pygame.display.flip()
