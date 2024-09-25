
import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()

		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		split1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
		split1.velocity = self.velocity.rotate(random.uniform(20, 50)) * 1.2

		split2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
		split2.velocity = self.velocity.rotate(random.uniform(20, 50) * -1) * 1.2
