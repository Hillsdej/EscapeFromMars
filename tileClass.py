import pygame, Func

class Tile(pygame.Rect):
 
    List = [] 
    width, height = 32,32
    total_tiles = 1
    H, V = 1,30
    
    def __init__(self, x, y, Type):

        self.parent = None
        self.H, self.G, self.F = 0,0,0
        
        self.type = Type
        self.number = Tile.total_tiles 
        Tile.total_tiles += 1

        if Type == 'empty':
            self.walkable = True
        else:
            self.walkable = False

        pygame.Rect.__init__(self,(x, y),(Tile.width, Tile.height))

        Tile.List.append(self)

    @staticmethod
    def get_tile(number):
        for tile in Tile.List:
            if tile.number == number:
                return tile

    @staticmethod
    def draw_tiles(screen):
        half = Tile.width // 2
        
        for tile in Tile.List:
            pass
                   
