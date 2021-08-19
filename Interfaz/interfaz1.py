from Clases_y_Funciones import *

#pygame.init() # inicializo el modulo
pygame.init()
    
# fijo las dimensiones de la pantalla a 1000,600 y creo una superficie que va ser la principal
pygame.display.set_caption("GENIUS GUESS!")     # Titulo de la Ventana
icono      = pygame.image.load("imgs2\\18.png")        #variable de icono
pygame.display.set_icon(icono)                  #llama la variable de icono


#funcion principal
def main_menu():
    
    pantalla   = pygame.display.set_mode((510,450))
    
    #Botones varios
    img1   = pygame.image.load("imgs2\\15_1.png")
    img2   = pygame.image.load("imgs2\\26_1.png")
    
    img3   = pygame.image.load("imgs2\\30_1.png")
    img4   = pygame.image.load("imgs2\\30_2.png")
    boton2 = Boton(img3, img4, 45, 350)
    
    img5   = pygame.image.load("imgs2\\31_1.png")
    img6   = pygame.image.load("imgs2\\31_2.png")
    boton3 = Boton(img5, img6, 155, 350)
    
    img7   = pygame.image.load("imgs2\\29_1.png")
    img8   = pygame.image.load("imgs2\\29_2.png")
    boton4 = Boton(img7, img8, 280, 350)
    
    img11  = pygame.image.load("imgs2\\34_1.png")
    img12  = pygame.image.load("imgs2\\34_1.png")
    boton6 = Boton(img11, img12, 405,335)
    
    img13  = pygame.image.load("imgs2\\44_1.png")
    img14  = pygame.image.load("imgs2\\44_2.png")
    boton7 = Boton(img13, img14, 140, 20)
    
    img15   = pygame.image.load("imgs2\\62_2.png")
    img16   = pygame.image.load("imgs2\\62_1.png")
    boton8  = Boton(img15, img16, 40, 140)
    
    img17   = pygame.image.load("imgs2\\61_2.png")
    img18   = pygame.image.load("imgs2\\61_1.png")
    boton9  = Boton(img17, img18, 150, 140)
    
    img19   = pygame.image.load("imgs2\\64_2.png")
    img20   = pygame.image.load("imgs2\\64_1.png")
    boton10 = Boton(img19, img20, 40, 240)
    
    img21   = pygame.image.load("imgs2\\63_2.png")
    img22   = pygame.image.load("imgs2\\63_1.png")
    boton11 = Boton(img21, img22, 150, 240)
    
    #Bucle del juego
    ejecutando = True
    click = False
    while ejecutando:
        
        reloj.tick(20) #operacion para que todo corra a 20fps
        pantalla.fill((0, 229, 238))
        pantalla.blit(img2, (285,154))
        pantalla.blit(img1, (5,340))
        
        if cursor.colliderect(boton7.rect):
            if click:
                senda_genio()
                
        if cursor.colliderect(boton2.rect):
            if click:
                senda_trofeos()
                
        if cursor.colliderect(boton3.rect):
            if click:
                process1 = subprocess.Popen(['python', 'Codigo general frases.py'])
                print(process1)
                
        if cursor.colliderect(boton4.rect):
            if click:
                process1 = subprocess.Popen(['python', 'Codigo general datos curiosos.py'])
                print(process1)
                
        if cursor.colliderect(boton8.rect):
            if click:
                process1 = subprocess.Popen(['python', 'my_flappy1.py'])
                print(process1)
                
        if cursor.colliderect(boton9.rect):
            if click:
                process1 = subprocess.Popen(['python', 'mini_juego.py'])
                print(process1)
                
        if cursor.colliderect(boton10.rect):
            if click:
                process1 = subprocess.Popen(['python', '3Game_1.py'])
                print(process1)
                
        if cursor.colliderect(boton11.rect):
            if click:
                process1 = subprocess.Popen(['python', 'juegomemoria.py'])
                print(process1)
                
                
        click = False
        
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if cursor.colliderect(boton3.rect):
                    click  = True
                    
                if cursor.colliderect(boton4.rect):
                    click  = True
                    
                if cursor.colliderect(boton7.rect):
                    click  = True
                    
                if cursor.colliderect(boton2.rect):
                    click  = True

                if cursor.colliderect(boton8.rect):
                    click = True  
                    
                if cursor.colliderect(boton9.rect):
                    click = True  
                    
                if cursor.colliderect(boton10.rect):
                    click = True  
                    
                if cursor.colliderect(boton11.rect):
                    click = True  
                
            if event.type == QUIT:
                ejecutando = False
                pygame.quit()
                sys.exit()  
            
        cursor.update()
        
        #Botones
        boton2.update(pantalla,cursor)
        boton3.update(pantalla,cursor)
        boton4.update(pantalla,cursor)
        boton6.update(pantalla,cursor)
        boton7.update(pantalla,cursor)
        boton8.update(pantalla,cursor)
        boton9.update(pantalla,cursor)
        boton10.update(pantalla,cursor)
        boton11.update(pantalla,cursor)
        
        pygame.display.update() #actualizo el display


