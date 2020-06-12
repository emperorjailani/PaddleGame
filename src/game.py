import sys
import math
import os
from src.bricks import  *
from src.paddle import *
from src.ball import *
class Game:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width ,self.height))
        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.bricks = Bricks(self)
        self.running = True
        self.score = 0
        self.gameOver = False
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Paddle Game")
        self.objects = [self.paddle , self.ball ]

    def draw(self):
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(f"Score: {self.score}", False, (255, 255, 255 ))
        self.win.fill((0, 0, 0))
        for obj in self.objects:
            obj.draw()
        self.bricks.draw()
        self.win.blit(text, (0, 0))
        pygame.display.flip()

    def update(self):
        for obj in self.objects:
            obj.update()
        self.bricks.update()

    def gameLoop(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break;
            self.draw()
            self.update()


    def mainMenu(self):
        next = False
        font = pygame.font.SysFont("comicsans" , 40 )
        txt = "Press Space To Play"
        Text = font.render( txt,False , (255,255,255))
        w,h = font.size(txt)
        pos = ((self.width-w)/2,self.height/2)
        while not next:
            self.win.fill((0,0,0))
            self.win.blit(Text,pos)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        next = True
        self.gameLoop()
        self.gameOver = True

