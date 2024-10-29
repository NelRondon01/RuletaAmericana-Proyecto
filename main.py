import pygame
import casilla
from ruleta import Ruleta
from textos import Texto
from apuesta import Apuesta
from personaje import Personaje

# INICIALIZAMOS LAS CLASES QUE USAREMOS
jugador = Personaje(0)
ruleta = Ruleta()
apuestas = [
    Apuesta(jugador,"pleno", 100, 12),
    Apuesta(jugador,"pleno", 100, 15),
    Apuesta(jugador,"pleno", 100, 20),
    Apuesta(jugador,"color", 50,  "negro")
]

# CONFIGURAMOS LA INTERFAZ PYGAME
pygame.init()
pantalla = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
juego = True
pygame.display.set_caption("RULETA (AMERICANA) - CASINO")

# CARGAMOS LA FUENTE A USAR & LA IMAGEN DE LA RULETA
fuente = pygame.font.Font("proyecto/fonts/GeneralSans-SemiBold.ttf", 26)
imagen = pygame.image.load("proyecto/assets/ruleta.png").convert_alpha()


log = []

# BUCLE DEL JUEGO
while juego:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego = False

    # COLOR DE FONDO DE PANTALLA
    pantalla.fill("white")

    # MOSTRAR RULETA
    ruleta.show(imagen, pantalla)

    # MOVIMIENTO DE LA RULETA
    ruleta.move()

    # CONTROLADOR PARA CUANDO LA RULETA SE DETIENE
    if ruleta.isStop():
        result = casilla.determinar_casilla(ruleta.ang)
        for apuesta in apuestas:
            if not apuesta.pagada:
                if apuesta.verificar_g(result) and not result[0] == 0:
                    pago = apuesta.calcular_pago()
                    log.append(Texto(f"+ {pago} fichas, por apuesta tipo {apuesta.tipo}", pantalla))
                    apuesta.pagar(jugador, pago)
                else:
                    log.append(Texto(f"\tPerdiste la apuesta tipo {apuesta.tipo}", pantalla))
                apuesta.pagada = True

    pygame.draw.line(pantalla, "red", (250, 0), (250, 100), 3)

    # INICIALIZAMOS LOS TEXTOS
    textos = [
        fuente.render(f"Angulo: {ruleta.ang}", True, "black"),
        fuente.render(f"Velocidad: {ruleta.vel}", True, "black"),
        fuente.render(f"Aceleración: {ruleta.acc}", True, "black"),
        fuente.render(f"Dinero: {jugador.dinero}", True, "black")
    ]

    y = 170
    for t in range(len(log)):
        log[t].mostrar((510, y+(t*20)))

    # RENDERIZADO DE TEXTOS
    x = 523 ; y = 50
    for t in range(len(textos)):
        pantalla.blit(textos[t], (x,y+(t*25)))
    

    # ACTUALIZACION DE LA PANTALLA
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
