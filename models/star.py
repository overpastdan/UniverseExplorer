import pygame
import pymunk
from utils.constants import YELLOW

class Star:
    def __init__(self, position, mass=2000, radius=30, color=YELLOW):
        self.position = position
        self.mass = mass
        self.radius = radius
        self.color = color
        self.body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
        self.body.position = position
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 0
        self.shape.friction = 0.5
        self.shape.collision_type = 1
        
    def draw(self, screen):
        pos_x, pos_y = int(self.body.position.x), int(self.body.position.y)
        
        # Create a glowing effect
        for i in range(10, 0, -2):
            alpha = 100 - i * 10
            radius = self.radius + i * 2
            s = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(s, (*self.color, alpha), (radius, radius), radius)
            screen.blit(s, (pos_x - radius, pos_y - radius))
            
        pygame.draw.circle(screen, self.color, (pos_x, pos_y), self.radius)