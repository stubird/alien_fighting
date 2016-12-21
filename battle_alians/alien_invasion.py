import sys
import pygame
import game_functions as gf
#import random
#import time
from setting import Settings
from ship import Ship

def run_game():
	"""draw a screen obj"""
	pygame.init()
	gm_set_obj = Settings()
	screen = pygame.display.set_mode((gm_set_obj.screen_width, gm_set_obj.screen_height))
	pygame.display.set_caption("Alien Invasion")

	"""creat a ship"""
	ship = Ship(screen)

	"""start the main loop"""
	while True:

		gf.check_events(ship)

		gf.update_screen(gm_set_obj, screen, ship)
run_game()
		
