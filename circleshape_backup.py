import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        # Each CircleShape's position property is a 
        # pygame.Vector2. Use its distance_to
        # method to calculate the distance
        # between two shapes
        r1 = self.radius
        r2 = other.radius
        return self.position.distance_to(other.position) <= r1 + r2
