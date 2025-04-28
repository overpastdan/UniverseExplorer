import pygame
import math
import random
from utils.constants import WHITE, GRAY

class Moon:
    def __init__(self, planet, orbit_radius, size):
        self.planet = planet
        self.orbit_radius = orbit_radius
        self.radius = size
        self.color = GRAY
        self.angle = random.uniform(0, 2 * math.pi)
        self.angular_velocity = 0.002 * math.sqrt(1000 / orbit_radius)
        self.x, self.y = planet.x, planet.y
        
    def update(self):
        self.angle += self.angular_velocity
        # Moon orbits around its planet
        self.x = self.planet.x + math.cos(self.angle) * self.orbit_radius
        self.y = self.planet.y + math.sin(self.angle) * self.orbit_radius
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)