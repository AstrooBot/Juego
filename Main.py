import sys, pygame 
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
        self.set_loza()
        
    def set_loza(self):

        self.shape = pygame.draw.rect(self.screen, self.color , (self.x, self.y, 100, 100), border_radius=15)
        self.rect = pygame.rect.Rect(self.shape)
        if self.text != None:
            self.screen.blit(self.text, (self.rect.centerx, self.rect.centery)) 

        
       
    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT] and self.color == 'red':
            self.x -= 115
        if teclas[K_RIGHT] and self.color == 'red':
            self.x += 115
        if teclas[K_UP] and self.color == 'red':
            self.y -= 115
        if teclas[K_DOWN] and self.color == 'red':
            self.y += 115     
        self.set_loza()
        
            
        
        
         
         
        
lozas_num = []        

    
for j in range(0,3):
    for i in range(0,3):
        i = Loza(screen,  50+(j*15)+(100*j), 50+(i*15)+(100*i), ' white')
        lozas_num.append(i)



lozas_num[-1].color = 'red' 
num = 0
font = pygame.font.Font(None, 36)
for i in lozas_num:
    num +=1
    i.text = font.render(str(num), 1, 'Black')
    i.set_loza()
    


               
 
while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            screen.fill('black')
            for lozas in lozas_num:
                lozas.update()
       
        
       
        
    pygame.display.update()

"""Generar todas las cajas: for i in range(0,3):
            for j in range(0,3):
                s = pygame.draw.rect(screen, 'white' , (50+(j*15)+(100*j), 50+(i*15)+(100*i), 100, 100), 0, border_radius=15) 
                r = pygame.rect.Rect((50+(j*15)+(100*j), 50+(i*15)+(100*i), 50+(j*15)+(100*j)+100, 50+(i*15)+(100*i)+100))
                self.rect_lozas.append( r )
                self.num_lozas.append(s)"""
"""num = 0
font = pygame.font.Font(None, 36)
for i in lozas_num:
            num +=1
            ctext = font.render(str(num), 1, 'Black')
            i.screen.blit(ctext, (i.rect.centerx, i.rect.centery))
    """