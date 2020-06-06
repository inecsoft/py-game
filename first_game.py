import pygame
# Import and initialize the pygame library
pygame.init()

#set up the drawing window
screen = pygame.display.set_mode((500,500))

#running untill the user exits
running = True

while running:
    # if the user clicked on the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill screen with white background
    screen.fill((255,255,255))
    
    # Draw a solid blue circle in the centre
    pygame.draw.circle(screen,(0,0,255),(250,250), 30)

    pygame.draw.square(screen,(20,20,20) ,(40,50), 40)    

    # Flip the display
    pygame.display.flip()

#Done! time to quit
pygame.quit()
