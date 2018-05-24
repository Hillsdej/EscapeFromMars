import pygame
display_width = 960
display_height = 640
screen = pygame.display.set_mode((display_width,display_height))
def game_intro():
    pygame.init()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        szcreen.image.load("images/Opening.png")
        largeText = pygame.font.SysFont('Arial.txt', 85)
        TextSurf, TextRect = text_objects("Game Test", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        button('Start',150,450,100,50,green,bright_green, "play")
        button('Quit',650,450,100,50,red,bright_red, "quit")
        
        pygame.display.update()
        clock.tick(15)

game_intro()
