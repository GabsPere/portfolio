#README: Desafio realizado com o intuito de consolidar o conteúdo aprendido no primeiro módulo. É um sistem simples
# de gerenciamento de times, com adição e remoção de jogadores e times, além da listagem e escalação dos times.

times = {}
autenticação = False
divisoria = "-"

while not autenticação:

    print("\nO que deseja fazer?")
    print("Opção 1 - Criar time")
    print("Opção 2 - Adicionar jogador")
    print("Opção 3 - Listar times")
    print("Opção 4 - Escalação")
    print("Opção 5 - Remover time")
    print("Opção 6 - Remover jogador")
    print("Opção 7 - Sair")

    escolha = input("> ")
    if escolha == "1":
        nome_time = input(f"Qual o nome do time?\n{50*divisoria}\n")
        times[nome_time] = {'nome': nome_time, 'jogadores': []}
        print("\nTime adicionado!\n")
    elif escolha == "2":
        adicionar_time = input(
            f"Informe o nome do time para adicionar o jogador:\n{50*divisoria}\n")
        nome_jogador = input("Informe o nome do jogador:\n")
        times[adicionar_time]['jogadores'].append(nome_jogador)
        print("\nJogador adicionado!\n")
    elif escolha == "3":
        for time in times.keys():
            print(f"{time}\n")
    elif escolha == "4":
        listar_jogadores = input(f"\tEscalação dos times\n{50*divisoria}\n")
        for nomedotime, dicionario in times.items():
            for i, j in dicionario.items():
                print(f"{i} - {j}")
    elif escolha == "5":
        remover_time = input(
            f"\nQual o nome do time que deseja remover?\n{50*divisoria}\n")
        del times[remover_time]
        print("\nTime removido com sucesso!\n")
    elif escolha == "6":
        qual_time = input(
            f"De qual time você deseja remover o jogador?\n{50*divisoria}\n")
        qual_jogador = input("Qual o nome do jogador?\n")
        time_escolhido = times[qual_time]
        print(f"O time escolhido foi {time_escolhido}")
        times[qual_time]['jogadores'].remove(qual_jogador)
    elif escolha == "7":
        autenticação = True
        print("\nSaindo do sistema!\n")
