import pygame
from pygame.locals import *
import sys
import time
from random import randint, choice

pygame.init() # <--- inicia o pygame
#definindo a tela --------------------------------------------------------------------------------------------------------]
tela_largura = 1280
tela_altura = 720
framerate = pygame.time.Clock()

screen = pygame.display.set_mode((tela_largura, tela_altura)) # Define a tela do jogo
pygame.display.set_caption('Shells and Fins')
#MUSICAS E SONS-----------------------------------------------------------------------------------------------------------]
musica_menu = pygame.mixer.music.load('musica_e_sons/musica_sereia.mp3') # Define a música do menu
pygame.mixer.music.set_volume(0.02) # Define o volume da música
pygame.mixer.music.play(-1) # Loop da música caso ela acabe.

select = pygame.mixer.Sound('musica_e_sons/select.wav') # Efeito sonoro do clique
select.set_volume(0.07) # Define o volume do efeito sonoro
#icone e logo ------------------------------------------------------------------------------------------------------------]
icon = pygame.image.load('ui/wave.png') # .load é usado para ''carregar'' os arquivos
pygame.display.set_icon(icon) # <---- Define icone
logo = pygame.image.load("ui/shells and fins horizintal.png")
icon_peixe = pygame.image.load("ui\icon_peixe.png")
icon_crustaceo = pygame.image.load("ui\icon_crustaceo.png")
#FUNDOS-------------------------------------------------------------------------------------------------------------------]
imagem_fundo = pygame.image.load('ui/fundo_pokemon.jpg') # Definindo a imagem de fundo da batalha
imagem_fundo = pygame.transform.scale(imagem_fundo, (1280, 720)) # .transform muda a escala de uma imagem para a desejada

fundo_menu = pygame.image.load("ui/fundo_menu.png") # Definindo imagem de fundo do menu
fundo_menu = pygame.transform.scale(fundo_menu, (1280, 720))

fundo_selecao = pygame.image.load("ui/fundo_selecao.png")
fundo_laranja = pygame.image.load("ui/fundo_laranja.png")
#ASSETS--------------------------------------------------------------------------------------------------------------------]
    # Definindo as imagens do jogo 
bolha = pygame.image.load('sprites/bolha.png')
bolha2 = pygame.image.load('sprites/bolha.png')
bolha2 = pygame.transform.scale(bolha2, (58/1.2, 55/1.2))
bolha3 = pygame.image.load('sprites/bolha.png')
bolha3 = pygame.transform.scale(bolha3, (58/1.5, 55/1.5))

plataforma = pygame.image.load('sprites/BASE_JOGO.PNG')
plataforma = pygame.transform.scale(plataforma, (512*1.1, 251*1.))

pause = pygame.image.load('ui/pause.png')
pause = pygame.transform.scale(pause, (120/2, 118/2))

botao_azul = pygame.image.load('ui/butao azul.png')
botao_azul = pygame.transform.scale(botao_azul, (32*7, 32*3))

botao_laranja = pygame.image.load('ui/butao laranja.png')
botao_laranja = pygame.transform.scale(botao_laranja, (32*7, 32*3))

status_azul = pygame.image.load('ui/status azul.png')
status_azul = pygame.transform.scale(status_azul, (360, 280))

status_laranja = pygame.image.load('ui/status laranja.png')
status_laranja = pygame.transform.scale(status_laranja, (360, 280))

BG_ACOES = pygame.image.load('ui/tela_acoes.png')
BG_ACOES = pygame.transform.scale(BG_ACOES, (470, 400))

peixe_selecao = pygame.image.load('ui/peixe_selecao.png')
crustaceo_selecao = pygame.image.load('ui/crustaceo_selecao.png')

ak_selecao = pygame.image.load('ui/ak_selecao.png')
ak_selecao_laranja = pygame.image.load('ui\selecao_ak_laranja.png')

powerwasher_selecao = pygame.image.load('ui/powerwasher_selecao.png')
powerwasher_selecao_laranja = pygame.image.load('ui\selecao_power_laranja.png')

bubble_selecao = pygame.image.load('ui/bubble_selecao.png')
bubble_selecao_laranja = pygame.image.load('ui\selecao_bubble_laranja.png')

duvida_azul = pygame.image.load('ui/DUVIDA_AZUL.png')
duvida_laranja = pygame.image.load('ui/DUVIDA_LARANJA.png')

backarrow = pygame.image.load('ui/backarrow.png')
backarrow = pygame.transform.scale(backarrow, (65, 65))

bullet = pygame.image.load("ui/bullet.png")
bullet = pygame.transform.scale(bullet, (25, 25))
#UIS ---------------------------------------------------------------------------------------------------------------------------------]
peixarlison_ak2o_sprite_frente = pygame.image.load('sprites/peixarlison/peixarlison ak-2o.png')
peixarlison_bubbleblaster_sprite_frente = pygame.image.load("sprites\peixarlison\peixarlison_bubbleblaster.png")
peixarlison_powerwasher_sprite_frente = pygame.image.load("sprites\peixarlison\peixarlison_powerwash.png")

