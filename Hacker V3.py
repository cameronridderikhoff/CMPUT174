#Hacker Game V3:
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

import uaio
import pygame
import random

def main():
    
    surface = createWindow()
    location = [0, 0]
    location = displayInstructions(surface, location)
    location = displayWords(surface, location)
    #checkAnswer will run until the user is out of guesses
    didPlayerWin = checkAnswer(surface, location) #check answer starts with a prompt for the guess
    
    displayResult(surface, location, didPlayerWin)
    
def createWindow():
    # create window
    pygame.init()
    surfaceX=800
    surfaceY=800
    surface = pygame.display.set_mode((surfaceX, surfaceY), 0, 0)
    pygame.display.set_caption('Hacker!!!')  
    return surface

def displayInstructions(surface, location):
    # display instructions
    instructions = ['A group of possible passwords will be displayed.','You must guess the password. You have at most 4 guesses.','If you are incorrect you will be told how many letters in','your guess were exactly the correct location of the password.']
    height=uaio.get_height('Test.')
    for  instruction in instructions:
        uaio.draw_string(instruction, surface, location)
        location[1] = location[1] + height
    return location
        
def displayWords(surface, location):
    # display words
    words = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING'] 
    height = uaio.get_height('TEST')
    for  word in words:
        uaio.draw_string(word, surface, location)
        location[1] = location[1] + height
    return location

def promptForGuess(surface, numGuesses, location):
    guess = uaio.input_string('Enter Password (' + str(numGuesses) + ' guesses remaining)>', surface, location)
    return guess

def checkAnswer(surface, location):
    #check answer 
    numberGuesses = 4 
    words = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING']
    answerPosition = random.randint(0, len(words)-1)
    answer = words[answerPosition]
    print(answer)
    height = uaio.get_height('TEST')
    
    while numberGuesses > 0:
        guess = promptForGuess(surface, numberGuesses, location)
        location[1] = location[1] + height
        correctLetters=0 #the number of correct letters in the guess  
        indexRange = min(len(answer), len(guess))
        for index in range(indexRange):
            if guess[index] == answer[index]:
                correctLetters = correctLetters+1
            
        if correctLetters == len(answer):#player guesses all the correct letters
            numberGuesses = 0
        else:
            numberGuesses = numberGuesses - 1
            if numberGuesses > 0:
                uaio.draw_string('Password Incorrect', surface, location)
                location[1] = location[1] + height 
                uaio.draw_string(str(correctLetters) + '/' + str(len(answer)) + ' correct.', surface, location)
                location[1] = location[1] + height            
                
    return correctLetters == len(answer) #this statement evalutes to either true or false

def displayResult(surface, location, win):
    #display result
    height = uaio.get_height("Test.")
    if  win:
        uaio.draw_string('User login successful', surface, location)
    else:
        uaio.draw_string('User login unsuccessful', surface, location)
    surfaceHeight = pygame.Surface.get_height(surface)
    location[1] =  surfaceHeight - height
    uaio.input_string('Press enter to exit', surface, location)
    endGame()

def endGame():
    # end game
    pygame.quit()    
main()