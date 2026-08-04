import pygame
from sys import exit


class Tela():

    def __init__(self):
        pygame.init()
        pygame.mixer.init() # Inicializa o sistema de áudio do Pygame

        # criando a tela
        self.width = 1408
        self.height = 768

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.titulo = pygame.display.set_caption('My boss wants to put his fangs in me! I kinda like it..')

        self.clock = pygame.time.Clock()

        # classe para imagens do jogo
        # carregar imagem de fundo
        self.fundo_menu = pygame.image.load("imagens/menu/corporate.png")
        # carregar imagem do botão de start e exit
        self.start_img = pygame.image.load("imagens/menu/botao_start.png")
        self.exit_img = pygame.image.load("imagens/menu/botao_exit.png")

        # carregando todas as cenas principais
        self.cena1 = pygame.image.load("imagens/cenas principais/cena1.png")
        self.cena2 = pygame.image.load("imagens/cenas principais/cena2.png")
        self.cena3 = pygame.image.load("imagens/cenas principais/cena3.png")
        self.cena4 = pygame.image.load("imagens/cenas principais/cena4.png")
        self.cena5 = pygame.image.load("imagens/cenas principais/cena5.png")
        self.cena5_1 = pygame.image.load("imagens/cenas principais/cena5_1.png")
        self.cena5_2 = pygame.image.load("imagens/cenas principais/cena5_2.png")
        self.cena6 = pygame.image.load("imagens/cenas principais/cena6.png")
        self.cena7 = pygame.image.load("imagens/cenas principais/cena7.png")
        self.cena8 = pygame.image.load("imagens/cenas principais/cena8.png")
        self.cena8_1 = pygame.image.load("imagens/cenas principais/cena8_1.png")
        self.cena8_2 = pygame.image.load("imagens/cenas principais/cena8_2.png")
        self.cena9 = pygame.image.load("imagens/cenas principais/cena9.png")
        self.cena10 = pygame.image.load("imagens/cenas principais/cena10.png")
        self.cena11 = pygame.image.load("imagens/cenas principais/cena11.png")

        # Variável para controlar qual música está tocando no momento
        self.musica_atual = None

        # dialogo
        self.fonte = pygame.font.SysFont("Times New Roman", 27, italic = True)
        self.texto_dialogo = 'Olá'

        # criar instancias dos botoes
        self.start_button = Botao(779, 440, self.start_img, 0.49)
        self.exit_button = Botao(779, 590, self.exit_img, 0.49)

        # estados, variaveis para guardar os estados atuais do jogo
        self.estado = 'MENU'
        
        # HISTÓRICO: necessário para saber qual era a cena anterior (incluindo o menu)
        self.historico = []

    def gerenciar_musica(self):
        """Define e toca a música correspondente à cena atual"""
        proxima_musica = None

        # Menu e Cenas 1 até 5_1 (Bach)
        if self.estado in ['MENU', 'CENA1', 'CENA2', 'CENA3', 'CENA4', 'CENA5', 'CENA5_1']:
            proxima_musica = "imagens/sons_cenas/03 - Bach - Violin Concerto No.2 in E Major - Allegro - BWV 1042.mp3"

        # Cenas 5_2 até 7 (Debussy)
        elif self.estado in ['CENA5_2', 'CENA6', 'CENA7']:
            proxima_musica = "imagens/sons_cenas/04 - Debussy - Clair De Lune, L. 75, Arr. for Music Box.mp3"

        # Cenas 8 até 11 (Liszt)
        elif self.estado in ['CENA8', 'CENA8_1', 'CENA8_2', 'CENA9', 'CENA10', 'CENA11']:
            proxima_musica = "imagens/sons_cenas/08 - Liszt - Liebestraum No. 3, Love Dream, S. 541 - Arr. for Music Box.mp3"

        # Troca a música apenas se a nova música for diferente da que já está tocando
        if proxima_musica != self.musica_atual:
            self.musica_atual = proxima_musica
            if proxima_musica is not None:
                try:
                    pygame.mixer.music.load(proxima_musica)
                    pygame.mixer.music.play(-1) # -1 toca em loop continuo
                except pygame.error:
                    print(f"Erro ao carregar o arquivo de áudio: {proxima_musica}")
            else:
                pygame.mixer.music.stop()

    def desenhar_texto(self, texto, x, y, largura_maxima):
        palavras = texto.split(' ')
        linhas = []
        linha_atual = ""

        for palavra in palavras:
            teste_linha = linha_atual + palavra + " "
            largura_teste, altura_teste = self.fonte.size(teste_linha)

            if largura_teste <= largura_maxima:
                linha_atual = teste_linha
            else:
                linhas.append(linha_atual)
                linha_atual = palavra + " "
        
        linhas.append(linha_atual)

        y_offset = 0
        for linha in linhas:
            superficie_texto = self.fonte.render(linha, True, (255, 255, 255))
            self.screen.blit(superficie_texto, (x, y + y_offset))
            y_offset += self.fonte.get_linesize()

    def desenhar_caixa_dialogo(self):
        largura_caixa = self.width - 100
        altura_caixa = 120
        x_caixa = 50
        y_caixa = self.height - altura_caixa - 30
                
        pygame.draw.rect(self.screen, (20, 20, 20), (x_caixa, y_caixa, largura_caixa, altura_caixa))
        pygame.draw.rect(self.screen, (255, 255, 255), (x_caixa, y_caixa, largura_caixa, altura_caixa), 3)
                
        largura_maxima_texto = largura_caixa - 40 
        self.desenhar_texto(self.texto_dialogo, x_caixa + 20, y_caixa + 20, largura_maxima_texto)

    def desenhar_na_tela(self):
        if self.estado == 'MENU':
            self.screen.blit(self.fundo_menu, (0, 0))

        elif self.estado == 'CENA1':
            self.screen.blit(self.cena1, (0, 0))
            self.desenhar_caixa_dialogo()

        elif self.estado == 'CENA2':
            self.screen.blit(self.cena2, (0, 0))
            self.desenhar_caixa_dialogo()

        elif self.estado == 'CENA3':
            self.screen.blit(self.cena3, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA4':
            self.screen.blit(self.cena4, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA5':
            self.screen.blit(self.cena5, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA5_1':
            self.screen.blit(self.cena5_1, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA5_2':
            self.screen.blit(self.cena5_2, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA6':
            self.screen.blit(self.cena6, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA7':
            self.screen.blit(self.cena7, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA8':
            self.screen.blit(self.cena8, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA8_1':
            self.screen.blit(self.cena8_1, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA8_2':
            self.screen.blit(self.cena8_2, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA9':
            self.screen.blit(self.cena9, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA10':
            self.screen.blit(self.cena10, (0, 0))
            self.desenhar_caixa_dialogo()
            
        elif self.estado == 'CENA11':
            self.screen.blit(self.cena11, (0, 0))

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.estado != 'MENU':
                        self.avancar_cena()
                
                elif event.key == pygame.K_LEFT:
                    if self.estado != 'MENU':
                        self.voltar_cena()
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.estado != 'MENU':
                    self.avancar_cena()

    def avancar_cena(self):
        self.historico.append(self.estado)

        if self.estado == 'CENA1':
            self.estado = 'CENA2'
            self.texto_dialogo = 'Minha vida mudou completamente com a chegada do chefe transferido de uma sede fora do país. Me sinto mais disposto com as novas mudanças. Eu trabalho menos, tenho mais vontade de evoluir com a empresa e ajudar meus colegas durante as tarefas.'

        elif self.estado == 'CENA2':
            self.estado = 'CENA3'
            self.texto_dialogo = 'Às vezes eu sentia ele me encarando, mas quando eu olhava não havia ninguém. Nessa época, pensei ser a minha mente pregando peças...'

        elif self.estado == 'CENA3':
            self.estado = 'CENA4'
            self.texto_dialogo = 'No começo ele foi mais sutil, me ajudando com as demandas que eu deixava para a noite, sempre ficávamos nós dois. Ele era como eu, não saia para o happy hour com os outros funcionários. Nós nos entendíamos assim.'

        elif self.estado == 'CENA4':
            self.estado = 'CENA5'
            self.texto_dialogo = 'Uma noite ele me chamou para jantar, foi inesperado, mas eu aceitei. O restaurante era o mais caro que eu já tinha visto, expressei minha preocupação com o valor e ele disse que eu não deveria me preocupar, ele pagaria. Eu deveria chamá-lo de Romeu em troca.'

        elif self.estado == 'CENA5':
            self.estado = 'CENA5_1'
            self.texto_dialogo = 'Noite esquisita aquela, ele nem tocou na comida e me encarava como se eu fosse o nascer do sol e a aurora boreal. Obviamente eu ficava constrangido. Ninguém me tratou como se eu fosse tão importante assim antes.'

        elif self.estado == 'CENA5_1':
            self.estado = 'CENA5_2'
            self.texto_dialogo = 'Conversamos sobre tudo. Ele me falou sobre o vasto mundo lá fora, o quanto apreciava arte e cultura. Sobre o seu passado e a família, ele expressou que aquele assunto estava proibido e eu percebi sua expressão de raiva, como se estivesse perturbado.'

        elif self.estado == 'CENA5_2':
            self.estado = 'CENA6'
            self.texto_dialogo = 'No outro dia, ele me evitou e aquilo doeu muito. Meu coração acelerava sempre que eu o via falando com outros funcionários, sem tempo pra mim. Eu não tinha feito nada de errado...'

        elif self.estado == 'CENA6':
            self.estado = 'CENA7'
            self.texto_dialogo = 'Durante semanas, esse foi o comportamento dele. Como um robô, Romeu passou a me tratar como se eu fosse só mais um funcionário. Acho que eu me enganei desde o começo. Disfarcei minha tristeza durante o dia e bebi ela durante a noite.'

        elif self.estado == 'CENA7':
            self.estado = 'CENA8'
            self.texto_dialogo = 'Até que em uma noite como qualquer outra, tudo mudou! Ficamos a sós e ele me procurou, em desespero, ele caiu de joelhos, dizendo que não suportava mais aquilo. Lágrimas desciam de seu rosto, mas... eram vermelhas! Eu corri, só que ele foi mais rápido e me prendeu contra a parede. Seus braços fortes como gaiolas deliciosas.'

        elif self.estado == 'CENA8':
            self.estado = 'CENA8_1'
            self.texto_dialogo = 'Ele me contou que nós dois estávamos destinados. Romeu era um vampiro de 350 anos, quando foi transformado estava em uma viagem de negócios, retornou o mais rápido que pode para compartilhar o dom com seu amante, mas acabou perdendo Anastasius para uma grave doença.'

        elif self.estado == 'CENA8_1':
            self.estado = 'CENA8_2'
            self.texto_dialogo = 'Todo esse tempo ele vagou a procura de seu amor, já sem esperanças, até conhecer Yuto, inesperadamente. Romeu me mostrou uma foto antiga de seu amante e era como me olhar no espelho. Aquilo tudo era uma insanidade... e eu gostava disso.'

        elif self.estado == 'CENA8_2':
            self.estado = 'CENA9'
            self.texto_dialogo = '(Uma foto polaroid de Romeu mordendo o pescoço de Yuto...)'

        elif self.estado == 'CENA9':
            self.estado = 'CENA10'
            self.texto_dialogo = '[ARQUIVO POLICIAL]: Dois funcionários são suspeito de assassinarem o andar inteiro e desaparecerem.'
            
        elif self.estado == 'CENA10':
            self.estado = 'CENA11'
            self.texto_dialogo = '' 
        
        elif self.estado == 'CENA11':
            self.historico.pop()

    def voltar_cena(self):
        if len(self.historico) > 0:
            self.estado = self.historico.pop()

            if self.estado == 'MENU':
                self.texto_dialogo = 'Olá'
            elif self.estado == 'CENA1':
                self.texto_dialogo = '(Yuto) Minha rotina maçante começava sempre às 10 da manhã e terminava às 10 da noite. Todos os dias a mesma coisa. Até que o nosso chefe se envolveu com mais de um dos funcionários, assediando-os e foi demitido.'
            elif self.estado == 'CENA2':
                self.texto_dialogo = 'Minha vida mudou completamente com a chegada do chefe transferido de uma sede fora do país. Me sinto mais disposto com as novas mudanças. Eu trabalho menos, tenho mais vontade de evoluir com a empresa e ajudar meus colegas durante as tarefas.'
            elif self.estado == 'CENA3':
                self.texto_dialogo = 'Às vezes eu sentia ele me encarando, mas quando eu olhava não havia ninguém. Nessa época, pensei ser a minha mente pregando peças...'
            elif self.estado == 'CENA4':
                self.texto_dialogo = 'No começo ele foi mais sutil, me ajudando com as demandas que eu deixava para a noite, sempre ficávamos nós dois. Ele era como eu, não saia para o happy hour com os outros funcionários. Nós nos entendíamos assim.'
            elif self.estado == 'CENA5':
                self.texto_dialogo = 'Uma noite ele me chamou para jantar, foi inesperado, mas eu aceitei. O restaurante era o mais caro que eu já tinha visto, expressei minha preocupação com o valor e ele disse que eu não deveria me preocupar, ele pagaria. Eu deveria chamá-lo de Romeu em troca.'
            elif self.estado == 'CENA5_1':
                self.texto_dialogo = 'Noite esquisita aquela, ele nem tocou na comida e me encarava como se eu fosse o nascer do sol e a aurora boreal. Obviamente eu ficava constrangido. Ninguém me tratou como se eu fosse tão importante assim antes.'
            elif self.estado == 'CENA5_2':
                self.texto_dialogo = 'Conversamos sobre tudo. Ele me falou sobre o vasto mundo lá fora, o quanto apreciava arte e cultura. Sobre o seu passado e a família, ele expressou que aquele assunto estava proibido e eu percebi sua expressão de raiva, como se estivesse perturbado.'
            elif self.estado == 'CENA6':
                self.texto_dialogo = 'No outro dia, ele me evitou e aquilo doeu muito. Meu coração acelerava sempre que eu o via falando com outros funcionários, sem tempo pra mim. Eu não tinha feito nada de errado...'
            elif self.estado == 'CENA7':
                self.texto_dialogo = 'Durante semanas, esse foi o comportamento dele. Como um robô, Romeu passou a me tratar como se eu fosse só mais um funcionário. Acho que eu me enganei desde o começo. Disfarcei minha tristeza durante o dia e bebi ela durante a noite.'
            elif self.estado == 'CENA8':
                self.texto_dialogo = 'Até que em uma noite como qualquer outra, tudo mudou! Ficamos a sós e ele me procurou, em desespero, ele caiu de joelhos, dizendo que não suportava mais aquilo. Lágrimas desciam de seu rosto, mas... eram vermelhas! Eu corri, só que ele foi mais rápido e me prendeu contra a parede. Seus braços fortes como gaiolas deliciosas.'
            elif self.estado == 'CENA8_1':
                self.texto_dialogo = 'Ele me contou que nós dois estávamos destinados. Romeu era um vampiro de 350 anos, quando foi transformado estava em uma viagem de negócios, retornou o mais rápido que pode para compartilhar o dom com seu amante, mas acabou perdendo Anastasius para uma grave doença.'
            elif self.estado == 'CENA8_2':
                self.texto_dialogo = 'Todo esse tempo ele vagou a procura de seu amor, já sem esperanças, até conhecer Yuto, inesperadamente. Romeu me mostrou uma foto antiga de seu amante e era como me olhar no espelho. Aquilo tudo era uma insanidade... e eu gostava disso.'
            elif self.estado == 'CENA9':
                self.texto_dialogo = '(Uma foto polaroid de Romeu mordendo o pescoço de Yuto...)'
            elif self.estado == 'CENA10':
                self.texto_dialogo = '[ARQUIVO POLICIAL]: Dois funcionários são suspeito de assassinarem o andar inteiro e desaparecerem.'
            elif self.estado == 'CENA11':
                self.texto_dialogo = ''

    def atualizar(self):
        self.gerenciar_musica() 

        if self.estado == 'MENU':
            if self.exit_button.mostrar_na_tela(self.screen):
                pygame.quit()
                exit()
            
            if self.start_button.mostrar_na_tela(self.screen):
                self.historico.clear()
                self.historico.append('MENU')
                
                self.estado = 'CENA1'
                self.texto_dialogo = '(Yuto) Minha rotina maçante começava sempre às 10 da manhã e terminava às 10 da noite. Todos os dias a mesma coisa. Até que o nosso chefe se envolveu com mais de um dos funcionários, assediando-os e foi demitido.'
            
    def rodando(self):
        rodando = True
        while rodando:
            self.eventos()
            self.desenhar_na_tela()
            self.atualizar()
            pygame.display.update()
            self.clock.tick(60)


# classe para os botões
class Botao():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def mostrar_na_tela(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y)) 

        return action


# game loop = onde tudo acontece
jogo = Tela()
jogo.rodando()

#criar máquina de estados do jogo para trocar de cena
#primeiro cria os estados e depois o gerenciador de estados

#class 

'''lore'''
#minha rotina maçante começava sempe as 10 da manha até as 10 da noite. Todos os dias a mesma coisa. Até que o nosso chefe se envolveu com mais de uma das funcionarias, asseadiando elas e foi demitido.

#Minha vida mudou completamente com a chegada chefe transferido de uma sede fora do país.
# as vezes eu sinto ele me encarando, mas quando eu olho não há ninguém


## Não sei o que o chefe reparou em mim... #não preciso ser tão profunda
##