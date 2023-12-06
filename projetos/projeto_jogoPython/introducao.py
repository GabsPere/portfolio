# Meu obejetivo é criar um jogo em Python que possa ser jogado através da CLI.
# Basicamente será feito através de perguntas e respostas, com uma história de background.

import time
guerreiro='Jacthor'

# Criação da personagem
confirmacao="N"
while confirmacao != "S":
      nome=(input('Qual seu nome?\n> '))
      confirmacao=(input(f'Seu nome será:{nome}\nTem certeza(S/N)?\n> ').upper())

cor_favorita=(input('Qual sua cor favorita?\nPS: Isso pode influenciar na sua gameplay...\n> '))
perfil=(f'Ótimo, seu nome é {nome} e sua cor favorita é {cor_favorita}.\nAproveite a jornada.')
print(perfil)

time.sleep(3)
# background
print('\nMuitos anos atrás, quando a terra ainda era um lugar hábitavel, existia um guerreiro'
      f' chamado {guerreiro}...')
time.sleep(3)
print('Por guerreiro você deve estar pensando: "Ele combatia o crime como o Batman!?" - Não')
time.sleep(3)
print('"Ele tinha super poderes??" - Eh...não também')
time.sleep(3)
print('"Ele ao menos usava uma espada e armadura? - Não..de certa forma, não.')
time.sleep(3)
print(f'{guerreiro} era um guerreiro dos enigmas, buscava resolver todo tipo de mistério que aparecesse na sua frente.')
time.sleep(3)
print(f'E você.. Isso,{nome}, você mesmo, irá conhecer essa história de cabo a rabo e de queda ainda solucionar alguns dos maiores mistérios daquela época..')
time.sleep(3)
print('Ah, isso não é um convite.\nBoa jornada!!')