times = {}
autenticação = False

while not autenticação:

    print("O que deseja fazer?")
    print("Opção 1 - Criar time")
    print("Opção 2 - Adicionar jogador")
    print("Opção 3 - Listar times")
    print("Opção 4 - Escalação")
    print("Opção 5 - Remover time")
    print("Opção 6 - Remover jogador")
    print("Opção 7 - Sair")

    escolha = input("> ")
    if escolha == "1":
        nome_time = input("Qual o nome do time?\n")
        times[nome_time] = {'nome': nome_time, 'jogadores': []}
        print("\nTime adicionado!\n")
    elif escolha == "2":
        adicionar_time = input(
            "Informe o nome do time para adicionar o jogador\n")
        nome_jogador = input("Informe o nome do jogador\n")
        times[adicionar_time]['jogadores'].append(nome_jogador)
        print("\nJogador adicionado!\n")
    elif escolha == "3":
        for time in times.keys():
            print(f"{time}")
    elif escolha == "4":
        listar_jogadores = input("Escalação dos times")
        for nomedotime, dicionario in times.items():
            for i, j in dicionario.items():
                print(f"{i} - {j}")
    elif escolha == "5":
        remover_time = input("\nQual o nome do time que deseja remover?\n")
        del times[remover_time]
        print("\nTime removido com sucesso\n!")
    elif escolha == "6":
        pass
    elif escolha == "7":
        autenticação = True
        print("\nSaindo do sistema!\n")
