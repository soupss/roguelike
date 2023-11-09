from settings import WINDOW_WIDTH, WINDOW_HEIGHT, GREEN, PLAYER_WIDTH, PLAYER_HEIGHT

from entities.entity import Entity


class Player(Entity):
    def __init__(self):
        size = (PLAYER_WIDTH, PLAYER_HEIGHT)
        super().__init__((0,0), size)
        self.rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.surface.fill(GREEN)
