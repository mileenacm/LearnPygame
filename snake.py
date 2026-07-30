import pygame
import random
import time

pygame.init()

largura = 600
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
preto = (0, 0, 0)

clock = pygame.time.Clock()
velocidade = 10

tamanho_bloco = 20

fonte = pygame.font.SysFont(None, 35)


def mostrar_pontuacao(pontos):
    valor = fonte.render("Pontos: " + str(pontos), True, preto)
    tela.blit(valor, (10, 10))


def jogo():

    x = largura // 2
    y = altura // 2

    x_mudanca = 0
    y_mudanca = 0

    cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20) * 20
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20) * 20

    fim_de_jogo = False

    while not fim_de_jogo:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fim_de_jogo = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0

                elif event.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0

                elif event.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0

                elif event.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        # Atualiza posição da cobra
        x += x_mudanca
        y += y_mudanca

        # Verifica colisão com bordas
        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_de_jogo = True

        tela.fill(branco)

        # Desenha comida
        pygame.draw.rect(
            tela,
            vermelho,
            (comida_x, comida_y, tamanho_bloco, tamanho_bloco)
        )

        # Cabeça da cobra
        cabeca = [x, y]
        cobra.append(cabeca)

        if len(cobra) > comprimento_cobra:
            del cobra[0]

        # Verifica colisão com o próprio corpo
        for bloco in cobra[:-1]:
            if bloco == cabeca:
                fim_de_jogo = True

        # Desenha a cobra
        for bloco in cobra:
            pygame.draw.rect(
                tela,
                verde,
                (bloco[0], bloco[1], tamanho_bloco, tamanho_bloco)
            )

        mostrar_pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        # Cobra comeu a comida
        if x == comida_x and y == comida_y:
            comida_x = round(
                random.randrange(0, largura - tamanho_bloco) / 20
            ) * 20

            comida_y = round(
                random.randrange(0, altura - tamanho_bloco) / 20
            ) * 20

            comprimento_cobra += 1

        clock.tick(velocidade)

    tela.fill(branco)

    mensagem = fonte.render(
        "GAME OVER - PONTOS: " + str(comprimento_cobra - 1),
        True,
        vermelho
    )

    tela.blit(mensagem, (largura // 6, altura // 3))

    pygame.display.update()

    time.sleep(3)

    pygame.quit()


jogo()