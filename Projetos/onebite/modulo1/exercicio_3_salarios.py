## Aumento salário funcionário

"""Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%."""

salario_atual = float(input("Olá, por motivos de reajuste salarial, precisamos que informe o valor atual do seu salário.\nR$:"))
reajuste_1 = salario_atual *0.10
reajuste_2 = salario_atual*0.15

if salario_atual > 1.250:
    print(f"Reajuste realizado com sucesso. Seu aumento foi de R${reajuste_1} e seu sálario passará a ser de R${salario_atual+reajuste_1:.2f}!")
elif salario_atual < 1.250 and salario_atual > 0:
    print(f"Reajuste realizado com sucesso. Seu aumento foi de R${reajuste_2} e seu salário passará a ser de R${salario_atual+reajuste_2:.2f}!")
else:
    print("Valor inválido. Por favor tente novamente.")