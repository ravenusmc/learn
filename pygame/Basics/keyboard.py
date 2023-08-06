import pygame

#Init pygame 
pygame.init()

# Display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Basic Movement")

#Set game values 
VELOCITY = 10

#Load Images 
dragon_image = pygame.image.load('../images/dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH//2
dragon_rect.bottom = WINDOW_HEIGHT

# The main game loop
running = True
while running:
    # Loop through a list of Event objects that have occured
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        #check for movement 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x  -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x  += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y  -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y  += VELOCITY
    #Fill display Surface to cover old image 
    display_surface.fill((0,0,0))
    #Blit a surface to our display
    display_surface.blit(dragon_image, dragon_rect)
    #Update the display
    pygame.display.update()

# End the game
pygame.quit()