import pygame
from sys import exit

pygame.init()

# Create the screen. The method receives a tuple that contains width and height
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("test")

# Create a font. It receives the path for the font type file
font = pygame.font.Font('font/Pixeltype.ttf', 50)
font_surface = font.render("El jueguito", False, "Black")

# Load images. Receives a path for the image
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
snail_surface = pygame.image.load('graphics/snail/snail1.png')

# The clock object helps to set the frame rate
clock = pygame.time.Clock()

# Position variables
snail_x = 650

# We use a while True loop to keep everything
while True:
	# Iterate from all the events happening
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # If you click de X button of the window
			pygame.quit()
			exit() 

	# Add the surfaces
	screen.blit(sky_surface, (0, 0))
	screen.blit(ground_surface, (0, 300))
	screen.blit(font_surface, (300, 50))
	screen.blit(snail_surface, (snail_x, 260))
	snail_x -= 4

	# If the snail reached the left side of the display, it returns to the position of before
	if snail_x < -90: 
		snail_x = 800

	pygame.display.update() 
	
	# Set the framerate
	clock.tick(60)