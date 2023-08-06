import pygame
import random 

# Init pygame
pygame.init()

# Display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection")

# Set game values
VELOCITY = 5

# Set FPS
FPS = 60
clock = pygame.time.Clock()

# Load Images
dragon_image = pygame.image.load('../images/dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (25,25)

coin_image = pygame.image.load('../images/coin.png')
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

# The main game loop
running = True
while running:
    # Loop through a list of Event objects that have occured
    for event in pygame.event.get():
        print(event)
        
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
     # check for movement
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.left > 0:
        dragon_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.right < WINDOW_WIDTH:
        dragon_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.top > 0:
        dragon_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.bottom < WINDOW_HEIGHT:
        dragon_rect.y += VELOCITY
    
    #Check For collision 
    if dragon_rect.colliderect(coin_rect):
        # print('Hit')
        coin_rect.left = random.randint(0, WINDOW_WIDTH - 32)
        coin_rect.top = random.randint(0, WINDOW_HEIGHT - 32)

    # Fill display Surface to cover old image
    display_surface.fill((0, 0, 0))
    # Draw Rectangles 
    pygame.draw.rect(display_surface, (255,0,0), dragon_rect, 1)
    pygame.draw.rect(display_surface, (255,0,0), coin_rect, 1)
    # Blit a surface to our display
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)
    # Update the display
    pygame.display.update()
    # tick the click
    clock.tick(FPS)

    pygame.display.update()

# End the game
pygame.quit()
