import pygame
from pygame import mixer
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    pygame.mixer.init()
    mixer.music.load("./assets/beatbox-elias.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(loops=-1)
    isDone = False
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0

    # Creation of sprite groups
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # set player groups and create player object
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # set asteroid groups
    Asteroid.containers = (asteroids, updatable, drawable)
    
    # Set asteroid field groups and create asteroid field object
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # Set shot groups Shot.containers = (shots, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    while not isDone:
        screen.fill("black")
        # Listens for user to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # CLock for adjusting FPS
        clock = pygame.time.Clock()
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.isColliding(player):
                print("Game over!")
                isDone = True
                continue
            
            for shot in shots:
                if shot.isColliding(asteroid):
                    asteroid.split()
                    shot.kill()
        for item  in drawable:
            item.draw(screen)


        dt = clock.tick(60)/1000
        pygame.display.flip()
if __name__ == "__main__":
    main()
