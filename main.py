import pygame

# Initialize pygame
pygame.init()

# Create Screen
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

#GAME LOOP
running = True
while running:
    pygame.time.delay(100)
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= vel
        else:
            x = 0
    if keys[pygame.K_RIGHT]:
        if x < (WIDTH - width):
            x += vel
        else:
            x = WIDTH - width
    if keys[pygame.K_UP]:
        if y > 0:
            y -= vel
        else:
            y = 0
    if keys[pygame.K_DOWN]:
        if y < (HEIGHT - height):
            y += vel
        else:
            y = HEIGHT - height
    # DRAW
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), (x,y,width,height))
    pygame.display.update()
    

 
#EXIT
pygame.quit()