crabonildo_ak2o_sprite_costas = pygame.image.load("sprites\crabonildo\crabonildo_costas_ak.png")
crabonildo_bubbleblaster_sprite_costas = pygame.image.load("sprites\crabonildo\crabonildo_costas_bubble.png")
crabonildo_powerwasher_sprite_costas = pygame.image.load("sprites\crabonildo\crabonildo_costas_power.png")


teste_dano = pygame.image.load("sprites\peixarlison\peixarlison costa bubbleblaster.png")
# Classes -----------------------------------------------------------------------------------------------------------]
"""
Class Barra_De_Vida
Essa classe recebe a barra de vida com posição, valores, max hp...

posX_vida - Coordenada X da tela  que fica a barra de vida
posY_vida - Coordenada Y da tela que fica a barra de vida
l - 
a - 
max_hp - 
"""

"""
Este é o método especial __init__, que é executado quando um objeto da classe é criado. 
Ele inicializa os atributos da classe. Neste caso, os atributos são posX_vida, posY_vida, 
l, a, hp e max_hp. Esses atributos representam a posição, largura, altura, pontos de vida 
atual e pontos de vida máximos da barra de vida.

Este é um método chamado desenho_bar_vida que desenha a barra de vida em uma superfície específica (surface). Ele usa a biblioteca Pygame para desenhar dois retângulos. O primeiro retângulo é desenhado em vermelho e representa a barra de vida completa. O segundo retângulo é desenhado em uma cor verde personalizada e representa a porção da barra de vida que está cheia, com base na proporção vida_calculo.

Em resumo, essa classe Barra_De_Vida é usada para criar uma barra de vida em um jogo ou aplicativo. Ela armazena informações sobre a posição, tamanho e pontos de vida da barra, e possui um método para desenhar a barra na tela.

"""

class Barra_De_Vida():
    def __init__(self, posX_vida, posY_vida, l, a, max_hp):
        self.posX_vida = posX_vida
        self.posY_vida = posY_vida
        self.a = a
        self.l = l
        self.hp = max_hp
        self.max_hp = max_hp

    def desenho_bar_vida(self, surface):
        vida_calculo = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.posX_vida, self.posY_vida, self.l, self.a))
        pygame.draw.rect(surface, (19, 242, 75), (self.posX_vida, self.posY_vida, self.l * vida_calculo,  self.a))

class Arma:
    def __init__(self,nome,dano,precisao,municao,municao_max):
        self.nome = nome
        self.dano = dano 
        self.municao = municao
        self.precisao = precisao
        self.municao_max = municao_max

    def recarregar(self):
        self.municao = self.municao_max
        print('\nRecarregou!\n')

    def atirar(self): #testa se tem munição, se tiver, ele reduz por 1, atira mesmo no ataque()

            if self.municao > 0:
                self.municao = self.municao - 1
                # print(f'\nAtirou!\n')
                # print('mun:', self.municao)

            elif self.municao <= 0:
                print("A munição Acabou.")
                Arma.recarregar(self)

AK2O = Arma('AK2O', 24, 65, 4, 4) #Rifle
BubbleBlaster = Arma('BubbleBlaster', 45, 50, 3, 3) #Shotgun
PowerWasher = Arma('PowerWasher', 34, 70, 1, 1) #Sniper

AK2O_2 = Arma('AK2O', 24, 65, 4, 4) #Rifle
BubbleBlaster_2 = Arma('BubbleBlaster', 45, 50, 3, 3) #Shotgun
PowerWasher_2 = Arma('PowerWasher', 34, 70, 1, 1) #Sniper
#Diminuir accuracy com tiros consecutivos.(Resetar acurracy ao recarregar)
#Aumentar accuracy ao defender.

#definindo sprites ------------------------------------------------------------------------]
class Peixe(pygame.sprite.Sprite, Arma, Barra_De_Vida): #Classe para o sprite do Peixe

    def __init__(self, Arma, Barra_De_Vida):
        pygame.sprite.Sprite.__init__(self)

        self.sprites_arma = {
            AK2O: peixarlison_ak2o_sprite_frente,
            BubbleBlaster: peixarlison_bubbleblaster_sprite_frente,
            PowerWasher: peixarlison_powerwasher_sprite_frente
        } # <-- Criando lista dos sprites    
        
        self.Arma = Arma
        self.Barra_De_Vida = Barra_De_Vida
        self.image = self.sprites_arma[self.Arma]
        self.rect = self.image.get_rect()
        self.rect.topleft = x_peixe, y_peixe
        self.image = pygame.transform.scale(self.image, (340, 242))

    def atacar(self):
        acerto = randint(1,100) # Pega um numero entre 1 e 100, no range da precisão, acerta.
        self.Arma.atirar()
        if self.Arma.precisao < acerto:
            print ("PEIXE ERROU")
            return False

        if self.Arma.precisao >= acerto:
            print ("PEIXE ACERTOU MISERIA")
            vida_crustaceo.hp = vida_crustaceo.hp - self.Arma.dano
            if (vida_crustaceo.hp <= 0):
                img_vencedor = pygame.image.load('sprites/peixarlison/peixarlison_perfil.png')
                img_vencedor = pygame.transform.scale(img_vencedor, (350, 250))
                vencedor = 'Peixe'
                End_game(vencedor, img_vencedor)

           

            return True

    def defender(self):
        print('PEIXARLISON ESTA MIRANDO')
        defender = True
        #self.Arma.precisao = self.Arma.precisao + 15

    def recarregar(self):
        self.Arma.recarregar()
        print('RECARREGANDO PEIXE')        

        # self.animar = False # Define se os sprites vão rodar ou não
    
    def update(self): # <-- Anima os sprites
        self.image = self.sprites_arma[self.Arma]
        self.image = pygame.transform.scale(self.image, ((340, 242))) # <-- Mudando o tamanho da imagem
            
            
        
            
        

