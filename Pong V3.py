# Pong V3
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


import pygame, time, uaio
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
      self.right_score = 0
      self.left_score = 0
   
   def draw(self):
      # Draw the Ball.
      # - self is the Ball to draw
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)
   
   def move(self):
      # Move the Ball.
      # - self is the Ball to move
      
      surface_size = self.surface.get_size()
      for coord in range(0, 2):
         self.center[coord] = self.center[coord] + self.velocity[coord]
         if self.center[coord] < self.radius:
            self.velocity[coord] = -self.velocity[coord]
            if coord == 0:
               self.right_score += 1
         if self.center[coord] > surface_size[coord] - self.radius:
            self.velocity[coord] = -self.velocity[coord]
            if coord == 0:
               self.left_score += 1


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
      pygame.key.set_repeat(20, 20)

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
      speed = 6
      if event.type == QUIT:
         self.close_clicked = True
         
      if event.type == KEYDOWN and self.continue_game:
         if pygame.key.get_pressed()[K_q]:
            if self.left_paddle.top > speed:
               self.left_paddle.top = self.left_paddle.top - speed
               print(type(event.type))
            else:
               self.left_paddle.top = 0 
         if pygame.key.get_pressed()[K_a]:
            if self.left_paddle.top + self.left_paddle.height + speed < self.surface.get_height():
               self.left_paddle.top = self.left_paddle.top + speed
            else:
               self.left_paddle.top = self.surface.get_height() - self.left_paddle.height
      
         if pygame.key.get_pressed()[K_p]:
            if self.right_paddle.top > speed:
               self.right_paddle.top = self.right_paddle.top - speed
            else:
               self.right_paddle.top = 0                
         if pygame.key.get_pressed()[K_l]:
            if self.right_paddle.top + self.right_paddle.height + speed < self.surface.get_height():
               self.right_paddle.top = self.right_paddle.top + speed
            else:
               self.right_paddle.top = self.surface.get_height() - self.right_paddle.height
            


   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color)
      self.ball.draw()
      pygame.draw.rect(self.surface, pygame.Color('white'), self.left_paddle)
      pygame.draw.rect(self.surface, pygame.Color('white'), self.right_paddle)
      self.draw_score()
      pygame.display.update()
      
   def draw_score(self):
      size = 50
      xcoord = self.surface.get_width() - uaio.get_width(str(self.ball.right_score), size)
      uaio.draw_string(str(self.ball.left_score), self.surface, (0,0), size)
      uaio.draw_string(str(self.ball.right_score), self.surface, (xcoord,0), size)


   def update(self):
      # Update the game objects.
      # - self is the Game to update
      
      self.ball.move()
      if self.ball.velocity[0] > 0:
         self.collide_paddle(self.right_paddle)
      else:
         self.collide_paddle(self.left_paddle)
         
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      if self.ball.right_score == 11 or self.ball.left_score == 11:
         self.continue_game = False
         
   def collide_paddle(self, paddle):
      if paddle.collidepoint(self.ball.center):
         self.ball.velocity[0] = -self.ball.velocity[0]


main()