import pygame

# Screen dimensions
WIDTH = 1200
HEIGHT = 800

# Colors
BACKGROUND = (5, 5, 15)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
BROWN = (165, 42, 42)
GRAY = (128, 128, 128)
PLANET_COLORS = [BLUE, RED, GREEN, ORANGE, PURPLE, CYAN, BROWN]

# Game states
GALAXY_VIEW = 0
SOLAR_SYSTEM_VIEW = 1

# Initialize fonts
pygame.font.init()
font = pygame.font.SysFont('Arial', 16)
title_font = pygame.font.SysFont('Arial', 30)