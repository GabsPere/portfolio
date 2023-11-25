# Advinhe o Número

# Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número. Algumas sugestões para o programa:

# 1. Utilizar um laço de repetição para que o programa execute até que o usuário informe um número referente a opção para sair do programa.
# 2. Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. Ex: 1 a 10.
# 3. Lê o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.
import random
adorno = "-"
feito = False

while not feito:
    print("O que deseja fazer?")
    print("1 - Adivinhar o número.")
    print("2 - Sair.")
    escolha = input("> ")
    if escolha == "1":
        print("\nAdvinhe um número de 1 a 10.")
        numero = int(input("Qual o número: "))
        resultado = random.randint(0, 10)
        if numero == resultado:
            print("Parabéns, você acertou!! (:\n")
        else:
            print(f"Tente novamente. O número sorteado foi {resultado}.\n")
    elif escolha == "2":
        print("Saindo...")
        feito = True
    else:
        print("Opção inválida. Escolha entre 1 e 2.\n")