#dimensões do peixe
x_peixe = 800
y_peixe = 110

vida_peixe = Barra_De_Vida(posX_vida=130, posY_vida=45, l=295, a=16, max_hp=100)

all_sprites_peixe = pygame.sprite.Group()
peixe = Peixe(Arma= AK2O, Barra_De_Vida=vida_peixe)

all_sprites_peixe.add(peixe)

class Crustaceo(pygame.sprite.Sprite, Arma, Barra_De_Vida): # Mesma coisa do peixe, mas para o crustaceo

    def __init__(self, Arma, Barra_De_Vida):
        pygame.sprite.Sprite.__init__(self)

        self.sprites_armas_crustaceo = {
            AK2O_2: crabonildo_ak2o_sprite_costas,
            BubbleBlaster_2: crabonildo_bubbleblaster_sprite_costas,
            PowerWasher_2: crabonildo_powerwasher_sprite_costas
        } # <-- Criando lista dos sprites

        #-- Adiciona sprites na lista
        self.Arma = Arma
        self.Barra_de_Vida = Barra_De_Vida
        self.image = self.sprites_armas_crustaceo[self.Arma]
        self.rect = self.image.get_rect()
        self.rect.topleft = x_crustaceo, y_crustaceo
        self.image = pygame.transform.scale(self.image, (111*3, 131*3))
        #-- Desenhando as imagens

        # self.animar = False # Define se os sprites vão rodar ou não
    def atacar(self):
        self.Arma.atirar()

        acerto = randint(1,100) # Pega um numero entre 1 e 100, no range da precisão, acerta.
        if self.Arma.precisao < acerto:
            print ("CRUSTACEO ERROU")
            return False
            
        if self.Arma.precisao >= acerto:
            print ("CRUSTACEO ACERTOU")
            vida_peixe.hp = vida_peixe.hp - self.Arma.dano

            if (vida_peixe.hp <= 0):
                img_vencedor = pygame.image.load('sprites/crabonildo/crabonildo_perfil.png')
                img_vencedor = pygame.transform.scale(img_vencedor, (350, 250))
                vencedor = 'Crustaceo'
                End_game(vencedor, img_vencedor)

            return True

    def defender(self):
        print('CRABONILDO ESTA A DEFENDER')
        defender = True

    def recarregar(self):
        self.Arma.recarregar()
        print('RECARREGANDO CRUSTACEO')     

    def update(self): # <-- Anima os sprites
            self.image = self.sprites_armas_crustaceo[self.Arma]
            self.image = pygame.transform.scale(self.image, (95*3.5, 95*3)) # <-- Mudando o tamanho da imagem
        
x_crustaceo = 130
y_crustaceo = 400

vida_crustaceo = Barra_De_Vida(posX_vida=863, posY_vida=506, l=295, a=16, max_hp=100) # <-- Barra de vida 

all_sprites_crustaceo = pygame.sprite.Group()
crustaceo = Crustaceo(Arma= BubbleBlaster_2, Barra_De_Vida=vida_crustaceo) # Definindo o Crustaceo

all_sprites_crustaceo.add(crustaceo)

#Codigo do Botão------------------------------------------------------------------------------------
class Button(): # Definindo classe do botão, todos os ''cliques'' do jogo entram nessa classe
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position): # Reconhece a posição
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position): # Muda a cor do botão
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
# Função para definir a fonte do texto
def get_font(size): # Definindo a fonte utilizada e seu tamanho
    return pygame.font.Font('fontes/Super Mario Bros. 2.ttf', size)

