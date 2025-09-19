import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

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
