import sys
import pygame 
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
    window= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
# start of defining variables code

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT /2
    player = Player(x, y)
    field = AsteroidField()

#  Start of game loop code
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        updatable.update(dt)



        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                running = False

       for shot in shots:
            if player.shoots:




        window.fill((0,0,0))

        for obj in drawable:
            obj.draw(window)



        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


    pygame.quit()
    sys.exit()




if __name__ == "__main__":
    main()
