import pygame

class Texto:
    def __init__(self, msg, display, color="black"):
        self.msg = msg
        self.fuente = pygame.font.Font("proyecto/fonts/GeneralSans-Regular.ttf", 18)
        self.color = color
        self.display = display
    
    def mostrar(self, pos):
        txt = self.fuente.render(self.msg, True, self.color)
        self.display.blit(txt, pos)