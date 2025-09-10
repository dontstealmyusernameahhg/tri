import pygame
import os
pygame.init()
white = (255, 255, 255)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 900))
pygame.display.set_caption("◉_◉")

image_path = os.path.join(os.path.dirname(__file__), "robloxgag.png")
try:
	pygameimage = pygame.image.load(image_path)
	# Scale image proportionally to fit within screen size
	img_rect = pygameimage.get_rect()
	max_width, max_height = 800, 700
	scale = min(max_width / img_rect.width, max_height / img_rect.height)
	new_size = (int(img_rect.width * scale), int(img_rect.height * scale))
	pygameimage = pygame.transform.scale(pygameimage, new_size)
except pygame.error:
	print(f"Error: '{image_path}' not found.")
	pygameimage = pygame.Surface((800, 700))
	pygameimage.fill(white)

while True: 
	screen.fill(white)  
	# Center the image on the screen
	image_rect = pygameimage.get_rect(center=(1000 // 2, 900 // 2))
	screen.blit(pygameimage, image_rect)

	for event in pygame.event.get():  
		if event.type == pygame.QUIT:  
			pygame.quit()   
			quit()  
	pygame.display.flip()
	clock.tick(30)
