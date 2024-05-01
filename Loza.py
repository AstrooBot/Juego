import pygame 
from pygame.locals import *
class Loza:
    def __init__(self, screen, x , y, color ) -> None:
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.shape = None
        self.rect = None
        self.text = None
        
        
    def set_loza(self):

        self.shape = pygame.draw.rect(self.screen, self.color , (self.x, self.y, 100, 100), border_radius=15)
        self.rect = pygame.rect.Rect(self.shape)
        if self.text != None:
            self.screen.blit(self.text, (self.rect.centerx, self.rect.centery)) 

        
       
    def update(self,loza):
        teclas = pygame.key.get_pressed()

        if teclas[K_LEFT] and 50 < self.x and self.check_left(loza) == True:
            self.x -= 115

        if teclas[K_RIGHT]  and self.x < 280 and self.check_right(loza) == True:
            self.x += 115


        if teclas[K_UP] and 50 < self.y and self.check_up(loza) == True:
            self.y -= 115
            

        if teclas[K_DOWN]  and self.y < 280 and self.check_down(loza) == True:
            self.y += 115
            

        self.set_loza()
        
            
            
    def check_down(self, loza):
            check = True

            for i in loza:
                if i.y == self.y+115 and i.x == self.x:
                    check = False
                
            return check 

    def check_up(self, loza):
            
            check = True

            for i in loza:
                if i.y == self.y-115 and i.x == self.x:
                    check = False
                
            return check 
            
    def check_left(self, loza):
            
            check = True

            for i in loza:
                if i.y == self.y and i.x == self.x-115:
                    check = False
                
            return check

    def check_right(self, loza):
            
            check = True

            for i in loza:
                if i.y == self.y and i.x == self.x+115:
                    check = False
                
            return check  