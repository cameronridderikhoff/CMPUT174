#Hacker Game V1:
#Authors: Cameron Ridderikhoff, Geping Xu
#When the game starts, a 500 pixels wide by 400 pixels high window and with the 
#title , instructions are displayed, explaining how the game works. 
#Words are then displayed in ALL CAPS. Each are on separate lines. 
#The user is then prompted for their guess at the password, number of guesses 
#remaining displayed. 
#If the word is correct, a congratulation message is displayed. 
#If the number of guesses now equals 0 and the guess is incorrect, 
#there is a condolence message displayed. 
#If the user still has more guesses, the program checks to see if any letters 
#are correct, an VM or on the lab cod in the correct location, and displays the number of correct 
#letters. 
#The program then prompts the user to try again, 
#until the user is out of guesses. 
#When the game is over, a prompt for the enter key to end the game is 
#displayed in the bottom left corner. 
#When pressed, the window closes and the game ends. 
#(All other writing starts in the top left, and goes down. 
#No words are erased, and neither are the previous guesses. 
#All text is 24pt font. White text on a black background.)


import pygame
import uaio

def main():

    # create window
    pygame.init()
    surfaceSize = (800, 800)
    surfaceX=1000
    surfaceY=800
    surface = pygame.display.set_mode(surfaceSize, 0, 0)
    pygame.display.set_caption('Hacker!!!')
    
    words = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING']
    answer = 'SURVIVE'
    
    # display instructions
    textX=0;
    textY=0;
    height=uaio.get_height('A group of possible passwords will be displayed.')
    uaio.draw_string('A group of possible passwords will be displayed.', surface, (textX, textY))
    textY = textY + height
    uaio.draw_string('You must guess the password. You have at most 4 guesses.', surface, (textX, textY))
    textY = textY + height
    uaio.draw_string('If you are incorrect you will be told how many letters in', surface, (textX, textY))
    textY = textY + height
    uaio.draw_string('your guess were exactly the correct location of the password.', surface, (textX, textY))
    textY = textY + height
    
    # display words
    uaio.draw_string('PROVIDE', surface, (textX, textY))
    textY = textY + height
    uaio.draw_string('SETTING', surface, (textX, textY))
    textY = textY + height
    uaio.draw_string('CANTINA', surface, (textX, textY))
    textY = textY + height       
    uaio.draw_string('CUTTING', surface, (textX, textY))
    textY = textY + height
    uaio.draw_string('HUNTERS', surface, (textX, textY))
    textY = textY + height    
    uaio.draw_string('SURVIVE', surface, (textX, textY))
    textY = textY + height    
    uaio.draw_string('HEARING', surface, (textX, textY))
    textY = textY + height    
    uaio.draw_string('HUNTING', surface, (textX, textY))
    textY = textY + height  
    uaio.draw_string('REALIZE', surface, (textX, textY))
    textY = textY + height
    uaio.draw_string('NOTHING', surface, (textX, textY))
    textY = textY + height
    uaio.draw_string('OVERLAP', surface, (textX, textY))
    textY = textY + height
    uaio.draw_string('FINDING', surface, (textX, textY))
    textY = textY + height
    uaio.draw_string('PUTTING', surface, (textX, textY))
    textY = textY + height    

    guess = uaio.input_string('Enter Password>', surface, (textX, textY))
    textY = textY + height
    
    #check answer and display result
    if guess == answer:
        uaio.draw_string('User login successful', surface, (textX, textY))
    else:
        uaio.draw_string('User login unsuccessful', surface, (textX, textY))
    
    
    textY = surfaceY - height
    uaio.input_string('Press enter to exit', surface, (textX, textY))
    
    # end game
    pygame.quit()
      
main()