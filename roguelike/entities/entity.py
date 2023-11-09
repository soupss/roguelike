import pygame


class Entity:
    def __init__(self, pos: (int, int), size: (int, int)):
        self.surface = pygame.Surface(size)
        self.rect = pygame.Rect(pos, size)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)
