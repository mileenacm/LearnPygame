#inicializando
import pygame 
import sys 

pygame.init()

#tamanho da tela
largura = 600
altura = 650

#cores
branco = (255,255,255)

#criand uma surface(janela), guardada na variavel tela
#na surface nós desenhamos os objetos

tela = pygame.display.set_mode((largura, altura))

#mudar título da janela
pygame.display.set_caption("Revisando")

#clock do jogo para limitar o fps
clock = pygame.time.Clock()

#--------------------FPS significa: Frames Per Second = Quadros por Segundo--------#

#Um jogo é na verdade uma sequência de imagens mostradas muito rapidamente:
#quando as imagens mudam rápido, vemos o movimento.

#com o clock todos os pcs rodam o jogo a mesma velocidade de 60 fps
# ou seja, todo mundo ve igual
#sem o clock, algum jogador veria mais lento e outro mais rapido.

#FPS = quantas vezes o jogo atualiza por segundo.
#Clock = objeto que controla o tempo.
#clock.tick(60) = limita o jogo a 60 FPS.
#Sem Clock, cada computador roda o jogo numa velocidade diferente.

#----------------------------fps e pixel---------------------------------------#

#if teclas[pygame.K_RIGHT]:
#    jogador.x += 5

#A cada frame, mova o jogador 5 pixels para a direita

#Em um segundo, o jogador move a quantia de pixel por frame
# 60 * 5 = move 300 pixels por segundo

#usando tempo real, delta time

#velocidade = 300  pixels por segundo

#delta = clock.tick(60) / 1000, quanto tempo passou desde o ult frame
# o clock.tick retorna em milissegundos e precisamos retornar em segundos
#por isso divide por 1000

# em 60 fps cada frame dura: 1/ 60 = 0,0167 segundos = 16,7 milisegundos

#mas a velocidade está em pixel por segundo
# por isso: delta = 16/ 1000 = 0,016 segundos

#jogador.x += velocidade * delta

# 300 * 0,016 = 4,8 pixels
#neste frame o jogador anda 4,8 pixels

# e depois de 60 fps: 4,8 * 60 = 288, quase 300

# se o fps cair para 30= 1/30 = 0,033 = 300 * 0,033 = 9,9 pixels por frame
#ou seja, cada frame anda mais, compensando a diminuição
#no final de 1 segundo= 9,9 * 30 = quase 300 pixels

# com o delta time a velocidade de 300px/s é constante independente do fps jogador.x += delta *velo
# sem o delta time a velocidade muda com o fps jogador.x += 5



#-----------------------------JOGADOR---------------------------------------#

#jogador
#├── x = 100
#├── y = 100
#├── width = 50
#└── height = 50

#Quando você escreve: jogador.x += 5
#está alterando apenas o valor armazenado no campo x dessa ficha

#jogador = pygame.rect(x,y,largura,altura)
jogador = pygame.Rect(100,100,50,50) #desenhar jogador só dentro do loop
velocidade = 5 # anda 5 pixels por frame

#parede
parede = pygame.Rect(300,200,200,50)


#----------------------Loop Principal-----------------------------#
rodando = True

while rodando:
    #evento: pega todos os eventos que acontecem
    #tecla, mouse, fechar janela
    for event in pygame.event.get():

# Verifica: O usuário fechou a janela?
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #fecha o programa


#Teclado
    teclas = pygame.key.get_pressed()

#guardando posição antiga do jogador
#salva onde o player estava antes de se mover
    antigo_x = jogador.x
    antigo_y = jogador.y 

#andar para a esquerda: a seta esquerda foi pressionada?
    if teclas[pygame.K_LEFT]:
        jogador.x -= velocidade
#para a direita
    if teclas[pygame.K_RIGHT]:
        jogador.x += velocidade

#baixo
    if teclas[pygame.K_UP]:
        jogador.y -= velocidade

#cima
    if teclas[pygame.K_DOWN]:
        jogador.y += velocidade

#COLISÃO
# Pergunta:O jogador está tocando na parede?

    if jogador.colliderect(parede):
        jogador.x = antigo_x
        jogador.y = antigo_y
# se ele bateu na parede, não atravessa, volta para a posição anterior

#pintar tela
    tela.fill((0,255,0))

    pygame.draw.rect(tela, branco, jogador)
        #desenha parede vermelha:
    pygame.draw.rect(tela, (255,0,0), parede)

    pygame.display.flip()

    clock.tick(60)



pygame.quit()






















