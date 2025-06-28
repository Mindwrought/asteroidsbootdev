import pygame 
from constants import *
from player import Player
import asteroidfield

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    window= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")


# start of defining variables code

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT /2
    player = Player(x, y)

#  Start of game loop code

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        keys = pygame.key.get_pressed()
        updatable.update(keys, dt)

        window.fill((0,0,0))

        for obj in drawable:
            obj.draw(window)

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


    pygame.quit()





if __name__ == "__main__":
    main()
