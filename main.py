import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0

    # Creation of sprite groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # set player groups and create player object
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # set asteroid groups
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    while True:
        screen.fill("black")
        # Listens for user to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # CLock for adjusting FPS
        clock = pygame.time.Clock()
        updatable.update(dt)
        for item  in drawable:
            item.draw(screen)


        dt = clock.tick(60)/1000
        pygame.display.flip()
if __name__ == "__main__":
    main()
