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

    miFuente = pygame.font.SysFont("Arial", 48)
    
    aux = 1
    # Bucle principal 
    while True:

        # 1.- Se dibuja la pantalla
        screen.fill(COLOR_FONDO)

        tiempo = int(pygame.time.get_ticks()/1000)
        
        if aux == tiempo:
            aux += 1
                   
        # 2.- Se comprueban los eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        contador = miFuente.render("Tiempo : " + str(tiempo), 0, (120,70,0))
        screen.blit(contador, (180,180))
        # 3.- Se actualiza la pantalla
        pygame.display.update()

# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
   main()