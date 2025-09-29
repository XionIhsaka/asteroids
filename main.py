import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers

    Player.containers = updateables, drawables
    Asteroid.containers = asteroids, updateables, drawables
    AsteroidField.containers = updateables
    Shot.containers = shots, updateables, drawables

    # fps counter
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    AsteroidField()

    print("Starting Asteroids!")
# Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return

# Call player update
        updateables.update(dt)

    # Collision detection

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

# Drawing the screen
        screen.fill((0, 0, 0))

        for sprite in drawables:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")