def senda_genio(): 
    
    pantalla = pygame.display.set_mode((510,460))

    img1   = pygame.image.load("imgs2\\35_3.png")
    img2   = pygame.image.load("imgs2\\35_1.png")
    boton1 = Boton(img1, img2, 20, 60)
    
    img5   = pygame.image.load("imgs2\\41_3.png")
    img6   = pygame.image.load("imgs2\\41_1.png")
    boton2 = Boton(img5, img6, 272, 60)
    
    img3   = pygame.image.load("imgs2\\36_3.png")
    img4   = pygame.image.load("imgs2\\36_1.png")
    boton3 = Boton(img3, img4, 20, 220)
    
    img7   = pygame.image.load("imgs2\\40_3.png")
    img8   = pygame.image.load("imgs2\\40_1.png")
    boton4 = Boton(img7, img8, 272, 220)
    
    img9   = pygame.image.load("imgs2\\38_2.png")
    img10  = pygame.image.load("imgs2\\38_1.png")
    boton5 = Boton(img9, img10, 20, 390)
    
    ejecutando = True
    click      = False
    while ejecutando:
        
        reloj.tick(20) #operacion para que todo corra a 20fps
        pantalla.fill((0, 229, 238))
        #pantalla.blit(img5, (40,580))
        
        if cursor.colliderect(boton1.rect):
            if click:
                process2 = subprocess.Popen(['python', 'MecánicaP1.py'])
                print(process2)

        if cursor.colliderect(boton2.rect):
            if click:
                process2 = subprocess.Popen(['python', 'ElectricidadP1.py'])
                print(process2)
                
        if cursor.colliderect(boton3.rect):
            if click:
                process2 = subprocess.Popen(['python', 'RelatividadP1.py'])
                print(process2)

        if cursor.colliderect(boton4.rect):
            if click:
                process2 = subprocess.Popen(['python', 'AstronomíaP1.py'])
                print(process2)

        if cursor.colliderect(boton5.rect):
            if click:
                main_menu() 
            
        click = False
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if cursor.colliderect(boton1.rect):
                    click = True   
                    
                if cursor.colliderect(boton2.rect):
                    click = True   
                    
                if cursor.colliderect(boton3.rect):
                    click = True
                
                if cursor.colliderect(boton4.rect):
                    click = True
                
                if cursor.colliderect(boton5.rect):
                    click = True                     
                   
            if event.type == QUIT:
                ejecutando = False
                pygame.quit()
                sys.exit()  
                
        cursor.update()
        
        boton1.update(pantalla,cursor)
        boton2.update(pantalla,cursor)
        boton3.update(pantalla,cursor)
        boton4.update(pantalla,cursor)
        boton5.update(pantalla,cursor)
        
        pygame.display.update() #actualizo el display
    
    

def senda_trofeos():
    
    pantalla   = pygame.display.set_mode((510,510))
    
    img1   = pygame.image.load("imgs2\\45_2.png")
    img2   = pygame.image.load("imgs2\\45_1.png")
    boton1 = Boton(img1, img2, 50, 20)
    
    img3   = pygame.image.load("imgs2\\46_2.png")
    img4   = pygame.image.load("imgs2\\46_1.png")
    boton2 = Boton(img3, img4, 280, 20)
    
    img5   = pygame.image.load("imgs2\\47_2.png")
    img6   = pygame.image.load("imgs2\\47_1.png")
    boton3 = Boton(img5, img6, 50, 240)
    
    img7   = pygame.image.load("imgs2\\48_2.png")
    img8   = pygame.image.load("imgs2\\48_1.png")
    boton4 = Boton(img7, img8, 280, 240)
    
    img9   = pygame.image.load("imgs2\\38_2.png")
    img10  = pygame.image.load("imgs2\\38_1.png")
    boton5 = Boton(img9, img10, 50, 460)
    
    ejecutando = True
    click      = False
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
                pygame.quit()
                sys.exit()

                
        cursor.update()
        
        boton1.update(pantalla,cursor)
        boton2.update(pantalla,cursor)
        boton3.update(pantalla,cursor)
        boton4.update(pantalla,cursor)
        boton5.update(pantalla,cursor)
        
        pygame.display.update() #actualizo el display
    
        
if __name__ == "__main__":
    main_menu()

