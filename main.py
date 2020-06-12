from src.game import *
import pygame
WIDTH = 600
HEIGHT = 800
while True:
    game = Game(WIDTH,HEIGHT)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    game.mainMenu()














