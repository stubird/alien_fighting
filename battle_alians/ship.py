import pygame

class Ship():

	def __init__(self, screen):
		"""init ship and set it's orange site"""
		self.screen = screen

		"""load the bmp and get rect"""
		self.image = pygame.image.load('picture/ship_little.bmp')
		self.rect = self.image.get_rect()	
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		"""draw ship in specific site"""
		self.screen.blit(self.image, self.rect)
