import os
import pygame

from Levels.levelstate import LevelState
from Levels.level import Level
from Enemies.towers import DemonTower, SkellyTower

BG_IMAGE = pygame.image.load(os.path.join("Assets/Sprites/Screens", "01_Tutorial.png"))

class Tutorial (Level):
    def __init__(self, w, h, win, game):
        super ().__init__(w,h,win)
        self.bg = BG_IMAGE
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.name = "Tutorial"
        self.game = game
        self.max_gems = 100
        self.gems = self.max_gems
        self.start_pos = (-50, 200)
        self.end_pos = (180, 775)
        self.path = [(-50, 200), (780, 200), (780, 560), (180, 560), (180, 775)]

    def start(self):
        print("Tutorial Starts")
        self.enemies.append(DemonTower((660, 370), False))
        self.enemies.append(SkellyTower((300, 150), True))
        self.enemies.append(SkellyTower((120, 370), False))
        self.enemies.append(SkellyTower((500, 0), True))

        self.initial_troop()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if self.level_ui.pauseCheck(x, y):
                    self.game.change(LevelState.PAUSE)
                #print(x, y)

                self.check_character_buy(x, y)

                if self.level_ui.won:
                    if self.level_ui.nextCheck(x, y):
                        self.game.change(LevelState.REBELION)
                elif self.level_ui.lost:
                    if self.level_ui.retryCheck(x, y):
                        self.game.change(LevelState.TUTORIAL)


        self.character_movement()
        self.enemy_attacks()
        if not self.check_win():
            self.check_lose()