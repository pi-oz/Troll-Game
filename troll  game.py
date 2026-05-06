import pygame
import random as r
import math
import mixer

# initialization part
pygame.init()
pygame.mixer.init()

# display part
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption("Catch me!")

# Game variables
black=(0,0,0)
white=(255,255,255)
ball_radius=20
ball_x=r.randint(50,950)
ball_y=r.randint(150,550)
score=0
dimension=20
font = pygame.font.SysFont(None, 48)
running=True
clock=pygame.time.Clock()
pygame.draw.circle(screen,black,(ball_x,ball_y),ball_radius)
def sound(music):
    so=pygame.mixer.Sound(music)
    so.play()

# Game loop
while running:
    screen.fill(white)
    score_text=font.render(f"Score:{score}",True,black)
    screen.blit(score_text,(10,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                run==False
    mo=pygame.mouse.get_pos()
    pygame.draw.circle(screen,black,(ball_x,ball_y),ball_radius)
    x,y= pygame.mouse.get_pos()
    distance=math.sqrt((ball_x-x)**2+(ball_y-y)**2)
    if distance<ball_radius+dimension:
        ball_x=r.randint(50,950)
        ball_y=r.randint(100,550)
        emoji=font.render("HA HA!!!",True,black)
        screen.blit(emoji,(140,10))
        sound("music.mp3")
    if distance<ball_radius:
        score+=1
    pygame.display.update()
    clock.tick(60)
pygame.quit()