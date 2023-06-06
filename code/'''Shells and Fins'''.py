# Shells and Fins
#Grupo 9
#Por: Arthur Francisco, Arthur Palmeira, Celso de Lira, Davi Leahy, José Samuel e Victor Leão.

# Imports ---------------------------------------------------------------------------------------------------------]

import time
import random

# Cores -----------------------------------------------------------------------------------------------------------]

finalizar_cor = '\033[0m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
cyan = '\033[36m'
lightgrey = '\033[37m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
lightcyan = '\033[96m'

# Classes --------------------------------------------------------------------------------------------------------]

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
            self.municao = self.municao - 1
            print('\nAtirou!\n')
            # self.municao -= 1

    def inspecionar(self):
        print(f'\nExibindo informações da sua arma:\n\n\
            Nome: {self.nome}\
            Dano: {self.dano}\
            Precisão: {self.precisao}\
            Munição: {self.municao}\
            ')
        
class Char(Arma):
    def __init__(self, player_name, equipe, Arma, vida = 100):
        self.player_name = player_name
        self.vida = vida
        self.Arma = Arma
        self.equipe = equipe 
        self.defesa = False

    def atacar(self):
        self.Arma.atirar()
        acerto = random.randint(1,100) # Pega um numero entre 1 e 100, no range da precisão, acerta.

        if self.Arma.precisao < acerto:
            return False
        elif self.Arma.precisao >= acerto:
            return True
    
    def defender(self):
        print('Você defende!')
        self.defesa = True # Retorna para false depois
    
    def status(self):
        print(f'\n{lightgreen}Exibindo status do jogador:\n\n\
        Nome: {self.player_name}\
        Equipe: {self.equipe}\
        HP: {self.vida}\
        \n{finalizar_cor}')
        self.Arma.inspecionar()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= JOGO =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def ui():

    moeda = random.randint(1,2)
    while True:
        
        if moeda == 1:
            print(f'\n{lightblue}{player1.player_name}, VAMOS!{finalizar_cor}\n')

            ações = int(input('Escolha uma opção:\n(1) ATIRAR (2) DEFENDER (3) RECARREGAR\n-> '))  

            if ações == 1:
                if player1.Arma.municao == 0:
                    print('\nVocê está sem munição.\nRecarregando.\n')
                    player2.Arma.recarregar()
                    moeda = 2

                elif player1.atacar() == False:
                    print(f'\n{red}Você errou!{finalizar_cor}\n')
                    moeda = 2

                elif player1.atacar() == True:
                    print(f'\n{green}Você acerta!{finalizar_cor}\n')

                    if player2.defesa == True:
                        dmg = player1.Arma.dano / 2
                        player2.vida -= dmg
                        print(f'\n{player2.player_name} Tomou {dmg} de dano!\nVida restante: {player2.vida}\n')
                        moeda = 2
                        if player2.vida <= 0: # morte
                            print(f'\n\n{orange}{player2.player_name} foi derrotado!\nVocê venceu {player1.player_name}!\n')
                            input('Insira qualquer botão pra finalizar. ')
                            break

                    elif player2.defesa == False:
                        dmg = player1.Arma.dano
                        player2.vida -= dmg
                        print(f'{player2.player_name} Tomou {dmg} de dano!\nVida restante: {player2.vida}')
                        if player2.vida <= 0: # morte
                            print(f'\n\n{orange}{player2.player_name} foi derrotado!\nVocê venceu {player1.player_name}!\n')
                            input('Insira qualquer botão pra finalizar. ')
                            break
                
            elif ações == 2:
                player1.defender()
                moeda = 2
            elif ações == 3:
                player1.Arma.recarregar() 
                moeda = 2  

            player1.defesa = False
            moeda = 2 # Muda o turno pra o p2

        elif moeda == 2:
            print(f'\n{lightred}{player2.player_name}, VAMOS!{finalizar_cor}\n')

            ações = int(input('Escolha uma opção:\n(1) ATIRAR (2) DEFENDER (3) RECARREGAR\n-> '))  

            if ações == 1:
                if player2.Arma.municao == 0:
                    print('\nVocê está sem munição.\nRecarregando.\n')
                    player2.Arma.recarregar()
                    moeda = 1    
                elif player2.atacar() == False:
                    print(f'\n{red}Você errou!{finalizar_cor}\n')
                    moeda = 1

                elif player2.atacar() == True:
                    print(f'\n{green}Você acerta!{finalizar_cor}\n')

                    if player1.defesa == True:
                        dmg = player2.Arma.dano / 2
                        player1.vida -= dmg
                        print(f'\n{player1.player_name} Tomou {dmg} de dano!\nVida restante: {player1.vida}\n')
                        moeda = 1
                        if player1.vida <= 0:# morte
                            print(f'\n\n{orange}{player1.player_name} foi derrotado!\nVocê venceu {player2.player_name}!\n')
                            input('Insira qualquer botão pra finalizar. ')
                            break

                    elif player1.defesa == False:
                        dmg = player2.Arma.dano
                        player1.vida -= dmg
                        print(f'\n{player1.player_name} Tomou {dmg} de dano!\nVida restante: {player1.vida}\n')

                        if player1.vida <= 0: # morte
                            print(f'\n\n{orange}{player1.player_name} foi derrotado!\nVocê venceu {player2.player_name}!\n')
                            input('Insira qualquer botão pra finalizar. ')
                            break
                                                  
            elif ações == 2:
                player2.defender()
                moeda = 1

            elif ações == 3:
                player2.Arma.recarregar()
                moeda = 1

            moeda = 1 # Muda o turno pra o p1
                
