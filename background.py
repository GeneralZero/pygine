import pygame

class Background(object):
	def __init__(self, resolution, image):
		self.mainsurf=pygame.image.load(image).convert()
		self.dest_rect=(0,0,resolution[0],resolution[1])
		self.src_rect=(0,0,resolution[0],resolution[1])
		
	def update_background(self,x):
		self.draw_rect.move_ip(.5*x,0)
		if self.draw_rect.right>4050:
			self.draw_rect.left=0
		if self.draw_rect.left<0:
			self.draw_rect.right=4050
	
	def draw(self, screen):
		screen.blit(self.mainsurf, self.dest_rect, self.src_rect )



	
