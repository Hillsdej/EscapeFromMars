#gives access to all of the pygame modules
import pygame
import time
import random
#this is the main function 
pygame.init()

#set up window using width and height in pixels
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width , display_height))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()

#set up colours
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red =(255,0,0)
bright_green =(0,255,0)

#size of mario sprite
mario_height = 70
mario_width = 95 

#downloaded mario sprite & removed whitespace with gimp alpha colour settings
#marioImg = pygame.image.load('Mario_Sprite 2.png')

def blocks_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def blocks(blockx, blocky, blockw, blockh, colour):
    pygame.draw.rect(gameDisplay, colour, [blockx, blocky, blockw, blockh])

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click [0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.QUIT
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))  

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def mario(x,y):
    gameDisplay.blit(marioImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return (textSurface, textSurface.get_rect())
        

def message_display(text):
    largeText = pygame.font.Font('FreeSansBold.ttf', 85)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def hit_wall():
    message_display('ouch')

def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('FreeSansBold.ttf', 85)
        TextSurf, TextRect = text_objects("Game Test", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button('Start',150,450,100,50,green,bright_green, "play")
        button('Quit',550,450,100,50,red,bright_red, "quit")
        
        pygame.display.update()
        clock.tick(15)
        
        
def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.45)

    x_change = 0
    y_change = 0
    

    block_startx = random.randrange(1,display_width)
    block_starty = -600
    block_speed = 5
    block_width = 100
    block_height = 100

    blockcount = 1
    dodged = 0

    gameExit = False

    #run the game loop
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #movement with keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = +5
                elif event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = +5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                

        x += x_change
        y += y_change

        gameDisplay.fill(white)

        blocks(block_startx, block_starty, block_width, block_height, red)
        block_starty += block_speed
        mario(x,y)
        blocks_dodged(dodged)
        
              
        if x > display_width - mario_width or x < 0:
            hit_wall()
        elif y > display_height - mario_height or y < 0:
            hit_wall()
                    

        if block_starty > display_height:
            block_starty = 0 - block_height
            block_startx = random.randrange(0, display_width)
            dodged += 1
            block_speed += 1

        if x > block_startx and x < block_startx + block_width or x + mario_width > block_startx and x + mario_width < block_startx + block_width:
            if y < block_starty + block_height:
                hit_wall()
        
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
    
