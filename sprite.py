import pygame
import math

class Motion(object):
    def __init__(self, max_velocity, initial_vel=0.0, initial_accel=0.0, gravity = 0.015, min_velocty = .45):
        self.min_velocty = min_velocty
        self.velocity = initial_vel
        self.acceleration = initial_accel
        self.max_velocity = max_velocity
        self.gravity = gravity
        self.last_direction = 1
        
    def update(self):
        self.velocity += self.acceleration  
        if abs(self.velocity) > self.max_velocity:
            self.velocity = self.max_velocity *(self.velocity / abs(self.velocity))
        if self.velocity !=0 and self.last_direction != (self.velocity / abs(self.velocity)):
            self.last_direction = (self.velocity / abs(self.velocity))
    def update_gravity(self):
        if abs(self.velocity)>self.min_velocty:
            self.velocity -= self.gravity * (self.velocity/abs(self.velocity))


class Sprite(object):
    def __init__(self):
        self.keypress_direction = [0,0,0,0]#up,down,left, right
        self.hight = 110
        self.width = 150
        self.frame = 1
        self.max_frame = 5
        self.size = 3
        self.image = []
        self.image.append(pygame.image.load("images/right_walk.png").convert_alpha())
        self.image.append(pygame.image.load("images/left_walk.png").convert_alpha())
        self.src_rect = pygame.Rect(0,0,self.hight,self.width)
        self.dest_rect = pygame.Rect(0,700,self.hight,self.width)
        self.draw_image = self.image[0]
        self.animation_counter=0
        self.animation_rate=20
        self.motion_x = Motion(10, gravity = 0.2)
        self.motion_y = Motion(10, gravity = 0.2)
        
    def update(self, resolution, colsision):
        self.update_pos(resolution, colsision)
        self.update_draw()
        
    def update_pos(self, resolution, colsision):
        self.motion_y.update()
        self.motion_x.update()
        self.dest_rect.x += self.motion_x.velocity
        self.dest_rect.y += self.motion_y.velocity
        if abs(self.motion_y.velocity) <= self.motion_x.min_velocty :
            self.motion_y.velocity = 0
        if abs(self.motion_x.velocity) <= self.motion_x.min_velocty :
            self.motion_x.velocity = 0
        
        for objects in colsision:
            #top Rect
            if object.rect.bottom > self.dest_rect.top and self.dest_rect.top > object.rect.top:
                if object.rect.left - self.dest_rect.right > object.rect.bottom - self.dest_rect.top:
                    self.dest_rect.top = object.rect.bottom
                #elif object.rect.left - self.dest_rect.right < object.rect.bottom - self.dest_rect.top:
                #elif object.rect.left - self.dest_rect.right < object.rect.bottom - self.dest_rect.top:
                    
            
                
            
            #if self.dest_rect.colliderect(objects.rect):
            #    print "colide"
        
        
        if self.dest_rect.top < 0:
            self.dest_rect.top = 0
            self.motion_y.velocity = 0
        if self.dest_rect.bottom > resolution[1]:
            self.dest_rect.bottom = resolution[1]
            self.motion_y.velocity = 0
        if self.dest_rect.left < 0:
            self.dest_rect.left = 0
            self.motion_x.velocity = 0
        if self.dest_rect.right > resolution[0]:
            self.dest_rect.right = resolution[0]
            self.motion_x.velocity = 0
        self.motion_x.update_gravity()
        self.motion_y.update_gravity()
        
        
        
    def update_draw(self):
        if self.motion_x.velocity > 0 :
            self.draw_image = self.image[0]
        elif self.motion_x.velocity < 0 :
            self.draw_image = self.image[1]
        elif self.motion_x.last_direction == 1:
            self.draw_image = self.image[0]
        elif self.motion_x.last_direction == -1:
            self.draw_image = self.image[1]
        if abs(self.motion_x.velocity) > self.motion_x.min_velocty:
            self.animation_counter += math.floor(1+abs(self.motion_x.velocity/(self.motion_x.max_velocity/2.5)))
            #print self.animation_counter
            if self.animation_counter>self.animation_rate:
                self.animation_counter=0
                self.frame+=1
                if self.frame == self.max_frame:
                    self.frame=0
                self.src_rect.left=self.frame*110
            
    def draw(self, screen):
        screen.blit(self.draw_image, self.dest_rect, self.src_rect)