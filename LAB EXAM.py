# Exemplar Graphics-5
# This is an example program that contains graphics using
# the pygame module, contains user-defined classes, and 
# responds to multiple kinds of events.
# It contains these kinds of statements: expression, assignment,
# import, function definition, while, for, if, return, class
# definition
# It contains these kinds of expressions: identifier, literal,
# attribute reference, function call, binary operator, expression
# list
# It uses these types: str, int, float, bool, NoneType, function,
# module, tuple, pygame.Surface, pygame.Color, pygame.Rect, Game,
# Circle

import pygame, time, random
from pygame.locals import *

# User-defined functions

def main():

   surface = create_window()
   game = Game(surface)
   game.play()
   pygame.quit()

def create_window():
    # Open a window on the display and return its Surface
    
   title = 'Jump'
   size = (500, 400)
   pygame.init()
   surface = pygame.display.set_mode(size, 0, 0)
   pygame.display.set_caption(title)
   return surface

# User-defined classes

class Circle:
   # An object in this class represents a colored circle.

   def __init__(self, center, radius, color, surface):
      # Initialize a Cirlcle.
      # - self is the Circle to initialize
      # - center is a list containing the x and y int
      # coords of the center of the Circle
      # - radius is the int pixel radius of the Circle
      # - color is the pygame.Color of the Circle
      # - surface is the window's pygame.Surface object

      self.center = center
      self.radius = radius
      self.color = color
      self.surface = surface
   
   def draw(self):
      # Draw the Circle.
      # - self is the Circle to draw
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)
   
   def jump(self, position):
      # Move the circle to the mouse's position.
      # - self is the Circle to move
      self.center=position
      if self.is_outside():
         self.color=pygame.Color("yellow")
      else:
         self.color=pygame.Color("blue")
      
   def is_outside(self):
      #checks to see if any part of the circle is outside the surface
      if (self.center[0]<self.radius) or (self.center[0]>self.surface.get_width()-self.radius):
         return True
      if (self.center[1]<self.radius) or (self.center[1]>self.surface.get_height()-self.radius):
         return True
      return False
   
   def set_color(self, color):
      self.color=color
      
   def get_color(self):
      # Return the color of the Circle.
      # - self is the Circle
      
      return self.color
   
   def enlarge(self, increment):
      # Enlarge the radius of the Circle.
      # - self is the Circle
      # - increment is the int number of pixels
      # to add to the radius
      
      self.radius = self.radius + increment

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the window's pygame.Surface object
      
      self.surface = surface
      self.bg_color = pygame.Color('black')
      self.pause_time = 0.01 # smaller is faster game
      self.close_clicked = False
      self.continue_game = True
      pos = [random.randint(50, surface.get_width()-50), random.randint(50, surface.get_height()-50)]
      self.circle = Circle(pos, 50, pygame.Color('blue'), surface)
      self.elapsed_time = 0
      self.radius_increment = 5

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      self.draw()
      while not self.close_clicked: # until player clicks close box
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
      # - self is the Game whose events will be handled

      event = pygame.event.poll()
      if event.type == QUIT:
         self.close_clicked = True
      elif event.type == MOUSEBUTTONUP and self.continue_game:
         self.handle_mouse_up(event.pos)

   def handle_mouse_up(self, position):
      # Respond to the player releasing the mouse button by
      # taking appropriate actions.
      # - self is the Game where the mouse up occurred
      self.circle.jump(position)
     

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color)
      self.circle.draw()
      if not self.continue_game:
         # Perform appropriate game over actions
         self.surface.fill(self.circle.get_color())
      pygame.display.update()

   def update(self):
      # Update the game objects.
      # - self is the Game to update
      
      self.elapsed_time = pygame.time.get_ticks() // 1000
         
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      
      pass

main()
