import pygame
import math
import random
from models.moon import Moon
from utils.constants import WIDTH, HEIGHT, WHITE, GREEN, RED, font

class Planet:
    def __init__(self, position, mass, radius, color, orbit_radius, star, angular_velocity):
        self.mass = mass
        self.radius = radius
        self.color = color
        self.orbit_radius = orbit_radius
        self.star = star
        self.angular_velocity = angular_velocity * 0.1  # Slow down movement
        self.angle = random.uniform(0, 2 * math.pi)
        self.name = f"Planet-{random.randint(1, 999)}"
        
        # Position
        self.x, self.y = position
        
        # Determine planet type based on orbit radius
        if orbit_radius < 150:
            self.type = "rocky"
            self.atmosphere = random.random() > 0.7  # 30% chance
            self.temperature = random.randint(200, 500)  # Hot
        elif orbit_radius < 250:
            self.type = "mixed"
            self.atmosphere = random.random() > 0.5  # 50% chance
            self.temperature = random.randint(-50, 200)  # Moderate
        else:
            self.type = "gas_giant"
            self.atmosphere = True  # Always has atmosphere
            self.temperature = random.randint(-200, -50)  # Cold
        
        # Water can only exist in certain temperature ranges
        self.water = (-50 < self.temperature < 100) and self.atmosphere
        # Habitability requires moderate temperatures and atmosphere
        self.habitable = (-20 < self.temperature < 50) and self.atmosphere and self.water
        
        # Generate moons based on planet type
        self.moons = []
        if self.type == "rocky":
            num_moons = random.randint(0, 2)
        elif self.type == "mixed":
            num_moons = random.randint(0, 3)
        else:  # gas giant
            num_moons = random.randint(2, 5)
            
        for _ in range(num_moons):
            moon_orbit = random.uniform(self.radius * 2, self.radius * 3)
            moon_size = random.randint(2, max(3, self.radius // 3))
            self.moons.append(Moon(self, moon_orbit, moon_size))
    
    def update(self):
        # Update planet position
        self.angle += self.angular_velocity
        self.x = self.star.body.position.x + math.cos(self.angle) * self.orbit_radius
        self.y = self.star.body.position.y + math.sin(self.angle) * self.orbit_radius
        
        # Update moons
        for moon in self.moons:
            moon.update()
    
    def draw(self, screen):
        # Draw orbit
        pygame.draw.circle(screen, (40, 40, 40), 
                         (int(self.star.body.position.x), int(self.star.body.position.y)), 
                         int(self.orbit_radius), 1)
        
        # Draw moons
        for moon in self.moons:
            moon.draw(screen)
        
        # Draw planet
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
    
    def draw_info(self, screen):
        info_lines = [
            f"Name: {self.name}",
            f"Type: {self.type}",
            f"Temperature: {self.temperature}°C",
            f"Atmosphere: {'Yes' if self.atmosphere else 'No'}",
            f"Water: {'Yes' if self.water else 'No'}",
            f"Moons: {len(self.moons)}",
            f"Habitable: {'Yes' if self.habitable else 'No'}"
        ]
        
        # Create info box
        padding = 5
        line_height = 20
        box_width = 180
        box_height = len(info_lines) * line_height + padding * 2
        
        x_pos = min(int(self.x) + self.radius + 10, WIDTH - box_width - padding)
        y_pos = min(int(self.y) - box_height//2, HEIGHT - box_height - padding)
        
        # Draw semi-transparent background
        info_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        pygame.draw.rect(info_surface, (0, 0, 0, 180), info_surface.get_rect())
        screen.blit(info_surface, (x_pos, y_pos))
        
        # Draw text
        for i, line in enumerate(info_lines):
            color = GREEN if "Yes" in line else WHITE
            if "Habitable: No" in line:
                color = RED
            text = font.render(line, True, color)
            screen.blit(text, (x_pos + padding, y_pos + i * line_height + padding))
