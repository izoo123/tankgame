import pygame
import random
import math
from Thingobjects import Bullet


#Function
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

#Create screen
WIDTH = 800
HEIGHT = 800

size = (WIDTH, HEIGHT)

#Tank and class


class Tank:
    moveForward = [False, False]
    tankHealth = [100, 100]
    nTank = 2
    tnkposx = [700, 100]
    tnkposy = [400, 400]
    tXchange = [0, 0]
    tYchange = [0, 0]
    tankFacing = [0, 0]
    angle = [0, 0]
    angle_change = [0, 0]
    bulletIcn = pygame.image.load('tank.png')
    tankIcn = [pygame.image.load('tank.png'), pygame.image.load('tank.png')]
    times = 10
    runOnceHit = True

    def __init__(self, posx, posy, screen, i):
       screen.blit(Tank.tankIcn[i], (posx, posy))

    @staticmethod
    def calculateDistance(x1, y1, x2, y2):
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return dist

    @staticmethod
    def collision(bullets, tank1, tank2):
        for i in range(5):
            colDist = Tank.calculateDistance(bullets[i].bposx, bullets[i].bposy, Tank.tnkposx[0], Tank.tnkposy[0])

            if colDist < 30:
                bullets[i].bposx = -50
                bullets[i].bposy = -50
                bullets[i].runOnce = True
                bullets[i].bulletStateTnk2 = False
                Tank.tankHealth[0] -= 10

        for i in range(5,10):
            colDist2 = Tank.calculateDistance(bullets[i].bposx, bullets[i].bposy, Tank.tnkposx[1], Tank.tnkposy[1])

            if colDist2 < 30:
                bullets[i].bposx = -50
                bullets[i].bposy = -50
                bullets[i].runOnce = True
                bullets[i].bulletStateTnk1 = False
                Tank.tankHealth[1] -= 10


    def controls(self, plcontrol, event, i, bullets):

        if event.type == pygame.KEYDOWN:
            if event.key == plcontrol[0]:
                Tank.angle_change[i] = 2

            if event.key == plcontrol[1]:
                Tank.angle_change[i] = -2

            if event.key == plcontrol[2]:
                Tank.moveForward[i] = True

            if event.key == plcontrol[3]:
                pass

            if event.key == plcontrol[4]:
                if event.key == pygame.K_f:
                    bullets[Bullet.fireCountTnk1].bulletFire(False)
                    Bullet.fireCountTnk1 += 1
                    if Bullet.fireCountTnk1 > 4:
                        Bullet.fireCountTnk1 = 0


                if event.key == pygame.K_PERIOD:
                    bullets[Bullet.fireCountTnk2].bulletFire(True)
                    Bullet.fireCountTnk2 += 1
                    if Bullet.fireCountTnk2 > 9:
                        Bullet.fireCountTnk2 = 5


        if event.type == pygame.KEYUP:
            if event.key == plcontrol[0]:
                Tank.angle_change[i] = 0

            if event.key == plcontrol[1]:
                Tank.angle_change[i] = 0

            if event.key == plcontrol[2]:
                Tank.moveForward[i] = False
                Tank.tXchange[i] = 0
                Tank.tYchange[i] = 0

    @staticmethod
    def tankForward(i):
        if Tank.moveForward[i]:

            if (Tank.tankFacing[i] >= 0 and Tank.tankFacing[i] < 0.2) or (
                    Tank.tankFacing[i] < -7.8 and Tank.tankFacing[i] >= -8):
                Tank.tXchange[i] = 0
                Tank.tYchange[i] = -1.5

            if (Tank.tankFacing[i] >= 0.2 and Tank.tankFacing[i] < 1) or (
                    Tank.tankFacing[i] < -7 and Tank.tankFacing[i] >= -7.8):
                Tank.tXchange[i] = -.5
                Tank.tYchange[i] = -1

            if (Tank.tankFacing[i] >= 1 and Tank.tankFacing[i] < 1.8) or (
                    Tank.tankFacing[i] < -6.2 and Tank.tankFacing[i] >= -7):
                Tank.tXchange[i] = -1
                Tank.tYchange[i] = -.5

            if (Tank.tankFacing[i] >= 1.8 and Tank.tankFacing[i] < 2.2) or (
                    Tank.tankFacing[i] < -5.8 and Tank.tankFacing[i] >= -6.2):
                Tank.tXchange[i] = -1.5
                Tank.tYchange[i] = 0

            if (Tank.tankFacing[i] >= 2.2 and Tank.tankFacing[i] < 3) or (
                    Tank.tankFacing[i] < -5 and Tank.tankFacing[i] >= -5.8):
                Tank.tXchange[i] = -1
                Tank.tYchange[i] = .5

            if (Tank.tankFacing[i] >= 3 and Tank.tankFacing[i] < 3.8) or (
                    Tank.tankFacing[i] < -4.2 and Tank.tankFacing[i] >= -5):
                Tank.tXchange[i] = -.5
                Tank.tYchange[i] = 1

            if (Tank.tankFacing[i] >= 3.8 and Tank.tankFacing[i] < 4.2) or (
                    Tank.tankFacing[i] < -3.8 and Tank.tankFacing[i] >= -4.2):
                Tank.tXchange[i] = 0
                Tank.tYchange[i] = 1.5

            if (Tank.tankFacing[i] >= 4.2 and Tank.tankFacing[i] < 5) or (
                    Tank.tankFacing[i] < -3 and Tank.tankFacing[i] >= -3.8):
                Tank.tXchange[i] = .5
                Tank.tYchange[i] = 1

            if (Tank.tankFacing[i] >= 5 and Tank.tankFacing[i] < 5.8) or (
                    Tank.tankFacing[i] < -2.2 and Tank.tankFacing[i] >= -3):
                Tank.tXchange[i] = 1
                Tank.tYchange[i] = .5

            if (Tank.tankFacing[i] >= 5.8 and Tank.tankFacing[i] < 6.2) or (
                    Tank.tankFacing[i] < -1.8 and Tank.tankFacing[i] >= -2.2):
                Tank.tXchange[i] = 1.5
                Tank.tYchange[i] = 0

            if (Tank.tankFacing[i] >= 6.2 and Tank.tankFacing[i] < 7) or (
                    Tank.tankFacing[i] < -1 and Tank.tankFacing[i] >= -1.8):
                Tank.tXchange[i] = 1
                Tank.tYchange[i] = -.5

            if (Tank.tankFacing[i] >= 7 and Tank.tankFacing[i] < 7.8) or (
                    Tank.tankFacing[i] < -.2 and Tank.tankFacing[i] >= -1):
                Tank.tXchange[i] = .5
                Tank.tYchange[i] = -1

            if (Tank.tankFacing[i] >= 7.8 and Tank.tankFacing[i] < 8) or (
                      Tank.tankFacing[i] < 0 and Tank.tankFacing[i] > -.2):
                Tank.tXchange[i] = 0
                Tank.tYchange[i] = -1.5
        #Tank.angle1 += Tank.angle1_change





