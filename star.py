import pygame
import random
from math import *

class Star(pygame.sprite.Sprite):

    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.pos = pygame.math.Vector2(x ,y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)

    def update_physics(self):
        self.update_acceleration()
        self.update_velocity()
        self.update_position()


    def move(self, displacement):
        self.pos += pygame.math.Vector2(displacement)
    
    def update_position(self):
        self.pos += self.velocity
        self.pos.x = min(1280, self.pos.x)
        self.pos.x = max(0, self.pos.x)
        self.pos.y = min(720, self.pos.y)
        self.pos.y = max(0, self.pos.y)

    def update_velocity(self):
        self.velocity += self.acceleration
        self.velocity.clamp_magnitude(20)
    
    def update_acceleration(self):
        new_acc = pygame.math.Vector2(0, 0)
        dis = (self.pos.x - 640) / 240
        new_acc.update(-dis*(e**-(dis**2)), (340 - self.pos.y)/1000)
        new_acc = new_acc + pygame.math.Vector2(random.random()-0.5, random.random()-0.5) / 4
        new_acc.clamp_magnitude(1)
        self.acceleration.update(new_acc)
        

    def update_graphics(self, screen):
        pygame.draw.circle(screen, "WHITE", self.pos, 3.0)
