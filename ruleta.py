import pygame

class Ruleta:
    def __init__(self):
        # CONSTANTES
        self.ACC = 0.08

        # VARIABLES
        self.vel = 0
        self.acc = self.ACC
        self.ang = 0

        # ESTADOS
        self.turn = True
        self.stop = False

    def show(self, imagen, display):
        imagen_rota = pygame.transform.rotate(imagen, self.ang)
        rect_rota = imagen_rota.get_rect(center=(250,250))
        display.blit(imagen_rota, rect_rota.topleft)

    def isStop(self):
        return self.stop

    def move(self):
        keys = pygame.key.get_pressed()

        if self.vel<20:
            self.vel+=self.acc
        self.ang+=self.vel

        if not self.turn:
            self.acc = 0
            self.vel *= .98
            if self.vel<.1:
                self.vel = 0

        self.stop = True if self.vel == 0 else False

        if keys[pygame.K_DOWN] and self.turn:
            self.turn = False
        if keys[pygame.K_UP] and not self.turn:
            self.turn = True
            self.acc = self.ACC

