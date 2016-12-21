import pygame

class Ship():

	def __init__(self, screen):
		"""init ship and set it's orange site"""
		self.screen = screen

		"""load the bmp and get rect"""
		self.image = pygame.image.load('picture/ship_little.bmp')
		self.speed = 2
		self.rect = self.image.get_rect()	
		self.screen_rect = screen.get_rect()
		self.moving_flag = 0

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False

	def update(self):
		"""move depend flag"""
		if self.moving_right == True:
			if self.moving_flag == pygame.K_RIGHT:
				self.rect.centerx += self.speed
			elif self.moving_flag == pygame.K_LEFT:
				self.rect.centerx -= self.speed
			elif self.moving_flag == pygame.K_UP:
				self.rect.centery -= self.speed
			elif self.moving_flag == pygame.K_DOWN:
				self.rect.centery += self.speed

	def blitme(self):
		"""draw ship in specific site"""
		self.screen.blit(self.image, self.rect)
