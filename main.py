import pygame
import Menu
import Options
import game

class Main(object):
	def __init__(self):
		self.fullscreen = False
		self.display_fps = False
		self.display_quad_bounds = False
		self.resolution = (1024,768)
		self.name = "Tiny?"
		self.exit = False
		pygame.init()
		pygame.display.set_caption(self.name)
		self.screen = pygame.display.set_mode(self.resolution)
		self.setup_menu(title=self.name)
		self.game = game.Game(self.resolution)

		'''self.option = Options.Options(["fullscreen", self.set_fullscreen],
		["displayfps", self.set_display_fps],
		["displayquadbounds", self.set_display_quad_bounds])
		#self.game = Game.Game()'''

	def set_fullscreen(self, yes):
		if yes =="yes":
			self.fullscreen = True
		else:
			self.fullscreen = False
			
	def set_display_fps(self, yes):
		if yes =="yes":
			self.display_fps = True
		else:
			self.display_fps = False
			
	def set_display_quad_bounds(self, yes):
		if yes =="yes":
			self.display_quad_bounds = True
		else:
			self.display_quad_bounds = False
		
	def setup_menu(self, title="My Game", image=None):
		self.menu = Menu.EzMenu(
			["Play Game", self.start_game],
			["Options", self.option_screen],
			["Credits", self.credit_screen],
			["Quit Game", self.quit_game])
		self.menu.set_title(title,(20,50))
		#self.menu.set_bgimage('images/bg.jpg')
		self.menu.set_highlight_color((0,0,255))
		self.menu.set_normal_color((0,0,0))
		self.menu.center_at(self.resolution[0]/2,self.resolution[1]/2)
		self.main_menu = True
		
	def start_game(self):
		print "Start Game"
		self.main_menu = False
		
	def option_screen(self):
		print "Options"
		#self.main_menu = False
	
	def credit_screen(self):
		print "Credits"
		#self.main_menu = False
		
	def quit_game(self):
		print "Quit"
		self.main_menu = False
		self.game.game_over = True
		#pygame.quit()
		
if __name__ =="__main__":
	g=Main()
	g.screen.fill((255, 255, 255))
	while(not g.game.game_over):
		events = pygame.event.get()
		if(g.main_menu):
			g.menu.update(events)
			g.menu.draw(g.screen, g.game.game_over)
		elif not g.game.game_over:
			g.game.clock.tick(50)
			g.game.keyboard_input(events)
			g.game.update()
			g.game.draw(g.screen)
			#print "start game"
			
		pygame.display.flip()