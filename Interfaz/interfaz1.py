import pygame
from pygame.locals import *
import sys


#pygame.init() # inicializo el modulo
pygame.init()

# fijo las dimensiones de la pantalla a 1000,600 y creo una superficie que va ser la principal
pantalla = pygame.display.set_mode((540,660))
pygame.display.set_caption("GENIUS GUESS!") # Titulo de la Ventana
icono = pygame.image.load("18.png") #variable de icono
pygame.display.set_icon(icono) #llama la variable de icono


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


# Creamos el cursor

cursor = Cursor()
    
#creo un reloj para controlar los fps
reloj = pygame.time.Clock()

#funcion main
def main_menu():
    
    
    # boton de repasar
    repasar1 = pygame.image.load("29_1.png")
    repasar2 = pygame.image.load("29_2.png")
    boton1 = Boton(repasar1, repasar2, 50, 150)
    
    #Botones varios
    img1 = pygame.image.load("15_1.png")
    img2 = pygame.image.load("26_1.png")
    
    img3 = pygame.image.load("30_1.png")
    img4 = pygame.image.load("30_2.png")
    boton2 = Boton(img3, img4, 45, 565)
    
    img5 = pygame.image.load("31_1.png")
    img6 = pygame.image.load("31_2.png")
    boton3 = Boton(img5, img6, 125, 565)
    
    img7 = pygame.image.load("32_1.png")
    img8 = pygame.image.load("32_2.png")
    boton4 = Boton(img7, img8, 231, 565)
    
    img9 = pygame.image.load("33_1.png")
    img10 = pygame.image.load("33_2.png")
    boton5 = Boton(img9, img10, 335, 565)
    
    img11 = pygame.image.load("34_1.png")
    img12 = pygame.image.load("34_2.png")
    boton6 = Boton(img11, img12, 420,550)
    
    img13 = pygame.image.load("15_2.png")
    img14 = pygame.image.load("15_3.png")
    boton7 = Boton(img13, img14, 200,150)
    
    
    #Bucle del juego
    ejecutando = True
    click = False
    while ejecutando:
        reloj.tick(20) #operacion para que todo corra a 20fps
        pantalla.fill((0, 229, 238))
        pantalla.blit(img2, (285,369))
        pantalla.blit(img1, (15,555))
        
        
        if cursor.colliderect(boton7.rect):
            if click:
                senda_genio()
                
        
        click = False
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton7.rect):
                    click = True
                
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
        boton7.update(pantalla,cursor)
        
        pygame.display.update() #actualizo el display
        
    pygame.quit()
    
def senda_genio(): 

    img1 = pygame.image.load("35_3.png")
    img2 = pygame.image.load("35_1.png")
    boton1 = Boton(img1, img2, 170, 50)
    
    img3 = pygame.image.load("36_3.png")
    img4 = pygame.image.load("36_1.png")
    boton2 = Boton(img3, img4, 170, 180)
    
    img5 = pygame.image.load("41_3.png")
    img6 = pygame.image.load("41_1.png")
    boton3 = Boton(img5, img6, 170, 310)
    
    img7 = pygame.image.load("40_3.png")
    img8 = pygame.image.load("40_1.png")
    boton4 = Boton(img7, img8, 170, 440)
    
    img9 = pygame.image.load("38_2.png")
    img10 = pygame.image.load("38_1.png")
    boton5 = Boton(img9, img10, 40, 580)
    
    ejecutando = True
    click = False
    while ejecutando:
        
        reloj.tick(20) #operacion para que todo corra a 20fps
        pantalla.fill((0, 229, 238))
        #pantalla.blit(img5, (40,580))
        
        if cursor.colliderect(boton5.rect):
            if click:
                main_menu() 
                
        click = False
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton5.rect):
                    click = True                    
                   
            if event.type == QUIT:
                ejecutando = False
                
        cursor.update()
        
        boton1.update(pantalla,cursor)
        boton2.update(pantalla,cursor)
        boton3.update(pantalla,cursor)
        boton4.update(pantalla,cursor)
        boton5.update(pantalla,cursor)
        
        pygame.display.update() #actualizo el display

#def primer_juego():
    

main_menu()
