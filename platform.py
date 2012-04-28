import pygame

class Platforms(object):
	def __init__(self, platform_type, top_left):
		if platform_type =='box':
			self.image=pygame.image.load("images/box2.png")
		elif platform_type == 'pipe':
			self.image=pygame.image.load("images/pipe2.png")
		elif platform_type == 'box_fun':
			self.image =pygame.image.load("images/boxfun.png")
		elif platform_type == 'small_pit':
			self.image=pygame.image.load("images/smallpit.png")
		elif platform_type == 'large_pit':
			self.image=pygame.image.load("images/largepit.png")
		self.rect=self.image.get_rect()
		#print top_left
		self.rect.topleft = top_left
		
	def draw(self, screen):
		screen.blit(self.image, self.rect)
		
	def get_rect(self):
		return self.rect