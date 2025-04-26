
import pygame
import sys

# Key constants
K_LEFT = pygame.K_LEFT
K_RIGHT = pygame.K_RIGHT
K_UP = pygame.K_UP
K_DOWN = pygame.K_DOWN

class Oixels:
    def __init__(self, width=32, height=32, scale=15, title="Oixels Game"):
        pygame.init()
        self.width = width
        self.height = height
        self.scale = scale
        self.screen = pygame.display.set_mode((width * scale, height * scale))
        pygame.display.set_caption(title)
        self.running = True
        self.font = pygame.font.SysFont('Arial', int(scale * 1.5))

    def clear(self):
        self.screen.fill((0, 0, 0))

    def pixel(self, x, y, color):
        pygame.draw.rect(self.screen, color, 
                        (x * self.scale, y * self.scale, 
                         self.scale, self.scale))

    def text(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x * self.scale, y * self.scale))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pygame.display.flip()

    def is_key_pressed(self, key):
        return pygame.key.get_pressed()[key]

    def quit(self):
        pygame.quit()
        sys.exit()
