# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:56:53 2021

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
    imagen2=pygame.image.load("Frases\\2.jpg")
    imagen3=pygame.image.load("Frases\\3.jpg")
    imagen4=pygame.image.load("Frases\\4.jpg")
    imagen5=pygame.image.load("Frases\\5.jpg")
    imagen6=pygame.image.load("Frases\\6.jpg")
    imagen7=pygame.image.load("Frases\\7.jpg")
    imagen8=pygame.image.load("Frases\\8.jpg")
    imagen9=pygame.image.load("Frases\\9.jpg")
    imagen10=pygame.image.load("Frases\\10.jpg")
    imagen11=pygame.image.load("Frases\\11.jpg")
    imagen12=pygame.image.load("Frases\\2.jpg")
    imagen13=pygame.image.load("Frases\\13.jpg")
    imagen14=pygame.image.load("Frases\\14.jpg")
    imagen15=pygame.image.load("Frases\\15.jpg")
    imagen16=pygame.image.load("Frases\\16.jpg")
    imagen17=pygame.image.load("Frases\\17.jpg")
    imagen18=pygame.image.load("Frases\\18.jpg")
    imagen19=pygame.image.load("Frases\\19.jpg")
    imagen20=pygame.image.load("Frases\\20.jpg")
    imagen21=pygame.image.load("Frases\\21.jpg")
    
    cursor1=cursor()
    f1=pygame.image.load("Frases\\f1.PNG")
    f2=pygame.image.load("Frases\\f2.PNG")
    botons=Boton(f1,f2)
    
    
    while True:
        ventana.fill(color)
        ventana.blit(imagen2,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(botons.rect):
                    imagen2=imagen3
                    if imagen3==imagen3:
                        imagen3=imagen4
                    if imagen4==imagen4:
                        imagen4=imagen5
                    if imagen5==imagen5:
                        imagen5=imagen6
                    if imagen6==imagen6:
                        imagen6=imagen7
                    if imagen7==imagen7:
                        imagen7=imagen8
                    if imagen8==imagen8:
                        imagen8=imagen9
                    if imagen9==imagen9:
                        imagen9=imagen10
                    if imagen10==imagen10:
                        imagen10=imagen11
                    if imagen11==imagen11:
                        imagen11=imagen12
                    if imagen12==imagen12:
                        imagen12=imagen12
                    if imagen12==imagen12:
                        imagen12=imagen13
                    if imagen13==imagen13:
                        imagen13=imagen14
                    if imagen14==imagen14:
                        imagen14=imagen15
                    if imagen15==imagen15:
                        imagen15=imagen16
                    if imagen16==imagen16:
                        imagen16=imagen17
                    if imagen17==imagen17:
                        imagen17=imagen18
                    if imagen18==imagen18:
                        imagen18=imagen19
                    if imagen19==imagen19:
                        imagen19=imagen20
                    if imagen20==imagen20:
                        imagen20=imagen21


            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        cursor1.update()
        botons.update(ventana,cursor1)
        pygame.display.update()
main()