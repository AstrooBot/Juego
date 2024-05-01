import sys, pygame 
import Mesa
from pygame.locals import *

def main():

    size = 430,430
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Rompecabezas deslizante")
    pygame.init()
    mesa = Mesa.Mesa(screen)
    mesa.set_lozas()


    while 1 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                screen.fill('black')
                
                for lozas in mesa.lozas_num:
                    lozas.update(mesa.lozas_num)         
        pygame.display.update()

if __name__ == "__main__":
   main() 