import pygame
import os
pygame.init()
import random
SIZE = (63,31)
class Brick:
    def __init__(self, game,pos):
        self.game = game
        self.pos = pos
        self.size =(63 , 31)
        path = os.path.join(os.getcwd(),os.path.join("Assets","Brick.png"))
        self.brick = pygame.image.load(path)
        self.colision = False

    def draw(self):
        if not self.colision:
            self.game.win.blit(self.brick,self.pos)

    def update(self):
        xBall,yBall = self.game.ball.pos
        yBall-=self.game.ball.radius
        x,y = self.pos
        w,h = self.size
        if( y <=yBall <= y + h ) and (x<=xBall<=x+w):
            self.game.ball.speed[1]*=-1
            self.game.score += 1
            self.colision = True

class Bricks(object):
    def __init__(self,game):
        self.game = game
        self.stage = []
        self.offset = 2
        self.size_Brick = (63, 31) #pixels
        self. col = 0
        self.row = 0
        self.fill()
        self.calculateStage()
    def fill(self):
        self.col = self.game.width // (self.size_Brick[0] + self.offset)
        self.row = random.randrange(5, 10)
        for i in range(self.row):
            temp = []
            for j in range(self.col):
                temp.append(random.randrange(0, 4))
            self.stage.append(temp)

    def calculateStage(self):
        self.Objects = []
        for i in range(self.row):
            for j in range(self.col):
                if self.stage[i][j]:
                    pos = (j * self.size_Brick[0] , i * self.size_Brick[1] )
                    self.Objects.append(Brick(self.game , pos))
    def draw(self):
        for obj in self.Objects[:]:
            obj.draw()

    def update(self):
        for obj in self.Objects[:]:
            obj.update()
            if obj.colision:
                self.Objects.remove(obj)





        # xBall,yBall = self.game.ball.pos
        # leftX,leftY = self.pos
        # # if(xBall >= leftX and xBall <= leftX + self.size[0]) and (yBall <= leftY + self.size[1] and yBall >= leftY):
        # #
        # #     if not self.colision:
        # #         if yBall <= leftY + self.size[1] and  yBall >= leftY:
        # #             self.game.ball.speed[1]*=-1
        # #         if xBall >= leftX and xBall <= leftX + self.size[0]:
        # #             self.game.ball.speed[0]*=-1
        # #     self.colision = True
