import pygame

#Init pygame 
pygame.init()

# Display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Music and Sound")

#Load sounds 
sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

#Play the sound
sound_1.play()
pygame.time.delay(2000)
#Change the volume 
sound_2.set_volume(.1)
sound_2.play()
pygame.time.delay(2000)

#Load Music 
pygame.mixer.music.load('music.wav')

#play and stop the music 
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(5000)
pygame.mixer.music.stop()

# The main game loop
running = True
while running:
    # Loop through a list of Event objects that have occured
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    #Blit a surface to our display

    pygame.display.update()

# End the game
pygame.quit()