import pygame, sys

screen = pygame.display.set_mode((960,640))
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red =(255,0,0)
bright_green =(0,255,0)


def blocks(blockx,blocky,blockw,blockh,colour):
    pygame.draw.rect(screen, colour, [blockx, blocky, blockw, blockh])

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

                #make a game_loop function in the main file
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))

    smallText = pygame.font.Font("Arial.txt", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

##def text_objects(text, font):
##    textSurface = font.render(text, True, black)
##    return (textSurface, textSurface.get_rect())
##

def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)
        largeText = pygame.font.Font('Arial.txt', 85)
        TextSurf, TextRect = text_objects("Game Test", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        button('Start',150,450,100,50,green,bright_green, "play")
        button('Quit',550,450,100,50,red,bright_red, "quit")
        
        pygame.display.update()
        clock.tick(15)



    
