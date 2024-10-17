import pygame.font

class Stat():
    def __init__(self,window):
        self.screen = window
        self.points_my = 0
        self.points_pc = 0
        self.color_fg = (0,0,0)
        self.font = pygame.font.SysFont(None,24)
        self.create_text()
        self.image_win = pygame.image.load("you_win.png")
        self.image_lose = pygame.image.load("you_lose.png")
        self.image = self.image_win#дефолтное значение
        self.rect = self.image.get_rect()
        self.rect.centerx = 350
        self.rect.centery = 350
        self.show = False
    def create_text(self):
        self.image_my_points = self.font.render(f"my score {self.points_my}",True,self.color_fg,(255,216,141))
        self.image_pc_points = self.font.render(f"pc score {self.points_pc}", True, self.color_fg, (255, 216, 141))
        self.image_my_points_rect = self.image_my_points.get_rect()
        self.image_my_points_rect.x = 150
        self.image_my_points_rect.y = 15
        self.image_pc_points_rect = self.image_pc_points.get_rect()
        self.image_pc_points_rect.x = 154
        self.image_pc_points_rect.y = 35

    def art_text(self):
        self.screen.blit(self.image_my_points,self.image_my_points_rect)
        self.screen.blit(self.image_pc_points,self.image_pc_points_rect)
        if self.show == True:
            self.screen.blit(self.image,self.rect)
