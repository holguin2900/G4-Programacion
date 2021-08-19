def flappy(gap = 6, t = 1.8, speed = 4):
    import pygame
    #import neat
    import time
    import os 
    import random
    pygame.font.init()
    pygame.mixer.init()#Sound effects
    
    #############################################################################################################
    
    #Time
    clock = pygame.time.Clock()
    fps = 60
    
    #Screen
    
    screen_width, screen_height = 600, 630
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flappy Bird")
    base_height = screen_height - screen_height//7
    #Images
    ADDRES= "C:\\Users\\LENOVO\\Documents\\GitHub\\G4-Programacion\\Interfaz\\minijuego_2flappy\\imgs"
    IMG_1 = ADDRES+"\\bird1.png"
    IMG_2 = ADDRES+"\\bird2.png"
    IMG_3 = ADDRES+"\\bird3.png"
    PIPE = ADDRES+"\\pipe.png"
    BASE = ADDRES+"\\base.png"
    BG = ADDRES+"\\bg.jpg"
    
    bird_imgs = [(pygame.image.load(IMG_1)),(pygame.image.load(IMG_2)),(pygame.image.load(IMG_3))]
    pipe_img = pygame.transform.scale(pygame.image.load(PIPE),(pygame.image.load(PIPE).get_width()*base_height//pygame.image.load(PIPE).get_height(),base_height))
    ground_img = pygame.transform.scale2x(pygame.image.load(BASE))
    #bg_img = pygame.transform.scale2x(pygame.image.load(BG))
    bg = pygame.transform.scale(pygame.image.load(BG),(screen_width, base_height))
    button_img = pygame.image.load(ADDRES+"\\restart.png")
    
    #button_img = pygame.font.SysFont(
    #    'Bauhaus 93',60).render("Presiona click derecho para comenzar", True, (255,255,255))
    ############################################################################################
    #Sound
    ADDRES_SOUND = "C:\\Users\\LENOVO\\Documents\\GitHub\\G4-Programacion\\Interfaz\\minijuego_2flappy\\sound"
    sound_point = pygame.mixer.Sound(ADDRES_SOUND+"\\sfx_point.wav")
    sound_wing = pygame.mixer.Sound(ADDRES_SOUND+"\\sfx_wing.wav")
    sound_collision = pygame.mixer.Sound(ADDRES_SOUND+"\\sfx_hit.wav")
    #Music
    pygame.mixer.music.load(ADDRES_SOUND+"\\sfx_music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1) 
    
    ############################################################################################
    #font
    font = pygame.font.SysFont('Bauhaus 93',60)
    font_2 = pygame.font.SysFont('Bauhaus 93',40)
    #Colors
    white =(255,255,255)
    black = (0,0,0)
    
    #Game variables
    ground_scroll = 0
    scroll_speed = speed
    flying = False
    game_over = False
    pipe_gap = bird_imgs[0].get_height()*gap
    pipe_frequency = t*1000 #milliseconds
    last_pipe = pygame.time.get_ticks() - pipe_frequency
    score = 0
    high_score = 0
    pass_pipe = False
    
    def draw_text(text,font,text_col,x,y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x-img.get_width()//2,y))
    def reset_game():
        pipe_group.empty()
        flappy.rect.x = 100
        flappy.rect.y = screen_height//2
        score = 0
        return score
    class Bird(pygame.sprite.Sprite):
        def __init__ (self,x,y):
            pygame.sprite.Sprite. __init__(self)
            self.images = bird_imgs
            self.index = 0
            self.counter = 0
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = [x,y]
            self.vel = 0
            self.clicked = False
        
        def update(self):
            if flying == True :
                #Gravity
                self.vel += 0.5
                if self.vel > 8:
                    self.vel = 8
                if self.rect.bottom < base_height:
                    self.rect.y += int(self.vel)
            
            #jump
            if game_over == False: 
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.vel = -10
                    sound_wing.play()
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
                    
                
                #Handle the animation
                self.counter += 1
                flap_cooldown = 5
                if self.counter > flap_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images):
                        self.index = 0
                    
                self.image = self.images[self.index]
                
                #rotate the bird
                self.image = pygame.transform.rotate(self.images[self.index], self.vel*-2)
            else:
                 self.image = pygame.transform.rotate(self.images[self.index], -75)
    
    
    class Pipe(pygame.sprite.Sprite):
        def __init__(self,x,y,position):
            pygame.sprite.Sprite. __init__(self)
            self.image = pipe_img
            self.rect = self.image.get_rect()
            
            #position = 1 top, position = -1  from bottom
            if position == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x,y - pipe_gap//2]
            if position == -1:
                self.rect.topleft = [x,y + pipe_gap//2]
        
        def update(self):
            self.rect.x -= scroll_speed
            if self.rect.right < 0:
                self.kill()
    
    class Button():
        
        
        
        def __init__(self,x,y,image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)
            
        def draw(self):
            action = False
            # get mouse position
            pos = pygame.mouse.get_pos()
            
            #check if mouse is over the button
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    action = True
                    
                    
            # draw button
            screen.blit(self.image,(self.rect.x - self.image.get_width()//2 ,self.rect.y))
            return action
        
    bird_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()
    flappy = Bird(100,screen_height//2)
    bird_group.add(flappy)
    
    button = Button(screen_width//2, base_height//2, button_img)
    
    run = True
    while run:
        
        
        #Time
        clock.tick(fps)
        
        screen.blit(bg,(0,0))
        
        bird_group.draw(screen)
        bird_group.update()
        pipe_group.draw(screen)
    
        
        #draw the ground
        screen.blit(ground_img,(ground_scroll,base_height))
        draw_text("Record: " + str(high_score),font_2,white,screen_width//2,screen_height-50)
        if flying == False:
            draw_text("Presiona: Click izquierdo",font_2,black,screen_width//2,screen_height//2-100)     
        
        #check score
        if len(pipe_group) > 0:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
                    and pass_pipe == False:
                        pass_pipe = True
            if pass_pipe == True:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                    score += 1
                    sound_point.play()
                    pass_pipe = False
        if score >high_score:
            high_score = score
        draw_text(str(score),font,white,screen_width//2,0) 
                
            
        #collision
        if game_over == False and pygame.sprite.groupcollide(bird_group, pipe_group,  False, False) or flappy.rect.top < 0:
            game_over = True
            sound_collision.play()
            
        #check if the bird hit the ground
        if flappy.rect.bottom > base_height:
            game_over = True
            flying = False
        
        if game_over == False and flying == True:
            #new pipes
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > pipe_frequency:
                pipe_heigth = random.randint(-100,100)
                btm_pipe = Pipe(screen_width,pipe_heigth + base_height//2,-1)
                top_pipe = Pipe(screen_width,pipe_heigth + base_height//2,1)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe = time_now
    
                
            #Draw and scroll the ground
            ground_scroll -= scroll_speed
            if abs(ground_scroll) > 50:
                ground_scroll = 0
            pipe_group.update()
        
        #check for game over and reset
        if game_over == True:
            if button.draw() == True:
                game_over = False
                score = reset_game()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False :
                flying = True
                
                
             
        pygame.display.update()
    pygame.quit()
#if __name__== "__flappy__": #It's just making sure when we run this file
flappy()
#flappy(5,1.5,6)  # gap, time and speed
#flappy(7,2,3)
# it would run this fucntion rather than other.
# 'Cause we can have other modules.                   
        
                    
    
