import random, pygame, sys
from pygame.locals import *

# Declaración de constantes y variables
COLOR_FONDO = (255, 255, 255)
# Otra forma usando la librería pygame: COLOR_FONDO = pygame.Color((0, 255, 255)

# Función principal del juego
def main():
      # Se inicializa el juego
      pygame.init()
      pygame.display.set_caption("Título del juego")
      screen = pygame.display.set_mode((640,512))

      mi_imagen = pygame.image.load("imagenes/ovni.png")
      x = 100
      y = 150
      velocidad = 1
      derecha = True

      # Bucle principal
      while True:

            # 1.- Se dibuja la pantalla
            screen.fill(COLOR_FONDO)
            screen.blit(mi_imagen, (x, y))
 
            # 2.- Se comprueban los eventos
            for event in pygame.event.get():
                  if event.type == QUIT:
                        pygame.quit()
                        sys.exit(0)

            if derecha == True:
                  if x < 450:
                        x += velocidad
                  else:
                        derecha = False
            else:
                  if x > 10:
                        x -= velocidad
                  else:
                        derecha = True

            # 3.- Se actualiza la pantalla
            pygame.display.update()

# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
   main()