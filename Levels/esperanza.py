import os
import pygame

from Levels.levelstate import LevelState
from Levels.level import Level
from Levels.level_ui import LevelUi
from Enemies.towers import DemonTower, SkellyTower
from Characters.elf import Elf
from Characters.dino import Dino
from Characters.ogre import Ogre
from Characters.wizard import Wizard


class Esperanza (Level):
    def __init__(self, w, h, win, game):
        super ().__init__(w,h,win)
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "03_Esperanza.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.game = game
        self.start_pos = (-50, 150)
        self.end_pos = (-30, 650)

    def start(self):
        print("Esperanza Starts")
        self.enemies.append(DemonTower(300, 125, True))
        self.enemies.append(DemonTower(550, 50, True))
        self.enemies.append(DemonTower(500, 300, True))
        self.enemies.append(DemonTower(700, 300, False))
        self.enemies.append(DemonTower(500, 520, False))
        self.enemies.append(SkellyTower(220,500, False))

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                # check if hit start btn
                x, y = pygame.mouse.get_pos()
                print(x, y)
                self.game.change(LevelState.TUTORIAL)