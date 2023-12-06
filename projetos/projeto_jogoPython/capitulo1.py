guerreiro='Jacthor'
#personagem
dano=0
defesa=0
sorte=0
# modulos usados
import time
import random

#background cap1
print(f'{guerreiro} era muito astusto, você quer um exemplo? Ele nunca errava uma advinhação')
time.sleep(3)
print('Você acha isso fácil? Vamos tentar')

time.sleep(3)
print('Primeiro desafio! Valendo 10 pontos de dano.\n')

print("Comecando o jogo...")
time.sleep(3)
chute=0
vidas=3
numerorandom= random.randint(0, 10)
while chute != numerorandom:
    chute = int(input('Chute um número entre 0 e 10\n> '))
    if chute == numerorandom:
        dano=dano+10
        print(f'Parabéns você acertou!\nParece fácil, mas futuramente irá continuar\nSeu dano agora é {dano}')
        break
    else:
        print(f'Eu disse que não era tão fácil assim!')
        vidas=vidas-1
        print(f'Menos uma vida, restam {vidas}')
    if vidas == 0:
        print('suas vidas acabaram!')
        print('Bom, não é tão facil assim, certo?')
        break

