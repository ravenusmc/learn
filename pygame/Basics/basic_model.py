import pygame

#Init pygame 
pygame.init()

# Display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Basic ")

#


# The main game loop
running = True
while running:
    # Loop through a list of Event objects that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# End the game
pygame.quit()