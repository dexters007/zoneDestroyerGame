import pygame
import random

pygame.init()

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

player = pygame.image.load("face.png")
borderTop = pygame.image.load("border.png")
borderBottom = pygame.image.load("border.png")
borderLeft = pygame.image.load("border1.png")
borderRight = pygame.image.load("border1.png")


player_height = player.get_height()
player_width = player.get_width()


playerXPosition = 40
playerYPosition = 500

borderTopXPosition = 0
borderTopYPosition = 0

borderBottomXPosition = 0
borderBottomYPosition = 640

borderLeftXPosition = 0
borderLeftYPosition = 0

borderRightXPosition = 1000
borderRightYPosition = 0

# create conditions to check if buttons are pushed

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

playerXSpeed = 0
playerYSpeed = 0



while 1:
    screen.fill(0)
    screen.blit(player, (playerXPosition,playerYPosition))
    screen.blit(borderTop, (borderTopXPosition,borderTopYPosition))
    screen.blit(borderBottom, (borderBottomXPosition,borderBottomYPosition))
    screen.blit(borderLeft, (borderLeftXPosition,borderLeftYPosition))
    screen.blit(borderRight, (borderRightXPosition,borderRightYPosition))

    pygame.display.flip()

    for event in pygame.event.get():

        # Check if the user quits the game

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Check if user presses the keys down

        if event.type == pygame.KEYDOWN:
            
            # Test if right buttons are pushed

            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # Check when button is released

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # Check if buttons are pushed

    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -=1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition +=1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -=1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition +=1

    if player_width < 40:
        player_width += 40
    
    if player_height <= 40:
        player_height += 40


