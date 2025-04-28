import pymunk

# Create and configure the physics space
def create_space():
    space = pymunk.Space()
    space.gravity = (0, 0)  # No global gravity - we'll calculate it manually
    space.damping = 0.7  # Add some drag to stabilize orbits
    
    # Collision types
    space.STAR_COLLISION_TYPE = 1
    space.PLANET_COLLISION_TYPE = 2
    
    # Add collision handlers
    def handle_star_planet_collision(arbiter, space, data):
        return True
        
    def handle_planet_planet_collision(arbiter, space, data):
        return True
    
    # Setup collision handlers
    handler = space.add_collision_handler(
        space.STAR_COLLISION_TYPE, 
        space.PLANET_COLLISION_TYPE
    )
    handler.separate = handle_star_planet_collision
    
    handler = space.add_collision_handler(
        space.PLANET_COLLISION_TYPE, 
        space.PLANET_COLLISION_TYPE
    )
    handler.separate = handle_planet_planet_collision
    
    return space

# Create and export the space instance
space = create_space()