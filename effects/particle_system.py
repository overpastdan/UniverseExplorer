import random
import pygame
import math

class Particle:
    def __init__(self, pos, velocity, color, lifetime):
        self.pos = list(pos)
        self.velocity = velocity
        self.color = color
        self.lifetime = lifetime
        self.age = 0
        
    def update(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.age += 1
        return self.age < self.lifetime

class ParticleSystem:
    def __init__(self, position, color, particle_count=20):
        self.position = position
        self.color = color
        self.particles = []
        self.particle_count = particle_count
    
    def emit(self):
        for _ in range(2):  # Emit 2 particles per frame
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(0.5, 2)
            velocity = [math.cos(angle) * speed, math.sin(angle) * speed]
            color = (*self.color, random.randint(100, 255))
            self.particles.append(Particle(self.position, velocity, color, 
                                        random.randint(30, 60)))
    
    def update(self):
        self.particles = [p for p in self.particles if p.update()]
    
    def draw(self, screen):
        for p in self.particles:
            alpha = 255 * (1 - p.age / p.lifetime)
            color = (*p.color[:3], int(alpha))
            pygame.draw.circle(screen, color, 
                             [int(p.pos[0]), int(p.pos[1])], 2)