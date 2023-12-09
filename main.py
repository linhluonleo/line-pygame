import math
import random
import sys

import pygame


class Dot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Line")

dots = pygame.sprite.Group()

for i in range(150):
    dot = Dot(random.randint(0, 1280), random.randint(0, 720))
    dots.add(dot)

radius = 200

running = True

while running:
    screen.fill("gray30")
    dots.update()
    dots.draw(screen)

    mouse_pos = pygame.mouse.get_pos()

    for dot in dots:
        dot_pos = dot.rect.center
        if (
            math.sqrt(
                (dot_pos[0] - mouse_pos[0]) ** 2 + (dot_pos[1] - mouse_pos[1]) ** 2
            )
            <= radius
        ):
            pygame.draw.line(screen, "white", mouse_pos, dot_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
sys.exit()
