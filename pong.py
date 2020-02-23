#!/usr/bin/python
import sys
import os
import pygame

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Defining colors
black = (0,0,0)
white = (255,255,255)





# Defining clock for time render 
clock = pygame.time.Clock()

# Try to start the game
try: pygame.init()
except: print('Error when trying to start pygame')

# Screen dimensions
width = 600
height = 440

# Setting the dimensions for the game
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pong!")

# Defining the initial score
playerOneScore = 0
playerTwoScore = 0

# Position of the paddles
playerOnePositionX = 20
playerOnePositionY = 170
playerTwoPositionX= 560
playerTwoPositionY = 170

# Initial position of the Ball
ballPositionX = 280
ballPositionY = 200

# Var for the ball velocity
ballVelocityX = 3
ballVelocityY = 3

# Pause controll
pause = False

# Var for exit controll
exit = True

# Colision sound

colissionWav = resource_path('assets/collision.wav')
ColisionEffect = pygame.mixer.Sound(colissionWav)

while exit:
    # Key to catch events
    key = pygame.key.get_pressed()
    
    # Getting the text-fonts
    gamePlayFont = resource_path('assets/Gameplay.ttf')
    font = pygame.font.Font(gamePlayFont, 20)
    textPlayerOne = font.render("Player 1", True, white)
    textPlayerTwo = font.render("Player 2", True, white)
    text = font.render("PAUSE", True, white)
    
    # Score texts
    scorePlayerOneText = font.render("{}".format(playerOneScore), True, white)
    scorePlayerTwoText = font.render("{}".format(playerTwoScore), True, white)

    # Creating the objects
    textPlayerOneRect = textPlayerOne.get_rect()
    textPlayerOneRect.center = (150,20)
    textPlayerTwoRect = textPlayerTwo.get_rect()
    textPlayerTwoRect.center = (450,20)
    textRect = text.get_rect()
    textRect.center = (300,220)
    scorePlayerOneTextRect = textPlayerOne.get_rect()
    scorePlayerOneTextRect.center = (150,50)
    scorePlayerTwoTextRect = textPlayerTwo.get_rect()
    scorePlayerTwoTextRect.center = (450,50)
    
   # Catch the pause command
    if pause:
        screen.blit(text,textRect)
        pygame.display.update()       
    for event in pygame.event.get():      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
        if event.type == pygame.QUIT:
            exit = False
    if pause: continue
    
    # Middle line
    pygame.draw.line(screen, white, (300,0),(300,440),4)
    pygame.display.update()
    pygame.display.flip()
    
    # Moviment Commands
    if key[pygame.K_w] and playerOnePositionY > 0: playerOnePositionY -= 4
    if key[pygame.K_s] and playerOnePositionY < 340 : playerOnePositionY += 4
    if key[pygame.K_UP] and playerTwoPositionY > 0 : playerTwoPositionY -= 4
    if key[pygame.K_DOWN] and playerTwoPositionY < 340 : playerTwoPositionY += 4
    
    # Background color
    screen.fill(black)
    
    # Collision controll
    if ballPositionX >= 580:
        ballPositionX = 280
        ballPositionY = 200
    
        ballVelocityX *= -1
        playerOneScore += 1
        ballVelocityX = 3
        ballVelocityY = 3
        ballVelocityX *= -1
        
    if ballPositionX < 1:
        ballPositionX = 280
        ballPositionY = 200
 
        ballVelocityX *= -1
        playerTwoScore +=1
        ballVelocityX = 3
        ballVelocityY = 3
        
    if ballPositionY > 419:
        ballVelocityY *= -1
        
    if ballPositionY < 1:
        ballVelocityY *= -1

    # Placing the objects
    j1 = pygame.draw.rect(screen, white, [playerOnePositionX,playerOnePositionY,20,100])
    j2 = pygame.draw.rect(screen, white, [playerTwoPositionX,playerTwoPositionY,20,100])
    ball = pygame.draw.rect(screen, white, [ballPositionX,ballPositionY,20,20])
    
    # Collision effects
    if j1.colliderect(ball):
        ColisionEffect.play()        
        if ballVelocityX < 0:
            ballVelocityX -= 0.2
            ballVelocityY -= 0.2
        else :
            ballVelocityX += 0.2
            ballVelocityY += 0.2
        ballPositionX += 3
        ballVelocityX *= -1
    if j2.colliderect(ball):
        ColisionEffect.play()
        if ballVelocityX < 0:
            ballVelocityX -= 0.2
            ballVelocityY -= 0.2
        else :
            ballVelocityX += 0.2
            ballVelocityY += 0.2  
        ballPositionX -= 3
        ballVelocityX *= -1
        
    # Printing the texts
    screen.blit(textPlayerOne,textPlayerOneRect)
    screen.blit(textPlayerTwo,textPlayerTwoRect)
    screen.blit(scorePlayerOneText,scorePlayerOneTextRect)
    screen.blit(scorePlayerTwoText,scorePlayerTwoTextRect)
    
    # Ball moviment
    ballPositionX += ballVelocityX
    ballPositionY += ballVelocityY
    clock.tick(100)
    
pygame.quit()

##mudei algo aqui foi mal
