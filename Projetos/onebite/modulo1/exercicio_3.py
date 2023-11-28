# 31 - Exercício 3

## Cálculo da Distância
"""Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas."""

km= float(input("Olá, seja bem vindo a Thorzinho Viagens. Para melhores ofertas, por favor informe qual será a distância -em KM- da sua próxima viagem.\n: "))
passagem1 = km * 0.50
passagem2 = km * 0.35
if km <= 200 and km >0:
    print(f"O valor da sua viagem será de R${passagem1:.2f}!\nObrigado por utilizar nosso serviços.")
elif km > 200:
    print(f"O valor da sua viagem será de R${passagem2:.2f}!\nObrigado por utilizar nosso serviços.")
else:
    print("Distância inválida. Por favor tente novamente.")