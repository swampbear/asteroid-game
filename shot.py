from circleshape import CircleShape
from constants import *
from pygame import mixer
from sound_effects import play_shot_sound
import pygame

class Shot(CircleShape):
    def __init__(self, x,y):
        super().__init__(x, y, SHOT_RADIUS)
    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen,"red", self.position, self.radius, 2)
        
    def sound(self):
        play_shot_sound()

