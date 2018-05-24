import pygame,sys
from tileClass import Tile
from object_classes import *

def interaction(screen, player):
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type ==  pygame. KEYDOWN:
            if event.key == pygame.K_e:
                player.current += 1
                player.current %= 3

    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_w]: # North
        future_tile_number = player.get_number() - Tile.V
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                player.set_target(future_tile)
                player.rotate('n')
                #player.y -= player.height                   

    if keys[pygame.K_s]: # South
        future_tile_number = player.get_number() + Tile.V
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                player.set_target(future_tile)
                player.rotate('s')
                #player.y += player.height 

    if keys[pygame.K_a]: # West
        future_tile_number = player.get_number() - Tile.H
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                player.set_target(future_tile)
                player.rotate('w')
                
                #player.x -= player.width 

    if keys[pygame.K_d]: # East
        future_tile_number = player.get_number() + Tile.H

        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                player.set_target(future_tile)
                player.rotate('e')
                #player.x += player.width 

                    
    if keys[pygame.K_LEFT]:
        player.rotate('w')
        Bullet(player.centerx, player.centery, -10,0,'w',player.get_bullet_type())       

    elif keys[pygame.K_RIGHT]:
        player.rotate('e')
        Bullet(player.centerx, player.centery, 10,0,'e',player.get_bullet_type())

    elif keys[pygame.K_UP]:
        player.rotate('n')
        Bullet(player.centerx, player.centery, 0,-10,'n',player.get_bullet_type())

    elif keys[pygame.K_DOWN]:
        player.rotate('s')
        Bullet(player.centerx, player.centery, 0,10,'s',player.get_bullet_type())
    
