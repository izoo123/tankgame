import pygame
import sys
import math
import random
import Characters
from Characters import Tank, rot_center
import Thingobjects
from Thingobjects import Bullet
from pygame import mixer

pygame.init()

#Create screen
WIDTH = 800
HEIGHT = 800

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)


#Title
pygame.display.set_caption("TANK WARS")

#Title screen
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
myfont = pygame.font.SysFont("monospace", 75)
pfont = pygame.font.SysFont("monospace", 45)
title = myfont.render("Tank Wars", 1, WHITE)
ScrPlaybtn= pfont.render("Start Game", 1, BLACK)
playbtn = pfont.render("Start Game", 1, WHITE)
TitleX = 190
TitleY = 200
PlayX = 245
PlayY = 500
titleRunning = True
startgame = False
blktitle = True
times = 10

#Bullets
bullet = [Bullet() for i in range(10)]

#Main game
background = pygame.image.load('street.jpg')

#Tank
numtanks = 2
newTankIcn = pygame.image.load('tank.png')

while titleRunning:
    #RGB screen
    screen.fill((0,50,0))
    screen.blit(title, (TitleX, TitleY))
    screen.blit(playbtn, (PlayX, PlayY))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Test")
            xpos = event.pos[0]
            ypos = event.pos[1]
            if (xpos > 250 and xpos < 510) and (ypos > 500 and ypos < 545):
                startgame = True
                break

        #Get mouse position
        #mpos = pygame.mouse.get_pos()

        #while (mpos[0] > 250 and mpos[0] < 510) and (mpos[1] > 500 and mpos[1] < 545):
            #screen.blit(ScrPlaybtn, (PlayX, PlayY))
           # pygame.display.update()
            #blktitle = False

        #if blktitle == False:
           # blktitle = True
            #break
                #mpos2 = pygame.mouse.get_pos()
                #if (mpos2[0] < 250 or mpos2[0] > 510) or (mpos2[1] < 500 or mpos[1] > 545):
                    #break

    if startgame == True:
        gameRunning = True
        break


pygame.init()
while gameRunning:
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))

    #Tanks
    tnk_1 = Tank(Tank.tnkposx[0], Tank.tnkposy[0], screen, 0)
    tnk_2 = Tank(Tank.tnkposx[1], Tank.tnkposy[1], screen, 1)

    #Scores
    healthPl1 = pfont.render("Player 2 Health: " + str(Tank.tankHealth[0]), 1, WHITE)
    screen.blit(healthPl1, (200,700))

    healthPl2 = pfont.render("Player 1 Health: " + str(Tank.tankHealth[1]), 1, WHITE)
    screen.blit(healthPl2, (30, 30))

    if Tank.tankHealth[0] == 0:
        endScreenRunning = True
        winner = "player1"
        break
    elif Tank.tankHealth[1] == 0:
        endScreenRunning = True
        winner = "player2"
        break

    #controls
    controlPl1 = pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_PERIOD
    controlPl2 = pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_f

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()




        tnk_1.controls(controlPl1, event, 0, bullet)
        tnk_2.controls(controlPl2, event, 1, bullet)

    Tank.tankForward(0)
    Tank.tankForward(1)

    for i in range(10):
        if bullet[i].bulletStateTnk1:
            bullet[i].shoot(screen, 0, Tank.tnkposx[0], Tank.tnkposy[0], Tank.angle[0])

        elif bullet[i].bulletStateTnk2:
            bullet[i].shoot(screen, 1, Tank.tnkposx[1], Tank.tnkposy[1], Tank.angle[1])

    for i in range(5):
        if bullet[i].bposx < 0 or bullet[i].bposx > 800:
            bullet[i].bulletStateTnk2 = False
            bullet[i].runOnce = True

        if bullet[i].bposy < 0 or bullet[i].bposy > 800:
            bullet[i].bulletStateTnk2 = False
            bullet[i].runOnce = True

    for i in range(5, 10):
        if bullet[i].bposx < 0 or bullet[i].bposx > 800:
            bullet[i].bulletStateTnk1 = False
            bullet[i].runOnce = True

        if bullet[i].bposy < 0 or bullet[i].bposy > 800:
            bullet[i].bulletStateTnk1 = False
            bullet[i].runOnce = True


    for i in range(numtanks):
        Tank.tankFacing[i] = Tank.angle[i] / 45

    for i in range(numtanks):
        if Tank.angle[i] >= 360:
            Tank.angle[i] = 0

        if Tank.angle[i] <= -360:
            Tank.angle[i] = 0

    #Updating Tank Position And Rotation
    for i in range(numtanks):
        Tank.tnkposx[i] += Tank.tXchange[i]
        Tank.tnkposy[i] += Tank.tYchange[i]

        Tank.angle[i] += Tank.angle_change[i]
        Tank.tankIcn[i] = rot_center(newTankIcn, Tank.angle[i])

        if Tank.tnkposx[i] < 0:
            Tank.tnkposx[i] = 1

        if Tank.tnkposx[i] > 800:
            Tank.tnkposx[i] = 799

        if Tank.tnkposy[i] < 0:
            Tank.tnkposy[i] = 1

        if Tank.tnkposy[i] > 800:
            Tank.tnkposy[i] = 79.9




    Tank.collision(bullet, tnk_1, tnk_2)

    pygame.display.update()

#player 1 winning text
pl1Wins = myfont.render("Player 1 Wins", 1, WHITE)
#player 2 winning text
pl2Wins = myfont.render("Player 2 Wins", 1, WHITE)

while endScreenRunning:

    screen.fill((0, 50, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if winner == "player1":
        screen.blit(pl1Wins, (100, 300))
    else:
        screen.blit(pl2Wins, (100, 300))


    pygame.display.update()


