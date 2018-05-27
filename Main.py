import pygame, sys, Func
from tileClass import Tile
from object_classes import *
from interaction import interaction
from invalidsFunc import *
from A_Star import A_Star
from time import sleep
#from game_intro import *

import os
x = 140
y = 50
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)


#set screen size 
display_width = 960
display_height = 640
screen = pygame.display.set_mode((display_width,display_height))
#print(type(screen))

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red =(255,0,0)
bright_green =(0,255,0)

clock = pygame.time.Clock()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x,y,w,h))
        if click [0] == 1 and action != None:
            if action == "play":
                gameLoop()
            elif action == "quit":
                pygame.quit()
                sys.exit()
    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))  

    smallText = pygame.font.SysFont("Arial.txt", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return (textSurface, textSurface.get_rect())


def game_intro():
    pygame.init()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        openingImage = pygame.image.load("images/OpeningImage.png")
        screen.blit(openingImage, (0,0))
        largeText = pygame.font.SysFont('Arial.txt', 85)
        TextSurf, TextRect = text_objects("Escape From Mars!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        button('Start',150,450,100,50,green,bright_green, "play")
        button('Quit',650,450,100,50,red,bright_red, "quit")
        
        pygame.display.update()
        clock.tick(15)

def gameLoop():
    pygame.init()
    pygame.font.init()
    #pygame.mixer.init()

    #pygame.mixer.music.load("audio/halo_themes.wav")
    #pygame.mixer.music.play(-1)

    invalids = tuple(invalids_func())

    for y in range(0, screen.get_height(), 32):
        for x in range(0, screen.get_width(), 32):
            if Tile.total_tiles in invalids:
                Tile(x, y, 'solid')
            else:
                Tile(x, y, 'empty')
                
    #set time
    #clock = pygame.time.Clock()
    FPS = 24
    total_frames = 0

    background = pygame.image.load('images/Background.png')
    player = Player(64,128)

        
    while player.health > 1:
        
        screen.blit(background,(0,0))

        Enemy.spawn(total_frames,FPS)
        Enemy.update(screen,player)

        player.movement()

        Bullet.super_massive_jumbo_loop(screen)

        A_Star(screen, player, total_frames, FPS)
        interaction(screen, player)
        player.draw(screen)

        Func.text_to_screen(screen,"Health {0}".format(player.health),0,0)
      

        pygame.display.flip()
        clock.tick(FPS)
        total_frames += 1

        if player.health <= 0:
            sleep(2)
            screen.blit(pygame.image.load("images/End.png"),(0,0))
            pygame.display.update()
            break

    sleep(4)

game_intro()
gameLoop()
pygame.quit()
sys.exit()
