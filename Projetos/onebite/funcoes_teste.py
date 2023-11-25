#modelo simples de banco com funções
valor_inicial = 1000
a = valor_inicial
mensagem_inicial=int(input("Olá seja bem vindo ao banco T&J. No que podemos te ajudar hoje?\n[1]- Depósito [2]- Saque [3]- Extrato [4]- Outros\nDigite a opção: "))
if mensagem_inicial == 1:
    valor_deposito = float(input("Qual valor deseja depositar?\nR$"))
    if valor_deposito > 0:
        def valor_depositado():
            return valor_inicial + valor_deposito
        print(f"Depósito realizado com sucesso. O valor atual é de R${valor_depositado():.2f}")
    else:
        print("Valor inválido. Por favor comece a operação novamente.")
        
 ##SAQUE
elif mensagem_inicial == 2:
    valor_saque = float(input("Qual valor deseja sacar?\nR$"))
    if valor_saque <= valor_inicial and valor_saque > 0:
        saque = lambda x: a - x
        print(f"Saque realizado com sucesso! Valor atual é de R${saque(valor_saque):.2f}")
    else:
        print("Valor inválido ou maior que o saldo atual. Por favor, comece a operação novamente.")
        
##Extrato
elif mensagem_inicial == 3:
    print(f"Seu saldo atual é de R${valor_inicial}!")
    
##Outros
else:
    mensagem_inicial_outros = int(input("Bem vindo ao menu OUTROS. O que deseja fazer?\n[1]- Empréstimo [2]- Sair\n"))
    if mensagem_inicial_outros == 1:
        valor_empréstimo = float(input("Qual o valor do empréstimo?\nR$"))
        print(f"Empréstimo realizado com sucesso. Seu saldo atual é de R${valor_inicial+valor_empréstimo:.2f}!")
    else:
        print("Obrigado por utilizar nossos serviços.")







