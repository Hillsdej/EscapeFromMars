import pygame

def text_to_screen(screen, text, x, y, size = 32,
            colour = (255, 255, 255), font_type = 'Arial.txt'):
        
        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, colour)
        screen.blit(text, (x, y))

    
