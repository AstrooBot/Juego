import sys, pygame 
import random
import Loza

class Mesa:  
     def __init__(self, screen):
        self.screen = screen  
        self.lozas_num = []        
        self.num = [1,2,3,4,5,6,7,8]
        self.index = 0
        random.shuffle(self.num)
        self.font = pygame.font.Font(None, 36)

     def set_lozas(self):
        for j in range(0,3):
            for i in range(0,3):
                i = Loza.Loza(self.screen,  50+(j*15)+(100*j), 50+(i*15)+(100*i), ' white')
                self.lozas_num.append(i)
        del self.lozas_num[-1] 

        for i in self.lozas_num:
            i.text = self.font.render(str(self.num[self.index]), 1, 'Black')
            self.index +=1
            i.set_loza()