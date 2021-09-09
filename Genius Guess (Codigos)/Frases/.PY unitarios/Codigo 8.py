# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 10:31:56 2021

@author: DUVAN
"""

import pygame,sys
from pygame.locals import *
import pygame 
class cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=460,y=530):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)
def main():
    color=(255,255,255)
    colordos= pygame.Color(240,30,60)
    pygame.init()
    ventana= pygame.display.set_mode((600,600))
    pygame.display.set_caption("Genius Quest")
    imagen2=pygame.image.load("8.jpg")
    cursor1=cursor()
    f1=pygame.image.load("f1.PNG")
    f2=pygame.image.load("f2.PNG")
    botons=Boton(f1,f2)
    while True:
        ventana.fill(color)
        ventana.blit(imagen2,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        cursor1.update()
        botons.update(ventana,cursor1)
        pygame.display.update()
main()