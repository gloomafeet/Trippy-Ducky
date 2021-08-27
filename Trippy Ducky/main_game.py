import pygame
import random
import math
from moviepy.editor import *
from pygame import mixer


def start():

    pygame.init()
    pygame.display.set_caption('Trippy Ducky')
    Weed = pygame.image.load("weed.png")
    pygame.display.set_icon(Weed)
    screen = pygame.display.set_mode((800, 600))
    clip1 = VideoFileClip('c1.mp4')
    clip2 = VideoFileClip('c2.mp4')
    clip3 = VideoFileClip('c3.mp4')

    video_size = (800,600)


    B1 = pygame.image.load('b4.png')
    B2 = pygame.image.load('b5-2.png')
    B3 = pygame.image.load('b53.png')
    B4 = pygame.image.load('b5.png')

    def background(B1):
        screen.blit(B1, (0,0))


    Player = pygame.image.load("duck.png")
    playerX= 0
    playerY= 200
    playerX_change = 0
    playerY_change = 0
    def player(x,y):
        screen.blit(Player, (x,y))


    weedX = random.randint(100, 700)
    weedY = random.randint(100, 500)

    Score = 0
    font = pygame.font.Font('freesansbold.ttf', 45)
    def score(x,y):
        score_render = font.render("Score: "+ str(Score), True, (255,255,255))
        screen.blit(score_render, (x,y))

    font1 = pygame.font.Font('freesansbold.ttf', 75)
    def gameover(x,y):
        rndr = font1.render("Thank you for playing", True, (255,0,0))
        screen.blit(rndr, (x,y))


    #n = 6

    #for i in range(n):
      #  Weed.append(pygame.image.load("weed.png"))
       # weedX.append(random.randint(100, 700))
        #weedY.append(random.randint(100, 500))
        #weed_change.append(3)

    def weed(x,y,):
        screen.blit(Weed, (x,y))

    def collision(playerX, playerY, weedX, weedY):
        distance = math.sqrt(math.pow((playerX - weedX),2) + (math.pow((playerY - weedY),2)))
        if distance < 22:
            return True
        else:
            return False


    running = True

    while running:
        screen.fill((255,0,255))
        background(B1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    playerX_change = 2
                if event.key == pygame.K_LEFT:
                    playerX_change = -2
                if event.key == pygame.K_UP:
                    playerY_change = -2
                if event.key == pygame.K_DOWN:
                    playerY_change = 2
                if event.key == pygame.K_SPACE:
                    scream = mixer.Sound('scream.wav')
                    scream.play()
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0


        if playerX >= 726:
           playerX = 726
        if playerX <= 5:
           playerX = 5

        if playerY >= 536:
            playerY = 536
        if playerY <= 5:
            playerY = 5

        #for i in range(n):
        weed(weedX, weedY)

        coll = collision(playerX, playerY, weedX, weedY)
        if coll:
            weedX = random.randint(100, 700)
            weedY = random.randint(100, 500)
            Score += 1
            if Score == 1:
                B1= B2
                clip1.resize(video_size).preview()
            if Score == 2:
                B1= B3
                clip2.resize(video_size).preview()
            if Score == 3:
                B1 = B4
                clip3.resize(video_size).preview()



        playerX += playerX_change
        playerY += playerY_change
        player(playerX, playerY)
        score(10,10)
        if Score >= 3:
            gameover(0, 150)

        pygame.display.update()

W = pygame.image.load("weed.png")
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Trippy Ducky')
pygame.display.set_icon(W)
Background = pygame.image.load('start.png')


def background():
    screen.blit(Background, (0, 0))


running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start()
                running = False

    background()
    pygame.display.update()
