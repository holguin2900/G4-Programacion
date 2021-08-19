from Clases_y_Funciones import *



def pantalla_inicial():
    
    pygame.init()
    
    color    = (255,255,255)
    colordos = pygame.Color(240,30,60)
    
    ventana  = pygame.display.set_mode((510,660))
    pygame.display.set_caption("Genius Guest!")
    imagen2  = pygame.image.load("imgs2\\72_1.png")
    
    reloj1   = pygame.time.Clock()
    fuente1  = pygame.font.SysFont("Times", 40,True,False)
    #texto1   = fuente1.render("Bienvenidos a Genius Guest",0,(50,0,0))
    segundos = 0

    img1     = pygame.image.load("imgs2\\74_1.png")
    img2     = pygame.image.load("imgs2\\73_1.png")
    boton1   = Boton(img1, img2, 360, 550)
    
    img3     = pygame.image.load("imgs2\\75_1.png")
    img4     = pygame.image.load("imgs2\\76_1.png")
    boton2   = Boton(img3, img4, 20, 550)
    
    click = False
    while True:
        
        ventana.fill(color)
        ventana.blit(imagen2,(0,0))

        if cursor.colliderect(boton1.rect):
            if click:
                login()    
                pygame.quit()
                sys.exit()

        if cursor.colliderect(boton2.rect):
            if click:
                registro()
                
        click = False
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton1.rect):
                    click = True
                if cursor.colliderect(boton2.rect):
                    click = True
            
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
                  
        segundos= pygame.time.get_ticks()/1000
        
        cursor.update()
        
        boton1.update(ventana, cursor)
        boton2.update(ventana, cursor)
        
        segundos= str(int(segundos))
        #contador=fuente1.render(segundos,0,(0,0,240))
        #ventana.blit(contador,(540,20))
        #ventana.blit(texto1,(20,150))
        pygame.display.update()
        
    pygame.quit()
    sys.exit()        
    
if __name__ == "__main__":
    pantalla_inicial()


