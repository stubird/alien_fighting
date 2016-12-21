import sys
import pygame
#import random
#import time
from setting import Settings
from ship import Ship

def run_game():
	"""draw a screen obj"""
	pygame.init()
	gm_set = Settings()
	screen = pygame.display.set_mode((gm_set.screen_width, gm_set.screen_height))
	pygame.display.set_caption("Alien Invasion")


	"""creat a ship"""
	ship = Ship(screen)

	"""start the main loop"""
	while True:

		"""watch the key and mouse event"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		"""draw the screen"""
		"""random color"""
		#screen.fill(random.sample(bg_color, 1)[0])
		screen.fill(gm_set.bg_color[2])
		ship.blitme()
		#time.sleep(1)
		"""stay the screen recently"""
		pygame.display.flip()	

run_game()
		
