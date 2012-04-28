from pygame import draw

class QuadTree(object):
	def __init__(self, box, current_level, max_level=4):# box (top_left_x, top_left_y, size_x, size_y)
		self.location = (box[0], box[1])
		self.size = (box[2], box[3])
		self.current_level = current_level
		self.max_level = max_level
		
		self.objects = []
		self.__setupchirldren__()
		
	def __setupchirldren__(self):
		self.top_right = 		None
		self.top_left = 		None
		self.bottom_right = 	None
		self.bottom_left = 		None
		
	def elements(self):
		if self.current_level == self.max_level:
			for x in self.objects:
				print x, x.rect
		else:
			if self.bottom_left != None:
				self.bottom_left.elements()
			if self.bottom_right != None:
				self.bottom_right.elements()
			if self.top_left != None:
				self.top_left.elements()
			if self.top_right != None:
				self.top_right.elements()
		
	def add_object(self, new_object, rect):
		if self.current_level == self.max_level:
			#print new_object, rect
			self.objects.append(new_object)
			#print self.objects
		else:
			half_size = (self.size[0]/2, self.size[1]/2)
			if rect.colliderect(self.location, half_size):
				if self.top_left == None:
					self.top_left = 		QuadTree((self.location[0], self.location[1], half_size[0], half_size[1]), self.current_level+1, self.max_level)
				self.top_left.add_object(new_object, rect)
			if rect.colliderect((self.location[0]+half_size[0], self.location[1]), half_size):
				if self.top_right == None:
					self.top_right = 		QuadTree((self.location[0]+half_size[0], self.location[1], half_size[0], half_size[1]), self.current_level+1, self.max_level)
				self.top_right.add_object(new_object, rect)
			if rect.colliderect((self.location[0], self.location[1]+half_size[1]), half_size):
				if self.bottom_left == None:
					self.bottom_left = 		QuadTree((self.location[0], self.location[1]+half_size[1], half_size[0], half_size[1]), self.current_level+1, self.max_level)
				self.bottom_left.add_object(new_object, rect)
			if rect.colliderect((self.location[0]+half_size[0], self.location[1]+half_size[1]), half_size):
				if self.bottom_right == None:
					self.bottom_right = 	QuadTree((self.location[0]+half_size[0], self.location[1]+half_size[1], half_size[0], half_size[1] ), self.current_level+1, self.max_level)
				self.bottom_right.add_object(new_object, rect)
				
	def draw(self, screen):
		#if self.current_level == self.max_level:
		draw.line(screen, (255, 0, 0), self.location, (self.location[0]+self.size[0], self.location[1]))
		draw.line(screen, (255, 0, 0), self.location, (self.location[0], self.location[1]+self.size[1]))
		draw.line(screen, (255, 0, 0), (self.location[0]+self.size[0], self.location[1]+self.size[1]), (self.location[0]+self.size[0], self.location[1]))
		draw.line(screen, (255, 0, 0), (self.location[0]+self.size[0], self.location[1]+self.size[1]), (self.location[0], self.location[1]+self.size[1]))
		if self.current_level != self.max_level:
			if self.bottom_left != None:
				self.bottom_left.draw(screen)
			if self.bottom_right != None:
				self.bottom_right.draw(screen)
			if self.top_left != None:
				self.top_left.draw(screen)
			if self.top_right != None:
				self.top_right.draw(screen)
					
	def get_elements(self, rect):
		#ret = self.objects
		if self.current_level == self.max_level:
			#print self.objects
			return self.objects
		else:
			half_size = (self.size[0]/2, self.size[1]/2)
			if self.top_left!= None and rect.colliderect((self.location, half_size)):
				return self.top_left.get_elements(rect)
				#for x in self.top_left.get_elements(rect):
				#	ret.append(x)
			if self.top_right!= None and rect.colliderect(((self.location[0]+self.size[0]/2, self.location[1]), half_size)):
				return self.top_right.get_elements(rect)
				#for x in self.top_right.get_elements(rect):
				#	ret.append(x)
			if self.bottom_left!= None and rect.colliderect(((self.location[0], self.location[1]+self.size[1]/2), half_size)):
				return self.bottom_left.get_elements(rect)
				#for x in self.bottom_left.get_elements(rect):
				#	ret.append(x)
			if self.bottom_right!= None and rect.colliderect(((self.location[0]+self.size[0]/2, self.location[1]+self.size[1]/2), half_size)):
				return self.bottom_right.get_elements(rect)
				#for x in self.bottom_right.get_elements(rect):
				#	ret.append(x)
			#print ret
		return []
				