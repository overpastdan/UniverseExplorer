import pygame
import sys
from models.galaxy import Galaxy
from utils.constants import WIDTH, HEIGHT, BACKGROUND, GALAXY_VIEW, SOLAR_SYSTEM_VIEW

class GalaxyExplorer:
    def __init__(self):
        self.state = GALAXY_VIEW  # Start with galaxy view
        self.galaxy = Galaxy()  # Create the galaxy with stars and planets
        self.selected_star = None  # No star selected at the start
        self.galaxy.state = GALAXY_VIEW  # Add state to galaxy
        self.zoom_level = 1.0
        self.target_zoom = 1.0
        self.transition_time = 0
    
    def handle_event(self, event):
        # Handle events like clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = pygame.mouse.get_pos()
                if self.state == GALAXY_VIEW:
                    # In galaxy view, check if a star is clicked
                    self.selected_star = self.galaxy.get_star_at(mouse_pos)
                    if self.selected_star:
                        self.state = SOLAR_SYSTEM_VIEW  # Switch to solar system view
                        self.galaxy.state = SOLAR_SYSTEM_VIEW  # Update galaxy state
                        self.target_zoom = 2.0  # Zoom in
                        self.transition_time = 30
            elif event.button == 3:  # Right click
                if self.state == SOLAR_SYSTEM_VIEW:
                    self.state = GALAXY_VIEW
                    self.galaxy.state = GALAXY_VIEW  # Update galaxy state
                    self.selected_star = None
                    self.target_zoom = 1.0  # Zoom out
                    self.transition_time = 30
            
    def update(self):
        # Smooth zoom transition
        if self.transition_time > 0:
            self.transition_time -= 1
            progress = self.transition_time / 30.0  # 30 frames transition
            self.zoom_level = self.target_zoom + (1.0 - self.target_zoom) * progress
            
        # Update game objects based on current state
        if self.state == GALAXY_VIEW:
            self.galaxy.update()
        elif self.state == SOLAR_SYSTEM_VIEW:
            # Only update planets orbiting the selected star
            for planet in self.galaxy.planets:
                if planet.star == self.selected_star:
                    planet.update()
    
    def draw(self, screen):
        # Draw background
        screen.fill(BACKGROUND)
        
        if self.state == GALAXY_VIEW:
            self.galaxy.draw(screen)
        elif self.state == SOLAR_SYSTEM_VIEW and self.selected_star:
            # Draw the selected star and its planets
            self.selected_star.draw(screen)
            for planet in self.galaxy.planets:
                if planet.star == self.selected_star:
                    planet.draw(screen)
                    planet.draw_info(screen)

