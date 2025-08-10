import pygame
import random
from star import Star

# Initialize pygame
pygame.init()

# Initialize clock
clock = pygame.time.Clock()

# Initialize display
SCREEN_DIMENSIONS = (1280, 720)
SCREEN_X = SCREEN_DIMENSIONS[0]
SCREEN_Y = SCREEN_DIMENSIONS[1]

screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Night sky")

pygame.draw.line(screen, "RED", (0, SCREEN_Y/2), (SCREEN_X, SCREEN_Y/2))
pygame.draw.line(screen, "RED", (SCREEN_X/2, 0), (SCREEN_X/2, SCREEN_Y))
pygame.display.flip()

# Initialize stars
stars = pygame.sprite.Group()
star1 = Star(100, 100, stars)
for i in range(100):
    new_star = Star(random.randint(0, SCREEN_X), random.randint(0, SCREEN_Y), stars)


# Simulation loop
running = True
while running:
    # Event detection loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update physics
    for star in stars:
        star.update_physics()
    
    # Update graphics
    screen.fill("BLACK")

    for star in stars:
        star.update_graphics(screen)
    pygame.display.flip()

    # Tick clock
    clock.tick(30)

    
pygame.quit()