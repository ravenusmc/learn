import pygame

# Init pygame
pygame.init()

# Display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Continous Movement")

# Set game values
MOVEMENT = 5

#Set FPS 
FPS = 60
clock = pygame.time.Clock()

# Load Images
dragon_image = pygame.image.load('../images/dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
# dragon_rect.bottom = WINDOW_HEIGHT

# The main game loop
running = True
while running:
    # Loop through a list of Event objects that have occured
    for event in pygame.event.get():
        # print(event)
        keys = pygame.key.get_pressed()
        # keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
    # check for movement
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= MOVEMENT
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += MOVEMENT
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= MOVEMENT
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += MOVEMENT

    # Fill display Surface to cover old image
    display_surface.fill((0, 0, 0))
    # Blit a surface to our display
    display_surface.blit(dragon_image, dragon_rect)
    # Update the display
    pygame.display.update()
    #tick the click 
    clock.tick(FPS)

# End the game
pygame.quit()
