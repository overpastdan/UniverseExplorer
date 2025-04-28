from utils.constants import HEIGHT, WIDTH


class Camera:
    def __init__(self):
        self.position = [WIDTH//2, HEIGHT//2]
        self.target_position = [WIDTH//2, HEIGHT//2]
        self.zoom = 1.0
        self.target_zoom = 1.0
        
    def update(self):
        # Smooth camera movement
        self.position[0] += (self.target_position[0] - self.position[0]) * 0.1
        self.position[1] += (self.target_position[1] - self.position[1]) * 0.1
        self.zoom += (self.target_zoom - self.zoom) * 0.1
    
    def set_target(self, x, y, zoom=1.0):
        self.target_position = [x, y]
        self.target_zoom = zoom