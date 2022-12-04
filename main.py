import pygame
import math

# inicializamos pygame

pygame.init()


# creamos variables para el juego

fps = 60

# creamos un timmer para el juego con pygame

timer = pygame.time.Clock()

# creamos una variable que tendra el tipo de font que usaremos en el juego
# puedes descargar la font que quieres , podemos buscar en dafont

font = pygame.font.Font('assets/fonts/Lemony.ttf', 32)

# definir constantes para el tamaño de la pantalla

WIDTH = 900
HEIGHT = 800

# usamos el tamaño de pantalla con pygame

screen = pygame.display.set_mode([WIDTH, HEIGHT])

# creamos unas listas vacias para los backgrounds y banners

backgrounds = []
banners = []
# lista de Targets
target_images = [[], [], []]

# diccionario para saber cuantos targets habran en cada nivel

targets = {
           1: [10, 5, 3],
           2: [13, 8, 6],
           3: [15, 12, 8, 3]
           }

# variable para nivel

level = 2

# el juego es un arcade , en mi caso sera un taller que arreglara vehiculos
# usaremos una llave como utensilio
# tendremos una llave para cada nivel

wrenchs = []

# usare un bucle for para recorrer los backgrounds etc
# 1, 4 empezara en uno y temrinara en 3 los ciclos for de python incluyen el inicio , pero no el final

for i in range(1, 4):
# agregamos los backgrounds a la lista cargando la imagen con pygame
    backgrounds.append(pygame.image.load(f'assets/background/{i}.jpg'))
    banners.append(pygame.image.load(f'assets/banners/{i}.png'))
    wrenchs.append(pygame.transform.scale(pygame.image.load(f'assets/wrenchs/{i}.png'), (150, 150)))

def draw_wrench():
    mouse_pos = pygame.mouse.get_pos()
    wrench_point = (WIDTH/2, HEIGHT - 200)
    lasers = ['red', 'purple', 'green']
    clicks = pygame.mouse.get_pressed()
    if mouse_pos[0] != wrench_point[0]:
        slope = (mouse_pos[1] - wrench_point[1])/(mouse_pos[0] - wrench_point[0])
    else:
        slope = -100000
    angle = math.atan(slope)
    rotation = math.degrees(angle)
    if mouse_pos[0] < WIDTH/2:
        wrench = pygame.transform.flip(wrenchs[level - 1], True, False)
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(wrench, 90 - rotation), (WIDTH/2 - 90, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
    else :
        wrench = wrenchs[level - 1]
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(wrench, 270 - rotation), (WIDTH/2 - 30, HEIGHT - 250))
            if clicks[0]:
                pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)





# realizando pruebas

run = True
while run:
    timer.tick(fps)
    # llenado la pantalla

    screen.fill('black')
    screen.blit(backgrounds[level - 1], (0, 0))
    # cargamos los banners
    screen.blit(banners[level - 1], (0, HEIGHT - 200))

    # dibujando la llave con una funcion
    if level > 0:
        draw_wrench()
    # evitando un loop infinito por medio de un evento de pygame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()  # este comando dice que llevemos all a la pantalla y lo mostremos
pygame.quit()











