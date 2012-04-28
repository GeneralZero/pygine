import pygame
import sprite
import background
import platform
import QuadTree

class Game(object):
    def __init__(self, resolution):
        self.game_over = False
        self.clock=pygame.time.Clock()
        self.resolution = resolution
        self.background=background.Background(resolution, "images\\BG.png")
        self.platforms = []
        self.player_sprite = sprite.Sprite()
        self.collision = QuadTree.QuadTree((0,0,self.resolution[0],self.resolution[1]), 0)
        self.win = 0 #0 = playing 1=Win -1 = lose
        
        #self.collision.add_object(0, self.player_sprite.dest_rect)
        self.create_world("world1.txt")
        
    def create_world(self, world):
        world_file = open(world, "r")
        for i, lines in enumerate(world_file):
            lines = lines.replace("(", "").rstrip().replace(")", "")
            split = lines.split(',')
            self.platforms.append(platform.Platforms(split[0], (int(split[1]), int(split[2]))))
            self.collision.add_object(self.platforms[i], self.platforms[i].rect)
        #print "\n\n"
        self.collision.elements()
        
    def keyboard_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_over = True
                if event.key == pygame.K_UP:
                    self.player_sprite.keypress_direction[0] = 1
                    self.player_sprite.motion_y.acceleration = -.5
                if event.key == pygame.K_DOWN:
                    self.player_sprite.keypress_direction[1] = 1
                    self.player_sprite.motion_y.acceleration = .5
                if event.key == pygame.K_LEFT:
                    self.player_sprite.keypress_direction[2] = 1
                    self.player_sprite.motion_x.acceleration = -.5
                elif event.key == pygame.K_RIGHT:
                    self.player_sprite.keypress_direction[3] = 1
                    self.player_sprite.motion_x.acceleration = .5
                if event.key == pygame.K_1:
                    self.player_sprite.size = 1
                elif event.key == pygame.K_2:
                    self.player_sprite.size = 2
                elif event.key == pygame.K_3:
                    self.player_sprite.size = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.player_sprite.keypress_direction[0] = 0
                    self.player_sprite.motion_y.acceleration = 0
                if event.key == pygame.K_DOWN:
                    self.player_sprite.keypress_direction[1] = 0
                if event.key == pygame.K_LEFT:
                    self.player_sprite.keypress_direction[2] = 0
                    self.player_sprite.motion_x.acceleration = 0
                elif event.key == pygame.K_RIGHT:
                    self.player_sprite.keypress_direction[3] = 0
                    self.player_sprite.motion_x.acceleration = 0
                    
                    
    def update(self):
        #print "test ",self.collision.get_elements(self.player_sprite.dest_rect)
        self.player_sprite.update(self.resolution, self.collision.get_elements(self.player_sprite.dest_rect))
        #self.music.update()
    
    def draw(self, screen):
        self.background.draw(screen)
        for x in self.platforms:
            x.draw(screen)
        self.player_sprite.draw(screen)
        self.collision.draw(screen)