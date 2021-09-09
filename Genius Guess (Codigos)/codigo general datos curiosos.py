# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 20:16:36 2021

@author: DUVAN
"""

import random
from random import randint
import subprocess
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
    imagen23=pygame.image.load("Datos curiosos\\23.jpg")
    imagen24=pygame.image.load("Datos curiosos\\24.jpg")
    imagen25=pygame.image.load("Datos curiosos\\25.jpg")
    imagen26=pygame.image.load("Datos curiosos\\26.jpg")
    imagen27=pygame.image.load("Datos curiosos\\27.jpg")
    imagen28=pygame.image.load("Datos curiosos\\28.jpg")
    imagen29=pygame.image.load("Datos curiosos\\29.jpg")
    imagen30=pygame.image.load("Datos curiosos\\30.jpg")
    imagen31=pygame.image.load("Datos curiosos\\31.jpg")
    imagen32=pygame.image.load("Datos curiosos\\32.jpg")
    imagen33=pygame.image.load("Datos curiosos\\33.jpg")
    imagen34=pygame.image.load("Datos curiosos\\34.jpg")
    imagen35=pygame.image.load("Datos curiosos\\35.jpg")
    imagen36=pygame.image.load("Datos curiosos\\36.jpg")
    imagen37=pygame.image.load("Datos curiosos\\37.jpg")
    imagen38=pygame.image.load("Datos curiosos\\38.jpg")
    imagen39=pygame.image.load("Datos curiosos\\39.jpg")
    imagen40=pygame.image.load("Datos curiosos\\40.jpg")
    imagen41=pygame.image.load("Datos curiosos\\41.jpg")
    imagen42=pygame.image.load("Datos curiosos\\42.jpg")
    
    cursor1=cursor()
    f1=pygame.image.load("Datos curiosos\\f1.PNG")
    f2=pygame.image.load("Datos curiosos\\f2.PNG")
    botons=Boton(f1,f2)
    
    
    while True:
        ventana.fill(color)
        ventana.blit(imagen23,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(botons.rect):
                    imagen23=imagen24
                    if imagen24==imagen24:
                        imagen24=imagen25
                    if imagen25==imagen25:
                        imagen25=imagen26
                    if imagen26==imagen26:
                        imagen26=imagen27
                    if imagen27==imagen27:
                        imagen27=imagen28
                    if imagen28==imagen28:
                        imagen28=imagen29
                    if imagen29==imagen29:
                        imagen29=imagen30
                    if imagen30==imagen30:
                        imagen30=imagen31
                    if imagen31==imagen31:
                        imagen31=imagen32
                    if imagen32==imagen32:
                        imagen32=imagen33
                    if imagen33==imagen33:
                        imagen33=imagen34
                    if imagen34==imagen34:
                        imagen34=imagen35
                    if imagen35==imagen35:
                        imagen35=imagen36
                    if imagen36==imagen36:
                        imagen36=imagen37
                    if imagen37==imagen37:
                        imagen37=imagen38
                    if imagen38==imagen38:
                        imagen38=imagen39
                    if imagen39==imagen39:
                        imagen39=imagen40
                    if imagen40==imagen40:
                        imagen40=imagen41
                    if imagen41==imagen41:
                        imagen41=imagen42

            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        cursor1.update()
        botons.update(ventana,cursor1)
        pygame.display.update()
main()