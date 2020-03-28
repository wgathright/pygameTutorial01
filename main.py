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


width = 64
height = 64
x = 50
y = HEIGHT - height
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def DrawGameWindow():
    global walkCount
    
    screen.blit(bg, (0,0))
    
    if walkCount >= 27:
        walkCount = 0
        
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(char, (x,y))
        
    
    pygame.display.update()


#GAME LOOP
running = True
while running:
    clock.tick(27)
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        left = True
        right = False
        if x > 0:
            x -= vel
        else:
            x = 0
    elif keys[pygame.K_RIGHT]:
        right = True
        left = False
        if x < (WIDTH - width):
            x += vel
        else:
            x = WIDTH - width
    else:
        right = False
        left = False
        walkCount = 0
        
    if not(isJump):   
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
            print("Jumping...")
    else: #if isJump True 
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.3 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            

            
    # DRAW
    DrawGameWindow()
    
    

 
#EXIT
pygame.quit()



