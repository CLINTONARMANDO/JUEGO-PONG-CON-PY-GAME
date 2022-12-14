import string
import pygame

pygame.init()

# Definimos las  estaticas
tamannio_pantalla = (700, 500)       # Ancho y alto
bg  = (0,0,0)
blanco = (255,255,255)
pad = 20
#tamaño paleta
w_pal = 10
h_pal = 90
#centro
c_x = int(tamannio_pantalla[0]/2)
c_y = int(tamannio_pantalla[1]/2)
#coordenadas paleta
x_pal1=pad
x_pal2=tamannio_pantalla[0] - (pad + w_pal)
y_pal1=c_y - h_pal/2
y_pal2=c_y - h_pal/2

# Definimos variables 
Fin = False
pelota_x = c_x
pelota_y = c_y
velocidad_pelota_x = 2
acelerac_pelota_x = 1
velocidad_pelota_y = 2
acelerac_pelota_y = 1
radio = 10
pointsp1 = 0
pointsp2 = 0
y_p1 = y_pal1
y_p2 = y_pal2
x_p1 = x_pal1
x_p2 = x_pal2
velocidad_p1 = 0
velocidad_p2 = 0
#valores y cordenadas linea media
linmedwi = 10
linmedhe = tamannio_pantalla[1]
linmedx = (tamannio_pantalla[0]-5)/2
linmedy = 0

pantalla = pygame.display.set_mode(tamannio_pantalla)

pygame.display.flip()
reloj = pygame.time.Clock()

while not Fin:
    # Est parte es para capturar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Fin = True

        # Eventos del Teclado
        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_w:
                velocidad_p1 = -5
            if event.key == pygame.K_s:
                velocidad_p1 = 5
            # Jugador 2
            if event.key == pygame.K_o:
                velocidad_p2 = -5
            if event.key == pygame.K_l:
                velocidad_p2 = 5

        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_w:
                velocidad_p1 = 0
            if event.key == pygame.K_s:
                velocidad_p1 = 0

            # Jugador 2
            if event.key == pygame.K_o:
                velocidad_p2 = 0
            if event.key == pygame.K_l:
                velocidad_p2 = 0

    # Aqui todo el codigo

    # Restricciones para la pelota
    # Eje X
    if pelota_x > (tamannio_pantalla[0]-radio):
        pelota_x = c_x
        pelota_y = c_y
        velocidad_pelota_x = 2
        velocidad_pelota_y = 2
        velocidad_pelota_x *= -1
        velocidad_pelota_y *= -1
        y_p1 = y_pal1
        y_p2 = y_pal2
        x_p1 = x_pal1
        x_p2 = x_pal2
        pointsp2 += 1
    if pelota_x < radio:
        pelota_x = c_x
        pelota_y = c_y
        velocidad_pelota_x = -2
        velocidad_pelota_y = -2
        velocidad_pelota_x *= -1
        velocidad_pelota_y *= -1
        y_p1 = y_pal1
        y_p2 = y_pal2
        x_p1 = x_pal1
        x_p2 = x_pal2
        pointsp1 += 1
    # Eje Y
    if pelota_y > (tamannio_pantalla[1]-radio) or pelota_y < radio:
        velocidad_pelota_y *= -1

    # Movimiento de la pelota
    pelota_x += velocidad_pelota_x
    pelota_y += velocidad_pelota_y

    # Movimiento de los jugadores (Paletas)
    y_p1 = y_p1 + velocidad_p1
    y_p2 = y_p2 + velocidad_p2

    # Renderizar la pantalla y los objetos
    pantalla.fill(bg)
    pel = pygame.draw.circle(pantalla, blanco, (pelota_x, pelota_y), radio)
    p1 = pygame.draw.rect(pantalla, blanco,(x_p1, y_p1, w_pal, h_pal))
    p2 = pygame.draw.rect(pantalla, blanco,(x_p2, y_p2, w_pal, h_pal))
    linmedvar = pygame.draw.rect(pantalla, blanco,(linmedx, linmedy, linmedwi, linmedhe))
    fuente = pygame.font.Font(None, 50)
    text1 = "Jugador 1: " + str(pointsp1)
    text2 = "Jugador 2: " + str(pointsp2)
    mensaje1=fuente.render(text1, 1, (255, 255, 255))
    mensaje2=fuente.render(text2, 1, (255, 255, 255))
    pantalla.blit(mensaje2, (15, 10))
    pantalla.blit(mensaje1, (15 + tamannio_pantalla[0]/2, 10))

    # Detectando las colisiones
    if pel.colliderect(p1) or pel.colliderect(p2): 
        velocidad_pelota_x *= -1
        acelerac_pelota_x *= -1
        acelerac_pelota_y *= -1
        velocidad_pelota_x += acelerac_pelota_x
        velocidad_pelota_y += acelerac_pelota_y
        
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()