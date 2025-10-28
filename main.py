import pygame
from constants import *
from player import *
from asteroid import *
from AsteroidField import *
from shot import *

def main():
    keep_looping = True
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_colour = (0, 0, 0)
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player1 = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS)
    field = AsteroidField()

    while keep_looping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(background_colour)
        updatable.update(dt)

        for asteroid_chk in asteroids:  # check to see if each asteroid collides with player. 
            if asteroid_chk.collision(player1):
                print("Game over!")
                exit(0)
            
            for shot in shots:  # check to see if any shot collides with the asteroid.               
                if asteroid_chk.collision(shot):
                    shot.kill()
                    asteroid_chk.split()
                    continue

        for draw_this in drawable:
            draw_this.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
