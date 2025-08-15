import pygame
import random
from star import Star

# Initialize pygame
pygame.init()

# Initialize clock
clock = pygame.time.Clock()

# Initialize display
SCREEN_DIMENSIONS = (1280, 720)

screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Night sky")

# Initialize background
background = pygame.surface.Surface(screen.get_rect().size)
background.fill("black")

fade_surf = pygame.Surface(screen.get_rect().size, pygame.SRCALPHA)
fade_surf.fill((0x00, 0x00, 0x00, 0x08))

# Initialize stars
stars = pygame.sprite.Group()
star1 = Star(screen, 100, 100, stars)
for i in range (200):
    new_star = Star(screen, random.randint(0, screen.get_width()), random.randint(0, screen.get_height()), stars)


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
    
    print(len(stars))

    # Update graphics
    screen.blit(background, (0, 0))

    for star in stars:
        star.update_graphics(screen)
        pygame.draw.line(background, "PURPLE", (int(star.pos.x), int(star.pos.y)), (int(star.pos.x), int(star.pos.y)), 3)
    
    background.set_at((int(star1.pos.x), int(star1.pos.y)), "GREEN")

    background.blit(fade_surf, (0, 0))

    pygame.display.flip()

    # Tick clock
    clock.tick(30)

    
pygame.quit()