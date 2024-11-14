import pygame

# Clase Boton
class Boton:
    def __init__(self, x, y, ancho, alto, texto, color=(200, 200, 200), fs=16, color_txt="black", hover=True, value=None, type=None):
        # ATRIBUTOS ESCENCIALES
        self.texto = str(texto)
        self.value = texto if value==None else value

        # RENDERIZADO
        self.pos = (x,y)
        bd = 2
        self.rect = pygame.Rect(x+bd, y+bd, ancho-bd*2, alto-bd*2)
        self.borde = pygame.Rect(x, y, ancho, alto)
        self.fuente = pygame.font.Font("proyecto/fonts/GeneralSans-SemiBold.ttf", fs)

        # COLORES
        self.color_texto = color_txt
        self.color_normal = color
        ajustar_brillo = lambda clr, factor: tuple(min(255, int(c * factor)) for c in clr)
        self.color_hover = ajustar_brillo(self.color_normal, 0.7)

        # ESTADOS
        self.type = type
        self.canHover = hover
        self.select = False
        


    def dibujar(self, pantalla):
        # Cambiar color si el mouse está sobre el botón
        mouse_pos = pygame.mouse.get_pos()
        color_actual = self.color_hover if self.rect.collidepoint(mouse_pos) else self.color_normal

        color_borde = color_actual if self.canHover else self.color_normal

        if not self.canHover:
            color_actual = self.color_normal
        
        if self.select:
            color_actual = self.color_hover
            color_borde = (79, 128, 255)
    
        pygame.draw.rect(pantalla, color_borde, self.borde)
        pygame.draw.rect(pantalla, color_actual, self.rect)
        
        # Renderizar el texto
        texto_renderizado = self.fuente.render(self.texto, True, self.color_texto)
        pantalla.blit(texto_renderizado, 
                      (self.rect.x + (self.rect.width - texto_renderizado.get_width()) // 2,
                       self.rect.y + (self.rect.height - texto_renderizado.get_height()) // 2))
    
    def isclick(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                if self.type == "bool":
                    self.value = False if self.value else True
                if self.type == "selection":
                    self.select = False if self.select else True
                return True
        return False
    
class ListaBotones: 
    def __init__(self, type=None):
        self.type = type
        self.botones = []

    def get(self):
        return self.botones
    
    def add(self, btn):
        if type(btn)==list:
            for x in btn:
                self.add(x)
        else:
            if not self.type==None:
                btn.type = self.type
            self.botones.append(btn)
    
    def dibujar(self, pantalla):
        for b in self.botones:
            b.dibujar(pantalla)

    def default(self):
        for btn in self.botones:
            btn.select = False

class ListaBotonesSelect(ListaBotones):
    def __init__(self):
        super().__init__("selection")

    def get_selects(self):
        sel = []
        for a in self.botones:
            if a.select:
                sel.append(a.value)
        return sel
    
class ListaBotonesOpcion(ListaBotones):
    def __init__(self):
        super().__init__("opcion")
    
    def opcion(self, index):
        for btn in self.botones:
            if btn == self.botones[index]:
                btn.select = True
            else:
                btn.select = False
        return str(self.botones[index].value).lower()

# lst = ListaBotonesSelect()
# lst1 = ListaBotones()

# print(lst.botones)