# Menu Para escolha de times
def Menu_Times():
    global arma_escolhida_peixe, arma_escolhida_crustaceo
    arma_escolhida_peixe = None
    arma_escolhida_crustaceo = None
    escolha = True
    while escolha:
        
        screen.blit(fundo_selecao, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        times = ['Peixes', 'Crustaceos']
        OPTIONS_TEXT = get_font(30).render("Escolha Sua Raça.", True, "black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(660, 100))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        time_peixe = Button(image= peixe_selecao, pos=(330, 375), 
                                text_input="PEIXES", font=get_font(30), base_color=(0, 204, 255), hovering_color="white")
        
        time_crustaceo = Button(image= crustaceo_selecao, pos=(930, 375), 
                                text_input="CRUSTACEOS", font=get_font(25), base_color="orange", hovering_color="white")
        backarrow_back1 = Button(image=backarrow, pos=(85, 70), 
                                text_input="", font=get_font(30), base_color=(0, 204, 255), hovering_color="white")
        
        for button in [time_peixe, time_crustaceo, backarrow_back1]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if time_peixe.checkForInput(MENU_MOUSE_POS):
                    Menu_Armas_Peixe()
                if time_crustaceo.checkForInput(MENU_MOUSE_POS):
                    Menu_Armas_Crustaceo()   
                if backarrow_back1.checkForInput(MENU_MOUSE_POS):
                    main_menu() 

        pygame.display.flip()

arma_escolhida_peixe = None
arma_escolhida_crustaceo = None

# Menu de seleção de armas
def Menu_Armas_Peixe():
    global arma_escolhida_peixe
    escolha_arma = True
    while escolha_arma:
        
        screen.blit(fundo_selecao, (0,0))
        screen.blit(duvida_azul, (960, 168))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        OPTIONS_TEXT = get_font(30).render("Escolha a Arma do Peixe.", True, "black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(660, 100))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        AK2O_stats = Button(image=ak_selecao, pos=(200, 375), 
                                text_input="", font=get_font(30), base_color=(0, 204, 255), hovering_color="white")
        
        Bubble_stats = Button(image=bubble_selecao, pos=(500, 375), 
                                text_input="", font=get_font(30), base_color=(0, 204, 255), hovering_color="white")
        
        powerwasher_stats = Button(image=powerwasher_selecao, pos=(800, 375), 
                                text_input="", font=get_font(30), base_color=(0, 204, 255), hovering_color="white")
        
        backarrow_back = Button(image=backarrow, pos=(85, 70), 
                                text_input="", font=get_font(30), base_color=(0, 204, 255), hovering_color="white")
        
        AK2O_Name = Button(image=None, pos=(200, 330), 
                                text_input="AK2O", font=get_font(15), base_color=(255, 255, 255), hovering_color=(0, 204, 255))
        Bubble_Name = Button(image=None, pos=(500, 330), 
                                text_input="BubbleBlaster", font=get_font(15), base_color=(255, 255, 255), hovering_color=(0, 204, 255))
        Powerwasher_Name = Button(image=None, pos=(800, 330), 
                                text_input="PowerWasher", font=get_font(15), base_color=(255, 255, 255), hovering_color=(0, 204, 255))

        for button in [AK2O_stats,Bubble_stats,powerwasher_stats, backarrow_back, AK2O_Name, Bubble_Name, Powerwasher_Name]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AK2O_stats.checkForInput(MENU_MOUSE_POS):
                    arma_escolhida_peixe = AK2O
                    
                if Bubble_stats.checkForInput(MENU_MOUSE_POS):
                    arma_escolhida_peixe = BubbleBlaster
                    
                if powerwasher_stats.checkForInput(MENU_MOUSE_POS):
                    arma_escolhida_peixe = PowerWasher
                    
                if backarrow_back.checkForInput(MENU_MOUSE_POS):
                    Menu_Times()
            if arma_escolhida_peixe is not None and arma_escolhida_crustaceo is None:
                Menu_Armas_Crustaceo()
            if arma_escolhida_peixe is not None and arma_escolhida_crustaceo is not None:
                jogo()
               
        peixe.update()   
        pygame.display.flip()
        
def Menu_Armas_Crustaceo():
        global arma_escolhida_crustaceo
        escolha_arma_crustaceo = True
        while escolha_arma_crustaceo:

            screen.blit(fundo_laranja, (0,0))
            screen.blit(duvida_laranja, (960, 168))
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            OPTIONS_TEXT = get_font(30).render("Escolha a Arma do Crustaceo.", True, "black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(660, 100))
            screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

            AK2O_stats = Button(image=ak_selecao_laranja, pos=(200, 375), 
                                    text_input="", font=get_font(30), base_color=(0, 204, 255), hovering_color="white")
            
            Bubble_stats = Button(image=bubble_selecao_laranja, pos=(500, 375), 
                                    text_input="", font=get_font(30), base_color=(0, 204, 255), hovering_color="white")
            
            powerwasher_stats = Button(image=powerwasher_selecao_laranja, pos=(800, 375), 
                                    text_input="", font=get_font(30), base_color=(0, 204, 255), hovering_color="white")
            
            backarrow_back = Button(image=backarrow, pos=(85, 70), 
                                    text_input="", font=get_font(30), base_color=(0, 204, 255), hovering_color="white")

            AK2O_Name = Button(image=None, pos=(200, 330), 
                                    text_input="AK2O", font=get_font(15), base_color=(255, 255, 255), hovering_color="orange")
            Bubble_Name = Button(image=None, pos=(500, 330), 
                                    text_input="BubbleBlaster", font=get_font(15), base_color=(255, 255, 255), hovering_color="orange")
            Powerwasher_Name = Button(image=None, pos=(800, 330), 
                                    text_input="PowerWasher", font=get_font(15), base_color=(255, 255, 255), hovering_color="orange")
            
            for button in [AK2O_stats,Bubble_stats,powerwasher_stats, backarrow_back, AK2O_Name, Bubble_Name, Powerwasher_Name]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if AK2O_stats.checkForInput(MENU_MOUSE_POS):
                        arma_escolhida_crustaceo = AK2O_2
                        
                    if Bubble_stats.checkForInput(MENU_MOUSE_POS):
                        arma_escolhida_crustaceo = BubbleBlaster_2
                        
                    if powerwasher_stats.checkForInput(MENU_MOUSE_POS):
                        arma_escolhida_crustaceo = PowerWasher_2
                        
                    if backarrow_back.checkForInput(MENU_MOUSE_POS):
                        Menu_Times()
            if arma_escolhida_crustaceo is not None and arma_escolhida_peixe is None:
                Menu_Armas_Peixe()
            if arma_escolhida_crustaceo is not None and arma_escolhida_peixe is not None:
                jogo()
                
            crustaceo.update()
            pygame.display.flip()

#LOOP DO JOGO ---------------------------------------------------------------------] 
def jogo():
        # Resets (O que vai ser resetado quando começa o jogo, munição, vida...)
        global arma_escolhida_peixe, arma_escolhida_crustaceo
        peixe.Arma.municao = peixe.Arma.municao_max
        crustaceo.Arma.municao = crustaceo.Arma.municao_max
        peixe.Arma = arma_escolhida_peixe
        crustaceo.Arma = arma_escolhida_crustaceo
        vida_crustaceo.hp = vida_crustaceo.max_hp
        vida_peixe.hp = vida_peixe.max_hp
        arma_escolhida_crustaceo = None
        arma_escolhida_peixe = None
        pygame.mixer.music.unload #Pausa a música do menu, para não tocar durante o jogo
        pygame.mixer.music.load('musica_e_sons/musica_rocky.mp3')
        pygame.mixer.music.play(-1)
    #posições das bolhas------------------------------------------------------------]
        posX_Bolha1 = randint(720, 1200)
        posY_Bolha1 = randint(5, 450)

        posX_Bolha2 = randint(720, 1200)
        posY_Bolha2 = randint(5, 450)

        posX_Bolha3 = randint(720, 1200)
        posY_Bolha3 = randint(5, 450)
        
        turnos = ['crustaceo', 'peixe']
        turno = choice(turnos)
        
        # Event Handler do jogo
        run = True
        while run: 
           
            framerate.tick(30) # <-- fps
            MENU_MOUSE_POS = pygame.mouse.get_pos()
           
            posY_Bolha1 -= 6 # <-------- velocidade que a bolha sobe
            if (posY_Bolha1 <= 300):
                posY_Bolha1 = tela_altura
                posX_Bolha1 = randint(720, 1200) # <------ definindo aleatoriamente a posição X da bolha
        
            posY_Bolha2 -= 7
            if (posY_Bolha2 <= 300):
                posY_Bolha2 = tela_altura
                posX_Bolha2 = randint(720, 1200)

            posY_Bolha3 -= 8
            if (posY_Bolha3 <= 300):
                posY_Bolha3 = tela_altura
                posX_Bolha3 = randint(720, 1200)
                
    #Blits do jogo------------------------------------------------------------------------------------------------------------
            screen.blit(imagem_fundo, (0,0))
            
            screen.blit(bolha,(posX_Bolha1,posY_Bolha1))
            screen.blit(bolha2,(posX_Bolha2,posY_Bolha2))
            screen.blit(bolha3,(posX_Bolha3,posY_Bolha3))
            
            screen.blit(plataforma, (720,250))   # <-------  adicionando a plataforma a tela nas posições x e y
            screen.blit(plataforma, (0, 560))

            screen.blit(status_laranja, (820, 380))
            vida_crustaceo.desenho_bar_vida(screen)
            screen.blit(status_azul, (104, -80))
            vida_peixe.desenho_bar_vida(screen)

    #opções-----------------------------------------------------------------------------------------------------------------------
            OPTIONS_BUTTON = Button(image= pause, pos=(1220, 50), 
                                text_input="", font=get_font(15), base_color="white", hovering_color="orange")
            
            for button in [OPTIONS_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)
        
    #sprite all-----------------------------------------------------------------------------------------------------------------------
            all_sprites_peixe.draw(screen) #<--  Inserindo o personagem na tela
            all_sprites_peixe.update()

            all_sprites_crustaceo.draw(screen)
            all_sprites_crustaceo.update()

            if turno == 'peixe':                
                LIFE_NUMBERS = get_font(15).render(f"{vida_peixe.hp}/{vida_peixe.max_hp}", True, "white")
                AMMO_NUMBERS = get_font(15).render(f"{peixe.Arma.municao}", True, "white")
                NAME_PEIXE = get_font(23).render("PEIXARLISON", True, (0, 204, 255))
                screen.blit(BG_ACOES, (50, -80))
                screen.blit(status_azul, (104, -80))
                vida_peixe.desenho_bar_vida(screen)
                screen.blit(LIFE_NUMBERS, (300, 75))
                screen.blit(icon_peixe, (470, 55))
                screen.blit(bullet, (120, 69))
                screen.blit(AMMO_NUMBERS, (150, 75))
                screen.blit(NAME_PEIXE, (150, 13))
                BOTAO_ATAQUE_PEIXE = Button(image=botao_azul, pos=(175, 135),
                                            text_input="ATACAR", font=get_font(15), base_color="white",
                                            hovering_color="orange")
                BOTAO_DEFENDER_PEIXE = Button(image=botao_azul, pos=(400, 135),
                                                text_input="DEFENDER", font=get_font(15), base_color="white",
                                                hovering_color="orange")
                BOTAO_RECARREGAR_PEIXE = Button(image=botao_azul, pos=(285, 200),
                                                    text_input="RECARREGAR", font=get_font(13), base_color="white",
                                                    hovering_color="orange")
                for button in [BOTAO_ATAQUE_PEIXE, BOTAO_DEFENDER_PEIXE, BOTAO_RECARREGAR_PEIXE]:
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(screen)
                      
                for event in pygame.event.get():                    
                    if event.type == pygame.QUIT: # <---- verifica se o usuario fechou o app
                        run = False
                        pygame.quit()
                        sys.exit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                            options_jogo()

                        if pygame.key.get_pressed()[K_ESCAPE]:
                            options_jogo()

                        if BOTAO_ATAQUE_PEIXE.checkForInput(MENU_MOUSE_POS):
                            peixe.atacar()
                            print(f'A munição do peixe é: {peixe.Arma.municao}')
                            turno = 'crustaceo'
                        if BOTAO_DEFENDER_PEIXE.checkForInput(MENU_MOUSE_POS):
                            defender = False
                            peixe.mirar()
                            turno = 'crustaceo'

                        if BOTAO_RECARREGAR_PEIXE.checkForInput(MENU_MOUSE_POS):
                            peixe.recarregar()
                            turno = 'crustaceo'

            if turno == 'crustaceo':
                LIFE_NUMBERS = get_font(15).render(f"{vida_crustaceo.hp}/{vida_crustaceo.max_hp}", True, "orange")                
                AMMO_NUMBERS = get_font(15).render(f"{crustaceo.Arma.municao}", True, "orange")
                NAME_CRUSTACEO = get_font(23).render("CRABONILDO", True, "orange")
                screen.blit(BG_ACOES, (775, 380))
                screen.blit(status_laranja, (820, 380))
                vida_crustaceo.desenho_bar_vida(screen)
                screen.blit(LIFE_NUMBERS, (1040, 535))
                screen.blit(icon_crustaceo, (785, 510))
                screen.blit(bullet, (855, 529))
                screen.blit(AMMO_NUMBERS, (880, 535))
                screen.blit(NAME_CRUSTACEO, (900, 472))
                BOTAO_ATAQUE = Button(image= botao_laranja, pos=(900, 600), 
                            text_input="ATACAR", font=get_font(15), base_color="white", hovering_color="orange")
                            
                BOTAO_DEFENDER = Button(image= botao_laranja, pos=(1130, 600), 
                                text_input="DEFENDER", font=get_font(15), base_color="white", hovering_color="orange")

                BOTAO_RECARREGAR = Button(image= botao_laranja, pos=(1017, 670), 
                                text_input="RECARREGAR", font=get_font(13), base_color="white", hovering_color="orange")
                
                for button in [BOTAO_ATAQUE, BOTAO_DEFENDER, BOTAO_RECARREGAR]:
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(screen)  

                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: # <---- verifica se o usuario fechou o app                        
                        run = False
                        pygame.quit()
                        sys.exit()   

                    if event.type == pygame.MOUSEBUTTONDOWN:                             
                        if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                            options_jogo()

                        if pygame.key.get_pressed()[K_ESCAPE]:
                            options_jogo()
                    
                        if BOTAO_ATAQUE.checkForInput(MENU_MOUSE_POS):
                            crustaceo.atacar()
                            print(f'A munição do crustaceo é: {crustaceo.Arma.municao}')
                            turno = 'peixe'
                            
                        if BOTAO_DEFENDER.checkForInput(MENU_MOUSE_POS):
                            crustaceo.defender()
                            turno = 'peixe'
                            
                        if BOTAO_RECARREGAR.checkForInput(MENU_MOUSE_POS):
                            crustaceo.recarregar()
                            turno = 'peixe'
                                                
            pygame.display.flip() #o display.flip tem basicamente a mesma função do .update, ele atualiza os elementos na tela
#MENU----------------------------------------------------------------------------------------------------------------------

#função que mexemos no Áudio do jogo no menu fora do jogo, função chamada assim que clicamos em Som no menu_jogo --------------------------------------------------------
def audio_menu():
    select.play()
    pygame.mixer.music.unpause()
    volume = 0.03
    
    audio_menu_run = True
    while audio_menu_run:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill((38, 62, 115))
        OPTIONS_TEXT = get_font(30).render("ALTERAR VOLUME", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(660, 60))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        AUMENTAR_SOM = Button(image=None, pos=(650, 280), 
                        text_input="+", font=get_font(50), base_color="black", hovering_color="orange")
        
        DIMINUIR_SOM = Button(image=None, pos=(650, 380), 
                            text_input="-", font=get_font(50), base_color="black", hovering_color="orange")
        
        VOLTAR = Button(image=None, pos=(650, 650), 
                            text_input="voltar", font=get_font(30), base_color="black", hovering_color="orange")

        for button in [AUMENTAR_SOM, VOLTAR, DIMINUIR_SOM]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AUMENTAR_SOM.checkForInput(OPTIONS_MOUSE_POS):
                    volume += 0.01
                    
                    pygame.mixer.music.set_volume(volume)
                    select.set_volume(volume)
                    
                if DIMINUIR_SOM.checkForInput(OPTIONS_MOUSE_POS):
                    volume -= 0.01

                    pygame.mixer.music.set_volume(volume)
                    select.set_volume(volume)

                if VOLTAR.checkForInput(OPTIONS_MOUSE_POS):
                        pygame.mixer.music.pause()
                        audio_menu_run = False
                        
        pygame.display.flip()
#função do menu de opções fora do jogo, função chamada quando clicamos em ''opções'' no menu ---------------------------------------------------------------------
def options_menu():
    select.play()
    pygame.mixer.music.pause()
    
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill((38, 62, 115))

        OPTIONS_TEXT = get_font(30).render("MENU DE OPÇÕES", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 60))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        Som  = Button(image=None, pos= (640, 360),
                    text_input ="som", font=get_font(30), base_color="black", hovering_color="orange")
        
        VOLTAR_TELA_INICIAL = Button(image=None, pos=(640, 650), 
                            text_input="voltar a tela inicial", font=get_font(30), base_color="black", hovering_color="orange")

        for button in [Som, VOLTAR_TELA_INICIAL]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[K_ESCAPE]:
                 main_menu()    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Som.checkForInput(OPTIONS_MOUSE_POS):
                    audio_menu()
                if VOLTAR_TELA_INICIAL.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu() 
                    
        pygame.display.flip()
#função do menu de opções in game, funcionando também como um pause para a partida que está acontecendo. ------------------------------------------------------------------
def options_jogo():
    select.play()
    pygame.mixer.music.pause()
    
    pausado = True
    while pausado:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill((38, 62, 115))

        OPTIONS_TEXT = get_font(30).render("JOGO PAUSADO.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(660, 60))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        RETOMAR = Button(image=None, pos=(650, 280), 
                            text_input="retomar", font=get_font(30), base_color="black", hovering_color="orange")
        
        Som  = Button(image=None, pos= (640, 380),
                    text_input ="som", font=get_font(30), base_color="black", hovering_color="orange")

        VOLTAR_AO_MENU= Button(image=None, pos=(650, 480), 
                            text_input="voltar ao menu", font=get_font(30), base_color="black", hovering_color="orange")
        
        for button in [RETOMAR, Som, VOLTAR_AO_MENU]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.key.get_pressed()[K_ESCAPE]:
                pygame.mixer.music.play()
                pausado = False    
                 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETOMAR.checkForInput(OPTIONS_MOUSE_POS):
                    select.play()
                    pygame.mixer.music.unpause()
                    pausado = False # Sai do loop do menu e retorna pro loop do jogo
        
                if VOLTAR_AO_MENU.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

                if Som.checkForInput(OPTIONS_MOUSE_POS):
                    # audio_jogo()
                    audio_menu()

        pygame.display.flip()
    
def     End_game(vencedor, img_vencedor): #recebe a variavel vencedor como parametro, que é definida quando o oponente perde a vida
    select.play()
    pygame.mixer.music.unload()
    pygame.mixer.music.load('musica_e_sons/musica_win.mp3')
    pygame.mixer.music.set_volume(0.03)
    pygame.mixer.music.play(-1)

    End_loop = True

    while End_loop:
        ENDGAME_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(fundo_selecao, (0,0))

        ENDGAME_TEXT = get_font(30).render("Jogo Finalizado.", True, "white")
        ENDGAME_RECT = ENDGAME_TEXT.get_rect(center=(660, 60))
        ENDGAME_WIN_TEXT = get_font(45).render(f"{vencedor} Venceu!", True, "yellow")
        ENDGAME_WIN_RECT = ENDGAME_WIN_TEXT.get_rect(center=(660, 150))

        IMG_VENCEDOR_RECT = img_vencedor.get_rect(center=(660, 350))

        screen.blit(ENDGAME_TEXT, ENDGAME_RECT)
        screen.blit(ENDGAME_WIN_TEXT, ENDGAME_WIN_RECT)
        screen.blit(img_vencedor, IMG_VENCEDOR_RECT )   

        VOLTAR_MENU_FIM_JOGO = Button(image=None, pos=(320, 650), 
                                text_input="voltar ao menu", font=get_font(30), base_color="white", hovering_color="orange")
        
        JOGAR_NOVAMENTE = Button(image=None, pos=(950, 650), 
                                text_input="Jogar Novamente", font=get_font(30), base_color="white", hovering_color="orange")
        
        for button in [VOLTAR_MENU_FIM_JOGO, JOGAR_NOVAMENTE]:
               button.changeColor(ENDGAME_MOUSE_POS)
               button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VOLTAR_MENU_FIM_JOGO.checkForInput(ENDGAME_MOUSE_POS):
                    pygame.mixer.music.unload()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if JOGAR_NOVAMENTE.checkForInput(ENDGAME_MOUSE_POS):
                    Menu_Times()    
                   
        pygame.display.flip()   
#função da aba créditos, será chamada assim que clicar em ''créditos'' ------------------------------------------------------------------------------------
def creditos_def():
     select.play()

     creditos_loop = True
     while creditos_loop:
          OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

          screen.fill((51, 153, 255))

          OPTIONS_TEXT = get_font(30).render("Créditos.", True, "yellow")
          OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(660, 60))

          palmeira_text = get_font(30).render("Arthur Francisco.", True, "white")
          palmeira_rect = palmeira_text.get_rect(center=(660, 150))

          davi_text = get_font(30).render("Arthur Palmeira.", True, "white")
          davi_rect = davi_text.get_rect(center=(660, 200))

          francisco_text = get_font(30).render("Celso de Lira.", True, "white")
          francisco_rect = francisco_text.get_rect(center=(660, 250))

          samuel_text = get_font(30).render("Davi Leahy.", True, "white")
          samuel_rect = samuel_text.get_rect(center=(660, 300))

          vitor_text = get_font(30).render("Filipe Malgueiro.", True, "white")
          vitor_rect = vitor_text.get_rect(center=(660, 350))

          celso_text = get_font(30).render("Samuel Braga.", True, "white")
          celso_rect = celso_text.get_rect(center=(660, 400))

          felipinho_text = get_font(30).render("Victor Leão.", True, "white")
          felipinho_rect = felipinho_text.get_rect(center=(660, 450))

          screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
          screen.blit(palmeira_text, palmeira_rect)
          screen.blit(davi_text, davi_rect)
          screen.blit(francisco_text, francisco_rect)
          screen.blit(samuel_text, samuel_rect)
          screen.blit(vitor_text, vitor_rect)
          screen.blit(celso_text, celso_rect)
          screen.blit(felipinho_text, felipinho_rect)

          VOLTAR_MENU_CREDITO = Button(image=None, pos=(650, 650), 
                                text_input="voltar ao menu", font=get_font(30), base_color="white", hovering_color="orange")
          
          for button in [VOLTAR_MENU_CREDITO]:
               button.changeColor(OPTIONS_MOUSE_POS)
               button.update(screen)

          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if VOLTAR_MENU_CREDITO.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
          pygame.display.flip() 
