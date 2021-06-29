def minijuego3():
    import pygame
    
    pygame.init()
    ADDRES = "C:\\Users\\Usuario\\Documents\\UN\\Métodos numéricos\\APPs\\WPy64-3940\\notebooks\\Pygame-Tutorials-master\\Game"
    #Screen
    win_width,win_height = 500,500
    win = pygame.display.set_mode((win_width,win_height))
    pygame.display.set_caption('3 Game')
    #Time
    FPS = 27
    clock = pygame.time.Clock()
    #Colors
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN_DARKER = (0,125,0)
    #Images
    walkRight = [pygame.image.load(ADDRES+'\\R1.png'), pygame.image.load(ADDRES+'\\R2.png'), pygame.image.load(ADDRES+'\\R3.png'), pygame.image.load(ADDRES+'\\R4.png'), pygame.image.load(ADDRES+'\\R5.png'), pygame.image.load(ADDRES+'\\R6.png'), pygame.image.load(ADDRES+'\\R7.png'), pygame.image.load(ADDRES+'\\R8.png'), pygame.image.load(ADDRES+'\\R9.png')]
    walkLeft = [pygame.image.load(ADDRES+'\\L1.png'), pygame.image.load(ADDRES+'\\L2.png'), pygame.image.load(ADDRES+'\\L3.png'), pygame.image.load(ADDRES+'\\L4.png'), pygame.image.load(ADDRES+'\\L5.png'), pygame.image.load(ADDRES+'\\L6.png'), pygame.image.load(ADDRES+'\\L7.png'), pygame.image.load(ADDRES+'\\L8.png'), pygame.image.load(ADDRES+'\\L9.png')]
    bg = pygame.transform.scale(pygame.image.load(ADDRES+'\\bg.jpg'),(win_width, win_height))
    char = pygame.image.load(ADDRES+'\\standing.png')
    
    enemy_walkRight = [pygame.image.load(ADDRES+'\\R1E.png'), pygame.image.load(ADDRES+'\\R2E.png'), pygame.image.load(ADDRES+'\\R3E.png'), pygame.image.load(ADDRES+'\\R4E.png'), pygame.image.load(ADDRES+'\\R5E.png'), pygame.image.load(ADDRES+'\\R6E.png'), pygame.image.load(ADDRES+'\\R7E.png'), pygame.image.load(ADDRES+'\\R8E.png'), pygame.image.load(ADDRES+'\\R9E.png'), pygame.image.load(ADDRES+'\\R10E.png'), pygame.image.load(ADDRES+'\\R11E.png')]
    enemy_walkLeft = [pygame.image.load(ADDRES+'\\L1E.png'), pygame.image.load(ADDRES+'\\L2E.png'), pygame.image.load(ADDRES+'\\L3E.png'), pygame.image.load(ADDRES+'\\L4E.png'), pygame.image.load(ADDRES+'\\L5E.png'), pygame.image.load(ADDRES+'\\L6E.png'), pygame.image.load(ADDRES+'\\L7E.png'), pygame.image.load(ADDRES+'\\L8E.png'), pygame.image.load(ADDRES+'\\L9E.png'), pygame.image.load(ADDRES+'\\L10E.png'), pygame.image.load(ADDRES+'\\L11E.png')]
    #Sound and Music
    bulletSound = pygame.mixer.Sound(ADDRES+"\\bullet.mp3")
    hitSound = pygame.mixer.Sound(ADDRES+"\\hit.mp3")
    jumpSound = pygame.mixer.Sound(ADDRES+"\\jump.wav")
    
    music = pygame.mixer.music.load(ADDRES+"\\music.mp3")
    pygame.mixer.music.play(-1)
    
    #Player
    HEALTH = 10
    score = 0
    N_BULLETS = 4
    class Player(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.isJump = False
            self.left = False
            self.right = False
            self.walkCount = 0
            self.jumpCount = 10
            self.standing = True
            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            self.shootLoop = 0
            
        def draw(self,win):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
    
            if not(self.standing):
                if self.left:
                    win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount +=1
            else:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            #pygame.draw.rect(win, RED , self.hitbox,2)
            
        def hit(self):
            self.isJump = False
            self.jumpCount = 10
            self.x, self.y = 50, win_height - char.get_height()
            self.walkCount = 0
            font1 = pygame.font.SysFont('comicsans',100)
            text = font1.render("-5",1 ,RED)
            win.blit(text,((win_width-text.get_width())//2,(win_height-text.get_height())//2))
            pygame.display.update()
            i = 0
            while i < 300:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()
                        
        def control(self):
            #Controls
            keys = pygame.key.get_pressed()
            #Bullets
            if self.shootLoop > 0:
                self.shootLoop += 1
            if self.shootLoop  > 3:
                self.shootLoop = 0
                
            if keys[pygame.K_SPACE] and self.shootLoop == 0:
                bulletSound.play()
                if self.left:
                    facing = -1
                else:
                    facing = 1 
                if len(bullets)<= N_BULLETS:
                    bullets.append(Projectile((self.x + self.width//2),(self.y + self.height//2),6, BLACK,facing))
                self.shootLoop = 1
                
            if keys[pygame.K_LEFT] and self.x - self.vel > 0 :
                self.x -= self.vel
                self.left = True
                self.right = False
                self.standing = False
            elif keys[pygame.K_RIGHT] and self.x + self.width + self.vel  < win_width:
                self.x += man.vel
                self.left = False
                self.right = True
                self.standing = False
            else: 
                self.standing = True
                self.walkCount = 0
                
             # Jump
            if not self.isJump:       
                if keys[pygame.K_UP]:
                    jumpSound.play()
                    self.isJump = True
                    self.right = False
                    self.left = False
                    self.walkCount = 0
            else:
                if self.jumpCount >= -10:
                    neg = 1
                    if self.jumpCount < 0:
                        neg = -1
                    self.y -= ((self.jumpCount**2) //2)*neg
                    self.jumpCount -= 1
                else:
                    self.isJump = False
                    self.jumpCount = 10
                    
            
    class Projectile (object):
        def __init__(self,x,y,radius,color,facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 8*facing
            
        def draw(self,win):
            pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
    
    class Enemy(object):
        walkRight = [pygame.image.load(ADDRES+'\\R1E.png'), pygame.image.load(ADDRES+'\\R2E.png'), pygame.image.load(ADDRES+'\\R3E.png'), pygame.image.load(ADDRES+'\\R4E.png'), pygame.image.load(ADDRES+'\\R5E.png'), pygame.image.load(ADDRES+'\\R6E.png'), pygame.image.load(ADDRES+'\\R7E.png'), pygame.image.load(ADDRES+'\\R8E.png'), pygame.image.load(ADDRES+'\\R9E.png'), pygame.image.load(ADDRES+'\\R10E.png'), pygame.image.load(ADDRES+'\\R11E.png')]
        walkLeft = [pygame.image.load(ADDRES+'\\L1E.png'), pygame.image.load(ADDRES+'\\L2E.png'), pygame.image.load(ADDRES+'\\L3E.png'), pygame.image.load(ADDRES+'\\L4E.png'), pygame.image.load(ADDRES+'\\L5E.png'), pygame.image.load(ADDRES+'\\L6E.png'), pygame.image.load(ADDRES+'\\L7E.png'), pygame.image.load(ADDRES+'\\L8E.png'), pygame.image.load(ADDRES+'\\L9E.png'), pygame.image.load(ADDRES+'\\L10E.png'), pygame.image.load(ADDRES+'\\L11E.png')]
        def __init__(self, x, y, width, height, end):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.path = [self.x, self.end]
            self.walkCount = 0
            self.vel = 3
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            self.health = HEALTH
            self.visible = True     
    
        def draw(self,win):
            self.move()
            if self.visible:
                if self.walkCount + 1 >= 33:
                    self.walkCount = 0
        
                if self.vel > 0:
                    win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                    self.walkCount += 1
                self.hitbox = (self.x + 17, self.y + 2, 31, 57)
                #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
                
                #Health
                pygame.draw.rect(win, RED, (self.hitbox[0],self.hitbox[1]-20,50,10))
                pygame.draw.rect(win, GREEN_DARKER, (self.hitbox[0],self.hitbox[1]-20,50-5*(HEALTH-self.health),10))
      
        def move(self):
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x - self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
    
        def hit(self):
            if self.health > 0:
                self.health -= 1
            else:
                self.visible = False
        
    ############################################################################################################
    def redrawGameWindow():
        global walkCount 
        win.blit(bg, (0,0))
        #Text
        text = font.render('Score: ' + str(score), 1, BLACK)
        win.blit(text,(win_width - 150,10))       
        
        man.draw(win) 
        goblin.draw(win)
        for bullet in bullets:
            bullet.draw(win)
            
            
        pygame.display.update()
    ############################################################################################################
    font = pygame.font.SysFont("comicsans",30,True,True) 
    bullets = []   
    man = Player(50,win_height - char.get_height(),char.get_width(),char.get_height())
    goblin = Enemy(win_width//4,win_height - enemy_walkLeft[0].get_height(),enemy_walkLeft[0].get_width(),enemy_walkLeft[0].get_height(),win_width-win_width//4)
    run = True
    while run:
        #Time
        clock.tick(FPS)
        #Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
###############################################################################################################
        #Bullets collision   
        for bullet in bullets:
            if goblin.visible == True and bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    hitSound.play()
                    score += 1
                    bullets.pop(bullets.index(bullet))  
            if bullet.x < win_width and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

###############################################################################################################            
        #Collision between characters
        if goblin.visible == True:
            if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                    man.hit()
                    score -= 5
###############################################################################################################        
        #Controls
        man.control()
        redrawGameWindow()
    
    pygame.quit()
minijuego3()