import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Asteroid stuff

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        speed_multiplier = 1.2

        # Create two new velocity vectors, rotated and faster
        new_vel1 = self.velocity.rotate(angle) * speed_multiplier
        new_vel2 = self.velocity.rotate(-angle) * speed_multiplier

        #  Create asteroids at same position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Assign velocities
        asteroid1.velocity = new_vel1
        asteroid2.velocity = new_vel2