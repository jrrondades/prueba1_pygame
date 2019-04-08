import random, pygame, sys
from pygame.locals import *

# Declaración de constantes y variables
COLOR_FONDO = (0, 255, 255)
ANCHO_FONDO = 900
ALTO_FONDO = 400

class NaveEspacial(pygame.sprite.Sprite):
    """ Clase para las Naves """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_nave = pygame.image.load("imagenes/nave.jpg")
        self.rect = self.img_nave.get_rect()
        self.rect.centerx = ANCHO_FONDO / 2
        self.rect.centery = ALTO_FONDO - 30
        self.lista_disparo = []
        self.vida = True
        self.velocidad = 20

    """ Nuevos cambios (Métodos) """
    def mover_derecha(self):
        self.rect.right += self.velocidad
        self.__mover()

    def mover_izquierda(self):
        self.rect.left -= self.velocidad
        self.__mover()

    
    def __mover(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= 900:
                self.rect.right = 900


    def disparar(self, x, y):
        mi_proyectil = Proyectil(x, y)
        self.lista_disparo.append(mi_proyectil)


    def dibujar(self, superficie):
        superficie.blit(self.img_nave, self.rect)

class Proyectil(pygame.sprite.Sprite):
    """ Clase para los Proyectiles """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img_proyectil = pygame.image.load("imagenes\disparoa.jpg")
        self.rect = self.img_proyectil.get_rect()
        self.velocidad_disparo = 5
        self.rect.top = y
        self.rect.left = x

    def trayectoria(self):
        self.rect.top -= self.velocidad_disparo

    def dibujar(self, superficie):
        superficie.blit(self.img_proyectil, self.rect)

class Invasor(pygame.sprite.Sprite):
    """ Clase para los Invasores """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.imagen_a = pygame.image.load("imagenes\MarcianoA.jpg")
        self.imagen_b = pygame.image.load("imagenes\MarcianoB.jpg")

        self.lista_img = [self.imagen_a, self.imagen_b]
        self.pos_img = 0

        self.img_invasor = self.lista_img[self.pos_img]
        self.rect = self.img_invasor.get_rect()

        self.lista_disparo = []
        self.velocidad = 20
        self.rect.top = y
        self.rect.left = x

        self.tiempo_cambio = 1

    def dibujar(self, superficie):
        self.img_invasor = self.lista_img[self.pos_img]
        superficie.blit(self.img_invasor, self.rect)

    def comportamiento(self, tiempo):
        #print(self.tiempo_cambio, tiempo)
        #print(self.pos_img, len(self.lista_img))
        if self.tiempo_cambio == tiempo:
            #print("tiempos iguales")
            self.pos_img += 1
            self.tiempo_cambio += 1
            if self.pos_img > len(self.lista_img) - 1:
                #print("reseteo posicion imagen")
                self.pos_img = 0


# Función principal del juego
def main():
    # Se inicializa el juego
    pygame.init()
    pygame.display.set_caption("Space Invader")
    screen = pygame.display.set_mode((ANCHO_FONDO,ALTO_FONDO))
    imagen_fondo = pygame.image.load("imagenes\Fondo.jpg")

    jugador = NaveEspacial()
    enemigo = Invasor(100, 100)

    en_juego = True

    # Nuevo cambio
    reloj = pygame.time.Clock()

    # Bucle principal
    while True:

        # 1.- Se dibuja la pantalla
        screen.fill(COLOR_FONDO)
        # Nuevo cambio
        reloj.tick(60)
        # jugador.mover()
        tiempo = int(pygame.time.get_ticks() / 1000)
        #print("Tiempo:", tiempo)
        
        # 2.- Se comprueban los eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if en_juego == True:
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.mover_izquierda()
                    elif event.key == K_RIGHT:
                        jugador.mover_derecha()
                    elif event.key == K_SPACE:
                        x, y = jugador.rect.center
                        jugador.disparar(x, y)

        screen.blit(imagen_fondo, (0,0))
        enemigo.comportamiento(tiempo)
        jugador.dibujar(screen)
        enemigo.dibujar(screen)
        
        if len(jugador.lista_disparo) > 0:
            for x in jugador.lista_disparo:
                x.dibujar(screen)
                x.trayectoria()
                if x.rect.top < 100:
                    jugador.lista_disparo.remove(x)

        # 3.- Se actualiza la pantalla
        pygame.display.update()

# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
    main()