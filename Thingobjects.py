import pygame
import math

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


class Bullet:
    bposx = 0
    bposy = 0
    bposxChange = 0
    bposyChange = 0
    bFacing = 0
    bulletDir = 0
    bulletStateTnk1 = False
    bulletStateTnk2 = False
    bulletIcn = pygame.image.load('bullet.png')
    newBulletIcn = pygame.image.load('bullet.png')
    fireCountTnk1 = 0
    fireCountTnk2 = 5
    bAngle = 0
    runOnce = True


    def bulletFire(self, i):
        if i:
            self.bulletStateTnk1 = True
        elif not i:
            self.bulletStateTnk2 = True


    def resetBullets(self):
        pass


    def shoot(self, screen, tankNum, tanksposx, tanksposy, angle):
            if self.runOnce:
                self.bposx = tanksposx
                self.bposy = tanksposy
                self.bFacing = angle / 45
                self.bulletIcn = rot_center(Bullet.newBulletIcn, angle)
                self.runOnce = False

            #minor issue bullet does not come out of the right part of the tank and always comes out of the same place despite rotation

            screen.blit(self.bulletIcn, (self.bposx, self.bposy))
            self.bposx += self.bposxChange
            self.bposy += self.bposyChange

            if (self.bFacing >= 0 and self.bFacing < 0.2) or (
                    self.bFacing < -7.8 and self.bFacing >= -8):
                self.bposxChange = 0
                self.bposyChange = -3

            if (self.bFacing >= 0.2 and self.bFacing < 1) or (
                    self.bFacing < -7 and self.bFacing >= -7.8):
                self.bposxChange = -1
                self.bposyChange = -2

            if (self.bFacing >= 1 and self.bFacing < 1.8) or (
                    self.bFacing < -6.2 and self.bFacing >= -7):
                self.bposxChange = -2
                self.bposyChange = -1

            if (self.bFacing >= 1.8 and self.bFacing < 2.2) or (
                    self.bFacing < -5.8 and self.bFacing >= -6.2):
                self.bposxChange = -3
                self.bposyChange = 0

            if (self.bFacing >= 2.2 and self.bFacing < 3) or (
                    self.bFacing < -5 and self.bFacing >= -5.8):
                self.bposxChange = -2
                self.bposyChange = 1

            if (self.bFacing >= 3 and self.bFacing < 3.8) or (
                    self.bFacing < -4.2 and self.bFacing >= -5):
                self.bposxChange = -1
                self.bposyChange = 2

            if (self.bFacing >= 3.8 and self.bFacing < 4.2) or (
                    self.bFacing < -3.8 and self.bFacing >= -4.2):
                self.bposxChange = 0
                self.bposyChange = 3

            if (self.bFacing >= 4.2 and self.bFacing < 5) or (
                    self.bFacing < -3 and self.bFacing >= -3.8):
                self.bposxChange = 1
                self.bposyChange = 2

            if (self.bFacing >= 5 and self.bFacing < 5.8) or (
                    self.bFacing < -2.2 and self.bFacing >= -3):
                self.bposxChange = 2
                self.bposyChange = 1

            if (self.bFacing >= 5.8 and self.bFacing < 6.2) or (
                    self.bFacing < -1.8 and self.bFacing >= -2.2):
                self.bposxChange = 3
                self.bposyChange = 0

            if (self.bFacing >= 6.2 and self.bFacing < 7) or (
                    self.bFacing < -1 and self.bFacing >= -1.8):
                self.bposxChange = 2
                self.bposyChange = -1

            if (self.bFacing >= 7 and self.bFacing < 7.8) or (
                    self.bFacing < -.2 and self.bFacing >= -1):
                self.bposxChange = 1
                self.bposyChange = -2

            if (self.bFacing >= 7.8 and self.bFacing < 8) or (
                    self.bFacing < 0 and self.bFacing > -.2):
                self.bposxChange = 0
                self.bposyChange = -3














