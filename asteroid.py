import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, color="white",  width=2, radius=self.radius, center=self.position)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(0, 50) # get a random angle, then create two velocity vectors from the original
        vel_rot_pos = self.velocity.rotate(random_angle)
        vel_rot_neg = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS # create new asterods with smaller radius. large->mediu, medium->small
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel_rot_pos * 1.2  # increase speed.
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel_rot_neg * 1.2

        
