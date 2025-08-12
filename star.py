import pygame
import random
from math import *

class Star(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, *groups, vel_x=0.0, vel_y=0.0, acc_x=0.0, acc_y=0.0,):
        super().__init__(*groups)
        self.screen = screen
        self.pos = pygame.math.Vector2(x ,y)
        self.vel = pygame.math.Vector2((vel_x, vel_y))
        self.acc = pygame.math.Vector2((acc_x, acc_y))

    def update_physics(self):
        self.update_acceleration()
        self.update_velocity()
        self.update_position()

    def move(self, displacement):
        self.pos += pygame.math.Vector2(displacement)
    
    def update_position(self):
        # move
        self.pos += self.vel

        # if moved out of bounds, spawn a new star
        if not(-50 <= self.pos.x <= self.screen.get_width() + 50):
            self.replace(1)
        if not(-50 <= self.pos.y <= self.screen.get_height() + 50):
            self.replace(1)

    def update_velocity(self):
        self.vel += self.acc
        self.vel.clamp_magnitude(20)
    
    def update_acceleration(self):
        # Initialize temp variable
        new_acc = pygame.math.Vector2(0, 0)
        # calculate a distance variable normalized so that it is centred and results in max accel at x
        x = 250
        dis = (self.pos.x - self.screen.get_width()/2) / (sqrt(2) * x)

        new_acc.update(-dis*(e**-(dis**2)), 0)
        new_acc = new_acc + pygame.math.Vector2(random.random()-0.5, random.random()-0.5) / 4
        new_acc.clamp_magnitude(1)

        self.acc.update(new_acc)
        
    def update_graphics(self, screen):
        pygame.draw.circle(screen, "WHITE", self.pos, 3.0)
        self.draw_acc()
    
    def draw_vel(self):
        pygame.draw.line(self.screen, "WHITE", self.pos, self.pos+self.vel)
    
    def draw_acc(self):
        self.draw_vel()
        pygame.draw.line(self.screen, "RED", self.pos+self.vel, self.pos+self.vel+self.acc*40)

    def replace(self, mode):
        if not (mode in [1, 2]):
            raise ValueError("invailid replace mode")

        # mode 1: spawn star at random position anywhere on screen
        if mode == 1:
            replacement = Star(self.screen, random.randint(0, self.screen.get_width()), random.randint(0, self.screen.get_height()))
        # mode 2: spawn star anywhere on the edge
        if mode == 2:
            lin_pos = random.randint(1, self.screen.get_width()*2 + self.screen.get_height()*2)
            coords = pygame.math.Vector2(0, 0)
            if lin_pos <= self.screen.get_width():
                coords.update(lin_pos, 0)
            elif lin_pos <= self.screen.get_width()*2:
                coords.update(lin_pos-self.screen.get_width(), self.screen.get_height())
            elif lin_pos <= self.screen.get_width()*2 + self.screen.get_height():
                coords.update(0, lin_pos-self.screen.get_width()*2)
            else:
                coords.update(self.screen.get_height(), lin_pos-self.screen.get_width()*2-self.screen.get_height())
            replacement = Star(self.screen, coords.x, coords.y)

        for group in self.groups():
            group.add(replacement)
        self.kill()
        del self
