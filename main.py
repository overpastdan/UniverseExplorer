from tkinter import font
import pygame
import sys
import json
from utils.constants import WHITE, WIDTH, HEIGHT, BACKGROUND
from models.galaxy_explorer import GalaxyExplorer

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Galaxy Explorer")
        self.clock = pygame.time.Clock()
        self.load_config()
        self.explorer = GalaxyExplorer()
        
    def load_config(self):
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {
                'fps': 60,
                'num_stars': 5,
                'planet_speed': 0.3,
                'debug': False
            }
            self.save_config()
    
    def save_config(self):
        with open('config.json', 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def run(self):
        running = True
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.explorer.handle_event(event)
            
            # Update
            self.explorer.update()
            
            # Draw
            self.screen.fill(BACKGROUND)
            self.explorer.draw(self.screen)
            
            # Debug info if enabled
            if self.config['debug']:
                self.draw_debug_info()
            
            pygame.display.flip()
            self.clock.tick(self.config['fps'])
        
        pygame.quit()
        sys.exit()
    
    def draw_debug_info(self):
        fps = str(int(self.clock.get_fps()))
        fps_text = font.render(f'FPS: {fps}', True, WHITE)
        self.screen.blit(fps_text, (10, 10))

if __name__ == "__main__":
    game = Game()
    game.run()