#função do menu principal, roda assim que começar o jogo -----------------------------------------------------------------------------------------------]
def main_menu():
    pygame.mixer.music.unload
    pygame.mixer.music.load('musica_e_sons/musica_sereia.mp3')
    pygame.mixer.music.play(-1)
    select.play()
    
    while True:
        screen.blit(fundo_menu, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        screen.blit(logo, (200, 50))

        JOGAR = Button(image=None , pos=(640, 350), 
                            text_input="JOGAR", font=get_font(30), base_color="white", hovering_color="orange")

        OPCOES = Button(image=None, pos=(640, 450), 
                            text_input="OPÇÕES", font=get_font(30), base_color="white", hovering_color="orange")
        
        CREDITOS = Button(image=None, pos=(640, 550), 
                            text_input="CRÉDITOS", font=get_font(30), base_color="white", hovering_color="orange")
        
        SAIR = Button(image=None, pos=(640, 650), 
                            text_input="SAIR", font=get_font(30), base_color="white", hovering_color="orange")
    
        for button in [JOGAR, OPCOES, SAIR, CREDITOS]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if JOGAR.checkForInput(MENU_MOUSE_POS):
                    select.play()
                    # jogo()
                    Menu_Times()
                if OPCOES.checkForInput(MENU_MOUSE_POS):
                    options_menu()
                if CREDITOS.checkForInput(MENU_MOUSE_POS):
                    creditos_def()    
                if SAIR.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        
main_menu()