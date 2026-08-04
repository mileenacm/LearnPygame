# inicializando os módulos
import pygame
pygame.init()

largura = 800
altura = 600

x = largura/2
y = altura/2
vel_x = 0
vel_y = 0

gravidade = 0.5
velocidade = 5
chao = False

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

#cores RGB: tuplas
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0,0,0)
branco = (255,255,255)

#Aqui o jogo acontece 
rodando = True
while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and chao:
                vel_y = -13
    
    keys = pygame.key.get_pressed()
    vel_x = 0
    if keys[pygame.K_LEFT]: vel_x = -velocidade
    if keys[pygame.K_RIGHT]: vel_x = velocidade

    vel_y += gravidade
    x += vel_x
    y += vel_y

    if y >= 550:
        y = 600
        vel_y = 0
        chao = True
    else:
        chao = False

    x = max(0, min(x,770))

    tela.fill((15,23,42))
    clock.tick(60)

    #retângulo
    pygame.draw.rect(tela,branco,(x,y,40,70))

    #círculo
   #pygame.draw.circle(tela, azul, (100,100), 60) 

    #linha
    #pygame.draw.line(tela, vermelho, (10,10), (800,800), 6) '''



    pygame.display.flip()

pygame.quit()




