import pygame
from tileClass import Tile
from random import randint
import random

class Character(pygame.Rect):

    width, height = 32,32

    def __init__(self, x, y):

        self.tx, self.ty = None,None
        pygame.Rect.__init__(self, x, y, Character.width, Character.height)
        
    def __str__(self):
        return str(self.get_number())

    def set_target(self, next_tile):
        if self.tx == None and self.ty == None:
            self.tx = next_tile.x
            self.ty = next_tile.y

    def get_number(self):

        return ((self.x // self.width) + Tile.H) + ((self.y // self.height)* Tile.V)

    def get_tile(self):

        return Tile.get_tile(self.get_number())

    def rotate(self, direction ,original_img):

        if direction == "n":
            if self.direction != "n":
                self.direction = "n"
                south = pygame.transform.rotate(original_img, 90)
                self.img = pygame.transform.flip(south, False,True)

        if direction == "s":
            if self.direction != "s":
                self.direction = "s"
                self.img = pygame.transform.rotate(original_img, 90)

        if direction == "e":
            if self.direction != "e":
                self.direction = "e"
                self.img = pygame.transform.flip(original_img, True, False)
            
        if direction == "w":
            if self.direction != "w":
                self.direction = "w"
                self.img = original_img

class Enemy(Character):

    List = []
    spawn_tiles = (12,15,168,514,537)
    original_img = pygame.image.load("Images/alien.png")
    health = 100 

    def __init__(self, x, y):

        self.direction = "w"
        self.health = Enemy.health
        self.img = Enemy.original_img
        Character.__init__(self, x, y)
        Enemy.List.append(self)

    @staticmethod
    def update(screen,player):

        for enemy in Enemy.List:
            screen.blit(enemy.img,(enemy.x, enemy.y))

            if player.x % Tile.width == 0 and player.y % Tile.height == 0:
                if enemy.x % Tile.width == 0 and enemy.y % Tile.height == 0:

                    tn = player.get_number()

                    N = tn + -(Tile.V)
                    S = tn + (Tile.V)
                    E = tn + (Tile.H)
                    W = tn + -(Tile.H)

                    NSEW = [N,S,E,W,tn]

                    if enemy.get_number() in NSEW:
                        player.health -= randint(0,15)
    
            if enemy.health <= 0:
                Enemy.List.remove(enemy)

            if enemy.tx != None and enemy.ty != None:

                X = enemy.x - enemy.tx
                Y = enemy.y - enemy.ty

                vel = 4

                if X < 0: # right
                    enemy.x += vel
                    enemy.rotate("e",Enemy.original_img)
                    
                elif X > 0:# left
                    enemy.x -= vel
                    enemy.rotate("w",Enemy.original_img)

                if Y > 0: #up
                    enemy.y -= vel
                    enemy.rotate("n",Enemy.original_img)
                    
                elif Y < 0:#down
                    enemy.y += vel
                    enemy.rotate("s",Enemy.original_img)

                if X == 0 and Y == 0:
                    enemy.tx, enemy.ty = None, None

    @staticmethod
    def spawn(total_frames, FPS):
        if total_frames % (FPS*2) == 0:
            r = randint(0,len(Enemy.spawn_tiles)-1)
            tile_num = Enemy.spawn_tiles[r]
            spawn_node = Tile.get_tile(tile_num)
            Enemy(spawn_node.x, spawn_node.y)
            Enemy.health = randint(0,400)
            
            

class Player(Character):

    def __init__(self, x, y):

        self.health = randint(300,800)
        self.current = 0 # = pistol, 1 = shotgun 3 = automatic  
        self.direction = "w"
        self.img = pygame.image.load('Images/spaceship_w.png')
        
        Character.__init__(self, x, y)

    def get_bullet_type(self):

        if self.current == 0:
            return 'pistol'
        elif self.current == 1:
            return 'shotgun'
        elif self.current == 2:
            return 'automatic'
            
    
    def movement(self):

       if self.tx != None and self.ty != None:

            X = self.x - self.tx
            Y = self.y - self.ty

            vel = 8

            if X < 0: # right
                self.x += vel
            elif X > 0:# left
                self.x -= vel

            if Y > 0: #up
                self.y -= vel
            elif Y < 0:#down
                self.y += vel

            if X == 0 and Y == 0:
                self.tx, self.ty = None, None

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def rotate(self, direction):

        path = 'Images/spaceship_'
        png = '.png'
        
        if direction == "n":
            if self.direction != "n":
                self.direction = "n"
                self.img = pygame.image.load(path + self.direction + png)

        if direction == "s":
            if self.direction != "s":
                self.direction = "s"
                self.img = pygame.image.load(path + self.direction + png)

        if direction == "e":
            if self.direction != "e":
                self.direction = "e"
                self.img = pygame.image.load(path + self.direction + png)
            
        if direction == "w":
            if self.direction != "w":
                self.direction = "w"
                self.img = pygame.image.load(path + self.direction + png)


class Bullet(pygame.Rect):

    width, height = 7,10
    List = []

    imgs = {'pistol':pygame.image.load('Images/pistol_b.png'),
            "shotgun" :pygame.image.load('Images/shotgun_b.png'),
            'automatic':pygame.image.load('Images/automatic_b.png')
            }

    gun_dmg = {'pistol' : (Enemy.health //3),
               'shotgun' : (Enemy.health //2),
               'automatic' : (Enemy.health //6)
               }
    
    def __init__(self, x, y, velx, vely, direction, type_):

        if type_ == "shotgun" or type_ == "pistol":
            try:
                dx = abs(Bullet.List[-1].x - x)
                dy = abs(Bullet.List[-1].y - y)

                if dx < 100 and dy < 100 and type_ == "shotgun":
                    return

                if dx < 40 and dy < 40 and type_ == "pistol":
                    return
            except:
                pass

        self.type = type_
        self.direction = direction
        self.velx, self.vely = velx, vely

        
        if direction == "n":
            south = pygame.transform.rotate(Bullet.imgs[type_], 90)
            self.img = pygame.transform.flip(south, False,True)

        if direction == "s":           
            self.img = pygame.transform.rotate(Bullet.imgs[type_], 90)

        if direction == "e":
            self.img = pygame.transform.flip(Bullet.imgs[type_], True, False)
            
        if direction == "w": 
            self.img = Bullet.imgs[type_]


        pygame.Rect.__init__(self,x,y,Bullet.width,Bullet.height)
        Bullet.List.append(self)


    def offscreen(self,screen):

        if self.x < 0:
            return True
        elif self.y < 0:
            return True
        elif self.x + self.width > screen.get_width():
            return True
        elif self.y + self.height > screen.get_height():
            return True
        else:
            return False

    @staticmethod
    def super_massive_jumbo_loop(screen):

        for bullet in Bullet.List:

            bullet.x += bullet.velx
            bullet.y += bullet.vely

            screen.blit(bullet.img, (bullet.x,bullet.y))

            #is it offscreen

            if bullet.offscreen(screen):
                Bullet.List.remove(bullet)
                continue

            for enemy in Enemy.List:

                if bullet.colliderect(enemy):
                    enemy.health -= Bullet.gun_dmg[bullet.type]
                    Bullet.List.remove(bullet)
                    break

            for tile in Tile.List:

                if bullet.colliderect(tile)and not(tile.walkable):
                    try:
                        Bullet.List.remove(bullet)
                    except:
                        break

                    
