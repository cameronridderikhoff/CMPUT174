# This is an example program that contains graphics, using
# modules pygame and uaio and responds to a close window event.
# It contains these kinds of statements: expression, assignment,
# import, function definition, while, return, class definition
# It contains these kinds of expressions: identifier, literal,
# attribute reference, function call, binary operator, expression
# list
# It uses these types:
# str, int, float, bool, NoneType, function, module, tuple
# pygame.Surface, pygame.Color, pygame.Rect, Game








import pygame
import time
import random
from pygame.locals import *




# User-defined functions




def main():


    surface = create_window()
    game = Game(surface)
    game.play()
    pygame.quit()
    
def create_window():
    # Open a window on the display and return its Surface
    
    title = 'Memory'
    size = (500, 400)
    pygame.init()
    surface = pygame.display.set_mode(size, 0, 0)
    pygame.display.set_caption(title)
    return surface




# User-defined classes




class Game:
    # An object in this class represents a complete game.




    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the window's pygame.Surface object
        
        self.surface = surface
        Tile.set_surface(surface)
        self.bg_color = pygame.Color('black')
        self.pause_time = 0.04 # smaller is faster game
        self.close_clicked = False
        self.continue_game = True
        self.tiles = []
        Tile.set_unclicked_image(pygame.image.load('question.bmp'))
        score=0
        self.image_list = []
        
        for index in range(0, 8):
            image = pygame.image.load('image'+str(index)+'.bmp')
            self.image_list.append(image)
        self.image_list = self.image_list + self.image_list
        
        self.create_grid()
        
    def create_grid(self):
        #creates the grid of tiles
        tile_width = self.surface.get_width() // 5
        tile_height = self.surface.get_height() // 4
        for row in range(0, 4):
            row_list = []
            for column in range(0, 4):
                x_coord = column * tile_width
                y_coord = row * tile_height
                tile_type = random.randint(0, len(self.image_list)-1)
                image = self.image_list[tile_type]
                self.image_list.remove(image)
                #FIX
                value = tile_type % 8
                
                tile = Tile(x_coord, y_coord, tile_width, tile_height, image, value)
                row_list.append(tile)
            self.tiles.append(row_list)
        
    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.
        
        self.draw()
        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_event()
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.draw()
            time.sleep(self.pause_time) # set game velocity by pausing
                       
    def handle_event(self):
        # Handle each user event by changing the game state
        # appropriately.
        # - self is the Game whose events will be handled.

        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True
        if event.type == MOUSEBUTTONUP and self.continue_game:
            self.handle_mouse_up(event)
        
    def handle_mouse_up(self, event):
        #handles the mouse up event
        for row in self.tiles:
            for tile in row:
                tile.click(event.pos)
                
    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        
        self.surface.fill(self.bg_color)
        
        self.draw_score()
        for row in self.tiles:
            for tile in row:
                tile.draw()
        pygame.display.update()
        
    def draw_score(self):
        size=40
        y=0
        width=uaio.get_width(str(self.score), size)
        x=self.surface.get_width() - width
        uaio.draw_string(str(self.score), self.surface, (x, y), size)
        
    def update(self):
        # Update the game objects.
        # - self is the Game to update
        
        self.score = pygame.time.get_ticks() // 1000
        
        stop=True
        for row in self.tiles:
            for tile in row:
                if not tile.flipped:
                    stop=False
        if stop:
            continue_game = False
             
    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
       
        pass
    
class Tile:
    @classmethod
    def set_surface(cls, surface):
        cls.surface = surface
        
    @classmethod
    def set_unclicked_image(cls, image):
        cls.unclicked_image = image
        
    border_width = 3
    fg_color = pygame.Color('black')
    
    
    def __init__(self, x, y, width, height, image, value):
        self.rectangle = Rect(x, y, width, height)
        self.image = image
        self.value = value
        self.flipped=False
        
    def draw(self):
        # Draw the tile
        pygame.draw.rect(Tile.surface, Tile.fg_color, self.rectangle, Tile.border_width)
        
        # Draw the image
        image_x = self.rectangle.left + self.border_width
        image_y = self.rectangle.top + self.border_width
        if self.flipped:
            self.surface.blit(self.image, (image_x, image_y))
        else:
            self.surface.blit(Tile.unclicked_image, (image_x, image_y))
        
    def click(self, position):
        #check to see if the tile was clicked
        if self.rectangle.collide_point(position):
            self.flipped=True
main()
