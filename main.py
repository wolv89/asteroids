
wx = 100
wy = 100

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (wx,wy)

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	afield = AsteroidField()

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")

		for u in updatable:
			u.update(dt)

		for a in asteroids:
			if player.collides(a):
				print("Game over!")
				sys.exit()
			for bullet in shots:
				if bullet.collides(a):
					a.split()
					bullet.kill()

		for d in drawable:
			d.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()