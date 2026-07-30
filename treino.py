
import pygame
from sys import exit

pygame.init()

#criando a tela
height = 617
width = 445

screen = pygame.display.set_mode((height, width))
titulo = pygame.display.set_caption('Teste')

clock = pygame.time.Clock()

#carregar imagem de fundo
fundo = pygame.image.load("oldman_yaoi.png")

#mostrar imagem de fundo
screen.blit(fundo, (0,0))

#carregar imagem do botão de start
start = pygame.image.load("Post\Assets\Bar\_base.png")

#classe para os botões
class Button():

    def __init__(self, x, y, image, scale):

        # para a sacle das imagens
        width = image.get_width()
        height = image.get_height()

       # variaves para instanciar os botoes
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    #metodo
    def mostrar_na_tela(self):

        action = False

        # para clickar, pegue a posição do mouse
        pos = pygame.mouse.get_pos()
        
        #checar se o mouse está em cima e clicou
        if self.rect.collidepoint(pos):
            if paygme.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #para desenhar o botao na tela , depois inserir esse metodo no loop
        screen.blit(self.image, (self.rect.x, self.rect.y)) 

        return action

#criar instancias dos botoes
start_button = Button(353, 73, start, 0.8)
#exit_button e outros a mesma coisa






#game loop = onde tudo acontece
rodando = True
while True:

#metodo de inserie botoes= começa com a instancia e o metodo
    if start_button.mostrar_na_tela() == True: #quero trocar de cena
        print('start')




#Evento para fechar a tela do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#FPS
    pygame.display.update()
    clock.tick(60)



