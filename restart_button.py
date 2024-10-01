import pygame

class Return():
    def __init__(self,window):
        self.screen = window
        self.image = pygame.image.load("button_return.png")
        self.rect = self.image.get_rect()
        self.rect.top = -10
        self.rect.right = 820
        small_image = pygame.transform.scale(self.image,(120,120))
        self.image = small_image
    def art_return(self):
        self.screen.blit(self.image,self.rect)

