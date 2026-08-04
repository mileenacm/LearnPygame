import pygame 
import sys 
from pygame.locals import *


pygame.init()

#screen
width = 400
height = 300
#tela que pode redefinir o tamanho
#(width, height), pygame.RESIZABLE)
screen = pygame.display.set_mode((width, height), 0, 32)
title = pygame.display.set_caption(' Endless cat :) ')

catImg = pygame.image.load('cat.png')
catx = 10 
caty = 10 
direction = 'right' 

RED = (255,0,0)

#fps
clock = pygame.time.Clock()


#background
#branco = (255,255,255)
color = (255,120,90)
screen.fill(color)
pygame.display.flip()
#fundo = pygame.image.load("imagens/menu/corporate.png")



#icon
pygame_icon = pygame.image.load("cat.png")
pygame.display.set_icon(pygame_icon)


#enemie
#enemie_basic = pygame.image.load("space invaders/space_invader_enemie.png")
#img com o fundo transparente 

#pygame.draw.ellipse(screen, RED, (300, 250, 40, 80), 1)
#pygame.Surface.set_colorkey (enemie_basic, [0,0,0])
#resize
#enemie_basic_small = pygame.transform.scale(enemie_basic, (60,60))

#screen.blit(enemie_basic_small, (100, 100))





run = True
while run:

    screen.fill(RED)

    if direction == 'right': 
        catx += 5 
        if catx == 280: 
             direction = 'down' 
    elif direction == 'down': 
        caty += 5 
        if caty == 220: 
             direction = 'left' 
    elif direction == 'left': 
         catx -= 5 
         if catx == 10: 
             direction = 'up' 
    elif direction == 'up': 
         caty -= 5 
         if caty == 10: 
             direction = 'right' 
  
    screen.blit(catImg, (catx, caty)) 



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #desenhar o fundo a partir da imagem
    #screen.blit(fundo, (0,0))
    

    pygame.display.update()

    clock.tick(60)



pygame.quit()
