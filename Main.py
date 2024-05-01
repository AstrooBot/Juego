import sys, pygame 
import random
from pygame.locals import *
size = width, height = 430,430

screen = pygame.display.set_mode(size)
pygame.init()

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

        if teclas[K_LEFT] and 50 < self.x and check_left(loza, self.x, self.y) == True:
            self.x -= 115

        if teclas[K_RIGHT]  and self.x < 280 and check_right(loza, self.x, self.y) == True:
            self.x += 115


        if teclas[K_UP] and 50 < self.y and check_up(loza, self.x, self.y) == True:
            self.y -= 115
            

        if teclas[K_DOWN]  and self.y < 280 and check_down(loza, self.x, self.y) == True :
            self.y += 115
            
                

        self.set_loza()
        
            
            
def check_down(loza, x, y):
        check = True

        for i in loza:
            if i.y == y+115 and i.x == x:
                check = False
            
        return check 

def check_up(loza, x, y):
        
        check = True

        for i in loza:
            if i.y == y-115 and i.x == x:
                check = False
            
        return check 
        
def check_left(loza, x, y):
        
        check = True

        for i in loza:
            if i.y == y and i.x == x-115:
                check = False
            
        return check

def check_right(loza, x, y):
        
        check = True

        for i in loza:
            if i.y == y and i.x == x+115:
                check = False
            
        return check     
         
    


         
         
        
lozas_num = []        
num = [1,2,3,4,5,6,7,8,9]
index = 0
random.shuffle(num)
font = pygame.font.Font(None, 36)
    
for j in range(0,3):
    for i in range(0,3):
        i = Loza(screen,  50+(j*15)+(100*j), 50+(i*15)+(100*i), ' white')
        lozas_num.append(i)



del lozas_num[-1] 
num = [1,2,3,4,5,6,7,8]
random.shuffle(num)
index = 0
font = pygame.font.Font(None, 36)
for i in lozas_num:
    
    i.text = font.render(str(num[index]), 1, 'Black')
    index +=1
    i.set_loza()



while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            screen.fill('black')
            
            for lozas in lozas_num:
                lozas.update(lozas_num)
       
        
       
        
    pygame.display.update()

