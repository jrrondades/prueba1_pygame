import random, pygame, sys
from pygame.locals import *

# Declaración de constantes y variables
COLOR_FONDO = (0, 255, 255)
# Otra forma usando la librería pygame: COLOR_FONDO = pygame.Color((0, 255, 255)

# Función principal del juego
def main():
    # Se inicializa el juego
    pygame.init()
    pygame.display.set_caption("Título del juego")
    screen = pygame.display.set_mode((640,400))

    miFuente = pygame.font.Font(None, 60)
    miTexto = miFuente.render("Prueba Fuente", 0, (200,80,60))
    miFuenteSistema = pygame.font.SysFont("Arial", 60)
    miTextoSistema = miFuenteSistema.render("Prueba Fuente Sistema", 0, (200,80,60))

    # Bucle principal 
    while True:

        # 1.- Se dibuja la pantalla
        screen.fill(COLOR_FONDO)
       
        # 2.- Se comprueban los eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        screen.blit(miTexto, (180,180))
        screen.blit(miTextoSistema, (70,10))
        # 3.- Se actualiza la pantalla
        pygame.display.update()

# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
   main()