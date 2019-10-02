# Pong V1
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
# Ball

import pygame, time
from pygame.locals import *

# User-defined functions

def main():

   surface = create_window()
   game = Game(surface)
   game.play()
   pygame.quit()

def create_window():
    # Open a window on the display and return its Surface
    
   title = 'Pong (the game)'
   size = (500, 400)
   pygame.init()
   surface = pygame.display.set_mode(size, 0, 0)
   pygame.display.set_caption(title)
   return surface

# User-defined classes

class Ball:
   # An object in this class represents a colored Ball.

   def __init__(self, center, radius, color, surface, velocity):
      # Initialize a Ball.
      # - self is the Ball initialize
      # - center is a list containing the x and y int
      # coords of the center of the Ball
      # - radius is the int pixel radius of the Ball
      # - color is the pygame.Color of the Ball
      # - surface is the window's pygame.Surface object

      self.center = center
      self.radius = radius
      self.color = color
      self.surface = surface
      self.velocity = velocity
   
   def draw(self):
      # Draw the Ball.
      # - self is the Ball to draw
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)
   
   def move(self):
      # Move the Ball.
      # - self is the Ball to move
      
      surface_size = self.surface.get_size()
      for index in range(0, 2):
         self.center[index] = (self.center[index] + self.velocity[index]) % surface_size[index]

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the window's pygame.Surface object
      
      self.surface = surface
      self.bg_color = pygame.Color('black')
      self.pause_time = 0.009 # smaller is faster game
      self.close_clicked = False
      self.continue_game = True
      self.ball = Ball([250, 200], 5, pygame.Color('white'), surface, [3, 1])
      self.left_paddle = pygame.Rect(75, ((self.surface.get_height()/2) - (0.5*30)), 10, 45) #parameters are (x, y, length, width)
      self.right_paddle = pygame.Rect((self.surface.get_width()-75)-10, (self.surface.get_height()/2)-(0.5*30), 10, 45)

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

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color)
      self.ball.draw()
      pygame.draw.rect(self.surface, pygame.Color('white'), self.left_paddle)
      pygame.draw.rect(self.surface, pygame.Color('white'), self.right_paddle)
      pygame.display.update()

   def update(self):
      # Update the game objects.
      # - self is the Game to update
      
      self.ball.move()
         
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      pass

main()
