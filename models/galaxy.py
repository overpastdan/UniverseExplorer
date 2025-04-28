import random
import pygame
import math
from models.star import Star
from models.planet import Planet
from utils.constants import GALAXY_VIEW, PLANET_COLORS, YELLOW, RED, ORANGE, BROWN, BLUE, CYAN, PURPLE

class Galaxy:
    def __init__(self, num_stars=5):
        self.stars = []
        self.planets = []
        self.asteroids = []
        self.state = GALAXY_VIEW
        self.generate_galaxy(num_stars)

    def generate_galaxy(self, num_stars):
        for _ in range(num_stars):
            x = random.randint(100, 1100)
            y = random.randint(100, 700)
            star = Star(position=(x, y), mass=2000, radius=30, color=YELLOW)
            self.stars.append(star)
            
            # Generate a solar system with realistic proportions
            self.generate_solar_system(star)
    
    def generate_solar_system(self, star):
        # Minimum and maximum distances from star (in pixels)
        MIN_ORBIT = 60  # Closest possible orbit
        MAX_ORBIT = 400  # Furthest possible orbit
        
        # Generate 2-8 planets per star
        num_planets = random.randint(2, 8)
        
        # Calculate orbit ranges using logarithmic distribution
        # This ensures planets are spaced further apart as they get farther from the star
        orbit_ranges = []
        for i in range(num_planets):
            # Use logarithmic spacing
            orbit = MIN_ORBIT + (MAX_ORBIT - MIN_ORBIT) * (math.log(i + 1) / math.log(num_planets))
            orbit_ranges.append(int(orbit))
        
        for i in range(num_planets):
            # Planet characteristics based on distance from star
            orbit_radius = orbit_ranges[i]
            
            # Smaller planets far from star, larger planets in "gas giant" zone
            if orbit_radius < 150:
                # Rocky planets (smaller)
                planet_radius = random.randint(8, 15)
                planet_mass = random.randint(100, 500)
                # Higher chance of being hot/rocky
                planet_color = random.choice([RED, ORANGE, BROWN])
            elif orbit_radius < 250:
                # Medium planets
                planet_radius = random.randint(12, 20)
                planet_mass = random.randint(400, 1000)
                # Mix of types
                planet_color = random.choice(PLANET_COLORS)
            else:
                # Gas giants (larger)
                planet_radius = random.randint(18, 35)
                planet_mass = random.randint(1000, 3000)
                # Higher chance of being gaseous
                planet_color = random.choice([BLUE, CYAN, PURPLE])
            
            # Orbital speed decreases with distance (Kepler's laws)
            angular_velocity = 0.02 * math.sqrt(1000 / orbit_radius)
            
            # Create the planet
            planet = Planet(
                position=(star.body.position.x + orbit_radius, star.body.position.y),
                mass=planet_mass,
                radius=planet_radius,
                color=planet_color,
                orbit_radius=orbit_radius,
                star=star,
                angular_velocity=angular_velocity
            )
            
            self.planets.append(planet)
        
        # Add asteroid belt between rocky planets and gas giants
        self.generate_asteroid_belt(star, 200, 220)
    
    def generate_asteroid_belt(self, star, inner_radius, outer_radius):
        num_asteroids = random.randint(20, 30)
        for _ in range(num_asteroids):
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(inner_radius, outer_radius)
            size = random.randint(1, 3)
            
            asteroid = {
                'x': star.body.position.x + math.cos(angle) * radius,
                'y': star.body.position.y + math.sin(angle) * radius,
                'radius': radius,
                'size': size,
                'angle': angle,
                'speed': 0.01 * math.sqrt(1000 / radius)
            }
            self.asteroids.append(asteroid)

    def draw(self, screen):
        if self.state == GALAXY_VIEW:
            # Draw enhanced galaxies
            for star in self.stars:
                pos = (int(star.body.position.x), int(star.body.position.y))
                
                # Draw outer glow
                for radius in range(45, 30, -5):
                    alpha_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
                    alpha = max(0, int(255 * (1 - radius/45)))  # Fade out effect
                    pygame.draw.circle(alpha_surface, (100, 100, 200, alpha), (radius, radius), radius)
                    screen.blit(alpha_surface, (pos[0] - radius, pos[1] - radius))
                
                # Draw core and spiral arms
                pygame.draw.circle(screen, (150, 150, 255), pos, 20)  # Brighter core
                pygame.draw.circle(screen, (200, 200, 255), pos, 10)  # Central bright spot
                
                # Draw spiral arms
                for i in range(2):  # Two spiral arms
                    angle = i * math.pi
                    for t in range(0, 20, 2):
                        spiral_x = pos[0] + math.cos(angle + t/5) * t
                        spiral_y = pos[1] + math.sin(angle + t/5) * t
                        size = max(1, 3 - t/7)
                        pygame.draw.circle(screen, (150, 150, 255), (int(spiral_x), int(spiral_y)), int(size))
        else:
            # Draw solar system
            for star in self.stars:
                star.draw(screen)
            
            # Draw asteroid belt
            for asteroid in self.asteroids:
                pygame.draw.circle(screen, (100, 100, 100), 
                                 (int(asteroid['x']), int(asteroid['y'])), 
                                 asteroid['size'])
            
            for planet in self.planets:
                if hasattr(planet, 'star') and planet.star in self.stars:
                    planet.draw(screen)
    
    def update(self):
        # Update all planets
        for planet in self.planets:
            planet.update()
        
        # Update asteroids
        for asteroid in self.asteroids:
            asteroid['angle'] += asteroid['speed']
            asteroid['x'] = (self.stars[0].body.position.x + 
                            math.cos(asteroid['angle']) * asteroid['radius'])
            asteroid['y'] = (self.stars[0].body.position.y + 
                            math.sin(asteroid['angle']) * asteroid['radius'])

    def get_star_at(self, position):
        # Check if the click position is within a star's radius
        for star in self.stars:
            dist = pygame.math.Vector2(position).distance_to(star.body.position)
            if dist < star.radius:
                return star
        return None
