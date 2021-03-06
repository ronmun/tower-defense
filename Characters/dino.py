from os import listdir
from os.path import isfile, join
import pygame
import os

from .entity import Entity, ENTITY_WIDTH, ENTITY_HEIGHT, SCALE, DINO_COST

path = os.path.join ("Assets/Sprites/Characters/Dino")
files = [f for f in listdir (path) if isfile (join (path, f))]

imgs = []
for f in files:
	imgs.append (
		pygame.transform.scale (
			pygame.image.load (join (path, f)),
			(int(ENTITY_WIDTH*SCALE), int(ENTITY_HEIGHT*SCALE))
		)
	)

class Dino (Entity):
	def __init__(self, pos, path):
		super().__init__(pos, path)
		self.name = "dino"
		self.cost = DINO_COST
		self.imgs = imgs[:]
		self.max_health = 6
		self.health = self.max_health
		self.vel = 2