def jogo():
    print(f'\n{cyan}Show, vamos começar!\nO primeiro a jogar será...\n')
    ui()

# Armas ----------------------------------------------------------------------------------------------------------------------------------]

AK2O = Arma('AK2O', 24, 55, 4, 4) #rifle
BubbleBlaster = Arma('BubbleBlaster', 50, 30, 2, 2) #shotgun
PowerWasher = Arma('PowerWasher', 34, 80, 1, 1) #Sniper

AK2O_p2 = Arma('AK2O', 24, 55, 4, 4) #rifle
BubbleBlaster_p2 = Arma('BubbleBlaster', 50, 30, 2, 2) #shotgun
PowerWasher_p2 = Arma('PowerWasher', 34, 80, 1, 1) #Sniper

dic_armas = {
    f'\n{orange}(1) AK2O': ('Dano: 24','Precisão: 55','Munição: 4'),
    '(2) BubbleBlaster': ('Dano: 50','Precisão: 30','Munição: 2'),
    '(3) PowerWasher': ('Dano: 34','Precisão: 80','Munição: 1')
}

# Inicialização --------------------------------------------------------------------------------------------------------------------------]
 
print(green,'\n\nBem vindo ao Shells and Fins!\n',finalizar_cor) # Inicio

escolha = int(input('Escolha uma opção:\n(1) Jogar (2) Sair\n-> ')) 
while escolha not in range(1,3):
    print('Escolha uma opção disponivel.')
    escolha = int(input('Escolha uma opção:\n(1) Jogar (2) Sair\n-> '))
if escolha == 1:
    print('Iniciando...')
    time.sleep(1)

elif escolha == 2:
    print('Fechando...')
    time.sleep(2)
    quit()

# Criando as equipes e adicionando os jogadores ------------------------------------------------------------------------------------------]

Fins = []
Shells = []

# Player 1
nome = input('\nInsira seu nome: ')
print(f'Ok {nome}, vamos lá!\n')
time.sleep(1)

equipe = int(input('\nSelecione sua equipe:\n(1) Peixe (2) Crustáceos\n-> '))
while equipe not in range(1,3):
    print(red,'Escolha uma opção disponivel.',finalizar_cor)
    equipe = int(input('\nSelecione sua equipe:\n(1) Peixe (2) Crustáceos\n-> '))

if equipe == 1:
    equipe = 'Peixes'
    Fins.append(nome)

elif equipe == 2:
    equipe = 'Crustáceos'
    Shells.append(nome)

for k,v in dic_armas.items(): #Revelando as armas disponiveis para o jogador escolher
    print(k,v)
time.sleep(2)
escolha_arma = int(input(f'{finalizar_cor}\nSelecione uma arma!\n-> '))

while escolha_arma not in range(1,4):
    print('Escolha uma opção disponivel.')

    for k,v in dic_armas.items():
        print(k,v)
    time.sleep(2)
    escolha_arma = int(input(f'\nSelecione uma arma!\n-> '))

else:

    if escolha_arma == 1:
        escolha_arma = AK2O
    elif escolha_arma == 2:
        escolha_arma = BubbleBlaster
    elif escolha_arma == 3:
        escolha_arma = PowerWasher

player1 = Char(nome,equipe,escolha_arma) #Atribuindo Jogador à class
# Player 2
print('\nSua vez Player 2! Você estará na equipe restante.\n')

nome2 = input('Insira seu nome: ')
time.sleep(1)
if equipe == 'Peixes':
    equipe2 = 'Crustáceos'
    Shells.append(nome)

elif equipe == 'Crustáceos':
    equipe2 = 'Peixes'
    Fins.append(nome)

for k,v in dic_armas.items():
    print(k,v)
time.sleep(2)
escolha_arma2 = int(input(f'\n{finalizar_cor}Selecione uma arma!\n-> '))

while escolha_arma2 not in range(1,4):
    print('Escolha uma opção disponivel.')

    for k,v in dic_armas.items():
        print(k,v)
    escolha_arma2 = int(input(f'\nSelecione uma arma!\n-> '))

else:

    if escolha_arma2 == 1:
        escolha_arma2 = AK2O_p2
    elif escolha_arma2 == 2:
        escolha_arma2 = BubbleBlaster_p2
    elif escolha_arma2 == 3:
        escolha_arma2 = PowerWasher_p2
       
player2 = Char(nome2,equipe2,escolha_arma2) #Atribuindo o Segundo Jogador à classe

player1.status()
time.sleep(2)
player2.status()
time.sleep(2)

jogo()