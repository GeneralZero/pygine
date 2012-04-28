import os

class Options(object):
		def __init__(self, *options):
			self.fullscreen = False
			self.display_fps = True
			self.file = None
			self.display_quad_bounds = False
			self.options = 	options
			
			self.read_from_file("options.ini")
				
		def read_from_file(self, settings_file):
			if os.path.exists(settings_file):
				self.file = open(settings_file, 'r')
				for x,line in enumerate(self.file):
					elem = line.split(":")[0].rstrip()
					yes = line.split(":")[1].rstrip()
					#print elem, yes
					#print self.options[elem](yes)
					if x<len(self.options):
						self.options[x][1](yes)
			else: self.write_to_file(settings_file)
			
		def write_to_file(self, settings_file):
			self.file = open(settings_file, 'w')
			for option in self.options:
				self.file.write(option[0]+":")
				#print self.file.write(option[0]+":")
				if option[1] =="yes":
					self.file.write("yes\n")
					#print "yes\n"
				else:
					self.file.write("no\n")
					#print "no\n"
					
		#def draw(self, screen):
			

'''g=Options(["fullscreen", self.fullscreen],
		["displayfps", self.display_fps],
		["displayquadbounds", self.display_quad_bounds])
g.read_from_file("options.ini")'''
