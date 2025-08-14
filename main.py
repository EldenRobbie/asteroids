import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    player1 = Player(x = (SCREEN_WIDTH / 2), y = (SCREEN_HEIGHT / 2))
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        player1.update(dt)
        screen.fill("black")
        player1.draw(screen)
        pygame.display.flip()
        
        # limit the framerate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
