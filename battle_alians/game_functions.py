import sys
import pygame

def check_events(ship):
	"""respond the event of key and mouse"""
	moving_right = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				"ship move to right"
				ship.rect.centerx += 3 
				ship.moving_right = True
				ship.moving_flag = event.key
			elif event.key == pygame.K_LEFT:
				"ship move to right"
				ship.rect.centerx -= 3
				ship.moving_right = True
				ship.moving_flag = event.key
			elif event.key == pygame.K_UP:
				"ship move to right"
				ship.rect.centery += 3
				ship.moving_right = True
				ship.moving_flag = event.key
			elif event.key == pygame.K_DOWN:
				"ship move to right"
				ship.rect.centery -= 3
				ship.moving_right = True
				ship.moving_flag = event.key
			
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			if event.key == pygame.K_LEFT:
				ship.moving_right = False
			if event.key == pygame.K_UP:
				ship.moving_right = False
			if event.key == pygame.K_DOWN:
				ship.moving_right = False

	ship.update()

def update_screen(gm_settings, screen, ship):
		"""random color"""
		#screen.fill(random.sample(bg_color, 1)[0])
		screen.fill(gm_settings.bg_color[2])
		ship.blitme()
		#time.sleep(1)
		"""stay the screen recently"""
		pygame.display.flip()	
