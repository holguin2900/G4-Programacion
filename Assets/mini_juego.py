# -*- coding: utf-8 -*-
"""
Created on Wed May 19 19:21:05 2021

@author: Usuario
"""
def minijuego_1():
    import pygame
    import os #Id path of the image
    pygame.font.init() #Intialize the pygame's font library. 
    pygame.mixer.init()#Sound effects
    ADDRES = "C:\\Users\\Usuario\\Documents\\UN\\Métodos numéricos\\APPs\\GitHub\\G4-Programacion\\Assets"
    
    WIDTH, HEIGHT = 900, 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maxwell vs Tesla") #Title
    
    
    #Colors
    WHITE = (255,255,255) # Screen color
    BLACK = (0,0,0) # Border color
    RED = (255,0,0)
    YELLOW = (255,255,0)
    #Border
    BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT) #Anticlockwise draw
    
    FPS = 60 #Speed of our game to add up.
    VEL = 5
    
    #Bullets
    BULLETS_VEL = 7
    MAX_BULLETS = 3
    YELLOW_HIT = pygame.USEREVENT + 1
    RED_HIT = pygame.USEREVENT + 2
    #Bullets sound
    #BULLET_FIRE_SOUND = pygame.mixer.Sound('Gun+Silencer.mp3')
    BULLET_FIRE_SOUND = pygame.mixer.Sound(ADDRES+'\\Gun+Silencer.mp3')
    #BULLET_HIT_SOUND = pygame.mixer.Sound('Grenade+1.mp3')
    BULLET_HIT_SOUND = pygame.mixer.Sound(ADDRES+'\\Grenade+1.mp3')
    
    #Health
    HEALTH_FONT = pygame.font.SysFont('comicsans',40)
    #Winner
    WINNER_FONT = pygame.font.SysFont('comicsans',100)
    
    SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 180,150
    
    
    
    #YELLOW_SPACESHIP_IMAGE = pygame.image.load('spaceship_yellow.png') En caso de que funcione sin el path directo
    YELLOW_SPACESHIP_IMAGE = pygame.image.load(ADDRES+'\\spaceship_yellow.png')
    #Poner doble \\ para evitar error
    
    #Scaled image
    #YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
    
    #Scaled and rotated image
    YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,YELLOW_SPACESHIP_IMAGE.get_height()*SPACESHIP_WIDTH//YELLOW_SPACESHIP_IMAGE.get_width())),0)
    
    
    
    
    #RED_SPACESHIP_IMAGE = pygame.image.load('spaceship_red.png')
    RED_SPACESHIP_IMAGE = pygame.image.load(ADDRES+'\\spaceship_red.png')
    
    #Scaled image
    #RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
    
    #Scaled and rotated image
    RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
        RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,RED_SPACESHIP_IMAGE.get_height()*SPACESHIP_WIDTH//RED_SPACESHIP_IMAGE.get_width())),0)
    
    #Background
    #SPACE = pygame.transform.scale(
        #pygame.image.load('space.png'),(WIDTH,HEIGHT))
    SPACE = pygame.transform.scale(pygame.image.load(ADDRES+'\\space.png'),(WIDTH,HEIGHT))
    
    
    
    def draw_window(red,yellow,red_bullets,yellow_bullets, red_health, yellow_health): #Position of our rectangles
        WIN.blit(SPACE,(0,0))
       # WIN.fill(WHITE) # (It's white) To fill the screen with a specific color.
        pygame.draw.rect(WIN, BLACK, BORDER) # It's similar to WIN.blit()
        
       # Health text
        red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
        yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
        WIN.blit(red_health_text,(WIDTH - red_health_text.get_width()-10,10))
        WIN.blit(yellow_health_text, (10, 10))
        
        
        WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y)) #Put images on the screen 
        WIN.blit(RED_SPACESHIP,(red.x,red.y))
        
        for bullet in red_bullets:
            pygame.draw.rect(WIN, RED, bullet)
            
        for bullet in yellow_bullets:
            pygame.draw.rect(WIN, YELLOW, bullet)
            
        pygame.display.update() # One value for red, blue and green (0 to 255).
        
    def yellow_handle_movement(keys_pressed,yellow):
            #Keyboard movement (method multiple keys at the time)
            keys_pressed = pygame.key.get_pressed()
            
            if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # LEFT
            # and we don't let our spaceship to be outside of the window
                yellow.x -= VEL
            if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # RIGHT #Less tha the border of middle of the screen
                yellow.x += VEL
            if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # UP
                yellow.y -= VEL
            if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 10 : # DOWN
                yellow.y += VEL
            
            
    
    
    def red_handle_movement(keys_pressed,red):
            #Keyboard movement (method multiple keys at the time)
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_LEFT]  and red.x - VEL > BORDER.x + BORDER.width : # LEFT
                red.x -= VEL
            if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # RIGHT
                red.x += VEL
            if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #UP
                red.y -= VEL
            if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 10 : # DOWN
                red.y += VEL
    
    def handle_bullets(yellow_bullets, red_bullets, yellow, red):
        for bullet in yellow_bullets:
            bullet.x += BULLETS_VEL
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                yellow_bullets.remove(bullet)
            elif bullet.x > WIDTH: #Check when the bullets are out of the screen
                yellow_bullets.remove(bullet)
                
        for bullet in red_bullets:
            bullet.x -= BULLETS_VEL
            if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                red_bullets.remove(bullet)
            elif bullet.x < 0: #Check when the bullets are out of the screen
                red_bullets.remove(bullet)
    
    #Who wins
    def draw_winner(text):
        draw_text = WINNER_FONT.render(text, 1 ,WHITE)
        WIN.blit(draw_text, (WIDTH//2- draw_text.get_width()//2,HEIGHT//2 - draw_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(5000) #5 seconds by a thousand
        
    def main():
        red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT) # Position rectangle
        yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT) # Position rectangle
        
        red_bullets = []
        yellow_bullets = []
        
        red_health = 10
        yellow_health = 10
        
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS) #it controls the speed of this while.
            for event in pygame.event.get(): 
                 if event.type == pygame.QUIT:
                     run = False
                     #pygame.quit #Restart game
                   # Bullets   
                 if event.type == pygame.KEYDOWN:
                    
                     if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS: # Left control
                         bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10 , 5)
                         yellow_bullets.append(bullet)
                         BULLET_FIRE_SOUND.play()#Bullet sound
                        
                     if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS: # Right control
                        bullet = pygame.Rect(red.x , red.y + red.height//2 - 2, 10 , 5)
                        red_bullets.append(bullet)
                        BULLET_FIRE_SOUND.play()#Bullet sound
                     
                    # Health
                 if event.type == RED_HIT:
                     red_health -= 1
                     BULLET_HIT_SOUND.play()#Hit sound
                    
                 if event.type == YELLOW_HIT:
                     yellow_health -= 1
                     BULLET_HIT_SOUND.play()#Hit sound
            
            #Winner
            winner_text = ""
            if red_health <= 0:
                winner_text = "Maxwell Wins!"
            
            if yellow_health <= 0:
                winner_text = "Tesla Wins!"
                
            if winner_text != "":
                draw_winner(winner_text) #SOMEONE WON
                break
                        
                         
            keys_pressed = pygame.key.get_pressed()
            yellow_handle_movement(keys_pressed,yellow)
            red_handle_movement(keys_pressed, red)
            
            handle_bullets(yellow_bullets, red_bullets, yellow, red)
            
            draw_window(red,yellow, red_bullets, yellow_bullets,
                        red_health, yellow_health)
            
        pygame.quit()
        #main() #Restart game and also delete pygame.quit()
        
    if __name__=="__main__": #It's just making sure when we run this file
        main()  # it would run this fucntion rather than other.
                # 'Cause we can have other modules.
                
minijuego_1()
    
                