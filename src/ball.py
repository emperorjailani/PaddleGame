import pygame
import os
pygame.init()

class Ball:
    def __init__(self,game):
        self.game = game
        self.pos = [400,250]
        self.maxSpeed = (3,5)
        self.speed = [self.maxSpeed[0], self.maxSpeed[1]]
        self.radius =8
    def draw(self):
        pygame.draw.circle(self.game.win , (255,0,0),(self.pos[0],self.pos[1]),self.radius)

    def update(self):
        self.move()

    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        if self.pos[0] - self.radius < 0 or self.pos[0] + self.radius > self.game.width:
            self.speed[0]*=-1
        if self.pos[1] - self.radius < 0 :
            self.speed[1]*=-1
        if self.pos[1] > self.game.height:
            self.game.running = False
        self.collisionPaddle()
    def collisionPaddle(self):
        xPaddle = self.game.paddle.position[0]
        yPaddle = self.game.paddle.position[1]
        wPaddle = self.game.paddle.width

        if (self.pos[0] >= xPaddle and self.pos[0]  <= (xPaddle+wPaddle)) and (self.pos[1] +self.radius >= yPaddle):
            self.speed[1]*=-1
            if self.game.paddle.speed > 0:
                self.speed[0] = abs(self.maxSpeed[0])
            elif self.game.paddle.speed < 0:
                self.speed[0] = -abs(self.maxSpeed[0])
            else:
                self.speed[0] = 0


