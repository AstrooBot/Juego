import sys, pygame 
from pygame.locals import *
size = width, height = 430,430

screen = pygame.display.set_mode(size)
pygame.init()

class Lozas:
    def __init__(self) -> None:
        self.num_lozas = []
        self.rect_lozas = []
    def set_lozas(self, screen):
        pygame.draw.rect(screen, 'white' , (j,i, 100, 100), 0, border_radius=15)
        
    def set_text(self,screen, j, i):
        pass
       
    def update(self):
         teclas = pygame.key.get_pressed()
         pass
         
        
        

    
lozas = Lozas()
lozas.set_lozas(screen)

while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        lozas.update()
        
        pygame.display.update()

"""Generar todas las cajas: for i in range(0,3):
            for j in range(0,3):
                s = pygame.draw.rect(screen, 'white' , (50+(j*15)+(100*j), 50+(i*15)+(100*i), 100, 100), 0, border_radius=15) 
                r = pygame.rect.Rect((50+(j*15)+(100*j), 50+(i*15)+(100*i), 50+(j*15)+(100*j)+100, 50+(i*15)+(100*i)+100))
                self.rect_lozas.append( r )
                self.num_lozas.append(s)"""
"""Generar todos los textos:
     num = 0
        for i in self.num_lozas:
            num +=1
            ctext = font.render(str(num), 1, 'Black')
            screen.blit(ctext, (i.centerx, i.centery))
    """