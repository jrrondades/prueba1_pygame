import random, pygame, sys
from pygame.locals import *

# Declaración de constantes y variables
COLOR_FONDO = (0, 255, 255)
color_line = pygame.Color(0,0,0)
COLOR_RECT = (250, 75, 0)
COLOR_CIRC = (0, 0, 120)
COLOR_POLI = (0, 120, 0)

# Función principal del juego
def main():
   # Se inicializa el juego
   pygame.init()
   pygame.display.set_caption("Título del juego")
   # Cambiar el color de la línea
   color_line.r = 120
   color_line.g = 120
   color_line.b = 120
   screen = pygame.display.set_mode((480,360))

   # Bucle principal
   while True:

      # 1.- Se dibuja la pantalla
      screen.fill(COLOR_FONDO)
      
      pygame.draw.polygon(screen, COLOR_POLI, ((140, 0), (291, 106), (237, 277), (56, 277), (0, 106)))
      pygame.draw.rect(screen, COLOR_RECT, (10, 10, 200, 150))
      pygame.draw.circle(screen, COLOR_CIRC, (80, 90), 30)
      pygame.draw.line(screen, color_line, (60, 80), (160, 100), 8)

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