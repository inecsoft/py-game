import pygame
from math import pi, sin, sqrt, cos
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN)


# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

pygame.init()

#set up the drawing window
screen = pygame.display.set_mode((600,600))

#running untill the user exits
running = True

while running:
    # if the user clicked on the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen with white background
    screen.fill((255,255,255))
     
    # RGB
    pygame.draw.circle(screen,(255,0,255),(250,250),300)
    pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
    
    #surface, angle
    #pygame.transform.rotate()

    # Flip the display
    pygame.display.flip()

#Done! time to quit
pygame.quit()
