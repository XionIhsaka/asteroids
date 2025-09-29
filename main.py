import pygame
from player import *
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # fps counter
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting Asteroids!")
# Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return

# Black screen
        screen.fill((0, 0, 0))
        player.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")
