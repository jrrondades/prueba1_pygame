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
   screen = pygame.display.set_mode((640,520))

   mi_imagen = pygame.image.load("imagenes/ovni.png")
   x = random.randint(10, 540)
   y = random.randint(10, 420)
   

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

      # 3.- Se actualiza la pantalla
      pygame.display.update()

# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
   main()