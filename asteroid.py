from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)
        image = pygame.image.load("./assets/eliastroid.png").convert_alpha()
        scaled = pygame.transform.scale(image, (self.radius*3, self.radius*3))
        screen.blit(scaled,(self.position.x-self.radius*1.5, self.position.y-self.radius*1.15))
        
    def update(self, dt):
            self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_angle = random.uniform(260,50)
        v1 = self.velocity.rotate(split_angle)
        v2 = self.velocity.rotate(-split_angle)
        asteroid1.velocity = v1 *1.2
        asteroid2.velocity = v2 *1.2
