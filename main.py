import pygame

# Initialize pygame
pygame.init()

# Create Screen
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game")

#Load Sprites
walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'),
             pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'),
             pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'),
             pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'),
             pygame.image.load('Game/R9.png')]
walkLeft =  [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'),
             pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'),
             pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'),
             pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'),
             pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        
    def draw(self,screen):
        if self.walkCount >= 27:
            self.walkCount = 0
        
        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            screen.blit(char, (self.x,self.y))



def DrawGameWindow():
    global walkCount
    
    screen.blit(bg, (0,0))
    man.draw(screen)
    pygame.display.update()


#GAME LOOP
man = player(50,HEIGHT - 64,64,64)
running = True
while running:
    clock.tick(27)
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        man.left = True
        man.right = False
        if man.x > 0:
            man.x -= man.vel
        else:
            man.x = 0
    elif keys[pygame.K_RIGHT]:
        man.right = True
        man.left = False
        if man.x < (WIDTH - man.width):
            man.x += man.vel
        else:
            man.x = WIDTH - man.width
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        
    if not(man.isJump):   
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
            print("Jumping...")
    else: #if isJump True 
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.3 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            

            
    # DRAW
    DrawGameWindow()
    
    

 
#EXIT
pygame.quit()



