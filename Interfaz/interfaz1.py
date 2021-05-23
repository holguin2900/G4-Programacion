import pygame
from pygame.locals import *
import sys

#Creamos el cursor
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)
    def update(self): #mueve el rectangulo segun la posicion de mouse
        self.left, self.top = pygame.mouse.get_pos() #devuelve la posiones del mouse

#creamos el boton
class Boton(pygame.sprite.Sprite):
    def __init__(self, imagen1, imagen2, x, y):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        
    def update(self, pantalla, cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else: self.imagen_actual = self.imagen_normal
        
        pantalla.blit(self.imagen_actual, self.rect)


    

#funcion main
def main():
    pygame.init() # inicializo el modulo
    
    # fijo las dimensiones de la pantalla a 1000,600 y creo una superficie que va ser la principal
    pantalla = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("GENIUS GUESS!") # Titulo de la Ventana
    icono = pygame.image.load("18.png") #variable de icono
    pygame.display.set_icon(icono) #llama la variable de icono
    
    # boton de repasar
    repasar1 = pygame.image.load("29_1.png")
    repasar2 = pygame.image.load("29_2.png")
    
    #Botones varios
    img1 = pygame.image.load("15_1.png")
    img2 = pygame.image.load("26_1.png")
    
    img3 = pygame.image.load("30_1.png")
    img4 = pygame.image.load("30_2.png")
    boton2 =Boton(img3, img4, 490, 510)
    
    img5 = pygame.image.load("31_1.png")
    img6 = pygame.image.load("31_2.png")
    boton3 =Boton(img5, img6, 570, 510)
    
    img7 = pygame.image.load("32_1.png")
    img8 = pygame.image.load("32_2.png")
    boton4 =Boton(img7, img8, 676, 510)
    
    img9 = pygame.image.load("33_1.png")
    img10 = pygame.image.load("33_2.png")
    boton5 =Boton(img9, img10, 780, 510)
    
    img11 = pygame.image.load("34_1.png")
    img12 = pygame.image.load("34_2.png")
    boton6 =Boton(img11, img12, 870,495)
    
    # Creamos el cursor
    boton1 = Boton(repasar1, repasar2, 600, 150)
    cursor = Cursor()
    
    #creo un reloj para controlar los fps
    reloj = pygame.time.Clock()
    
    #Bucle del juego
    ejecutando = True
    while ejecutando:
        reloj.tick(20) #operacion para que todo corra a 20fps
        pantalla.fill((0, 229, 238))
        pantalla.blit(img2, (730,314))
        pantalla.blit(img1, (460,500))

        for event in pygame.event.get():
            if event.type == QUIT:
                ejecutando = False
                
        cursor.update()
        
        #Botones
        boton1.update(pantalla,cursor)
        boton2.update(pantalla,cursor)
        boton3.update(pantalla,cursor)
        boton4.update(pantalla,cursor)
        boton5.update(pantalla,cursor)
        boton6.update(pantalla,cursor)
        
        pygame.display.update() #actualizo el display
        
    pygame.quit()
    
main()
