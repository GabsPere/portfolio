name = input("Digite o nome do jogo:\n")
year_launch = int(input("Digite o ano de lançamento:\n"))
classification = float(input("Digite a nota do jogo:\n"))

if classification >= 8.0 or year_launch > 2022:
    print(f"O jogo {name} é bom. Pode jogar!")
    
else:
    print(f"Nota do jogo {name} está abaixo do esperado. Não recomendo jogar!")