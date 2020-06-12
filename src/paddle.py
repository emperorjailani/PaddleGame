import pygame
pygame.init()
class Paddle(object):
    def __init__(self, game):
        self.game = game
        self.width = 100
        self.height = 10
        self.offset = 20
        self.color = (255,255,255)
        self.position = [
            self.game.width/2 - self.width/2,
            self.game.height - self.offset
        ]
        self.speed = 0
        self.maxSpeed = 10

    def draw(self):
        pygame.draw.rect(self.game.win, self.color,(self.position[0],self.position[1],self.width,self.height))

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.moveLeft()
        elif pressed[pygame.K_RIGHT]:
            self.moveRight()
        else:
            self.stop()
        pygame.display.flip()
    def moveLeft(self):
        self.speed = -(self.maxSpeed)
        self.move()
        if self.position[0] < 0:
            self.position[0] = 0


    def moveRight(self):
        self.speed = self.maxSpeed
        self.move()
        if self.position[0]+self.width > self.game.width:
            self.position[0] = self.game.width - self.width


    def move(self):
        self.position[0] += self.speed

    def stop(self):
        self.speed = 0


