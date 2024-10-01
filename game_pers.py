import pygame
class Game_pers():
    def __init__(self,window,image,x,y,type_object):
        self.screen = window
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type_object = type_object
        self.small_image = pygame.transform.scale(self.image,(self.image.get_width()/2,self.image.get_height()/2))
        self.default_x = x
        self.default_y = y
    def art_pers(self):
        self.screen.blit(self.small_image,self.rect)
    def default_position(self):
        self.rect.x = self.default_x
        self.rect.y = self.default_y
