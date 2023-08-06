import pygame

import pygame

#Initiailze pygame
pygame.init()

#Create a display surface and set its caption
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

#Define colors as RGB Tuples 
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#Give Background color to display 
display_surface.fill(BLUE)

#Draw Shapes  
#Line(Surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0,0), (100,100), 5)
pygame.draw.line(display_surface, MAGENTA, (100,100), (200,300), 2)

#Circle(Surface, color, center, radius, thickness...0 for fill)
pygame.draw.circle(display_surface, CYAN, (300,300), 100, 3)

#Rectangle (surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, GREEN, (500, 0, 100, 100))

#The main game loop
running = True

while running:
    #Loop through a list of Event objects that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

#End the game
pygame.quit()