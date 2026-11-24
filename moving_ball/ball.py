import pygame
class Ball:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.radius = 25
        self.speed = 20
        self.color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.radius
        )

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
